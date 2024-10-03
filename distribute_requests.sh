#!/bin/bash

# Function to send a request using curl
send_request() {
    service_url=$1
    payload=$2

    echo "Sending to: $service_url"
    response=$(curl -s -X POST "$service_url" -H "Content-Type: application/json" -d "$payload")
    echo "Response: $response"
}

# Function to handle requests for each file
worker() {
    service_url=$1
    file_name=$2
    username=$3

    payload="{\"username\": \"$username\", \"file_name\": \"$file_name\"}"
    send_request "$service_url" "$payload"
}

# Function to dynamically distribute requests to web services
distribute_requests() {
    file_data=$1
    web_services=("${!2}")
    total_requests=$(jq '[.[] | .no_requests] | add' <<< "$file_data")
    num_services=${#web_services[@]}

    requests_per_second=$(echo "$total_requests / $num_services / 3600" | bc -l)
    time_per_request=$(echo "1 / $requests_per_second" | bc -l)

    while [ "$total_requests" -gt 0 ]; do
        for service_url in "${web_services[@]}"; do
            file_entry=$(jq -c '.[] | select(.no_requests > 0)' <<< "$file_data" | head -n 1)
            if [ -z "$file_entry" ]; then
                break
            fi

            username=$(jq -r '.username' <<< "$file_entry")
            file_name=$(jq -r '.file_name' <<< "$file_entry")

            worker "$service_url" "$file_name" "$username" &

            # Update file entry to reduce no_requests
            file_data=$(jq "(.[] | select(.file_name == \"$file_name\").no_requests) -= 1" <<< "$file_data")
            total_requests=$((total_requests - 1))

            if [ "$total_requests" -le 0 ]; then
                break
            fi
        done

        sleep "$time_per_request"
    done
}

# Main script execution starts here
HOST_WS_1=${HOST_WS_1:-localhost}
HOST_WS_2=${HOST_WS_2:-localhost}
HOST_WS_3=${HOST_WS_3:-localhost}
HOST_WS_4=${HOST_WS_4:-localhost}
HOST_WS_5=${HOST_WS_5:-localhost}
HOST_WS_6=${HOST_WS_6:-localhost}
HOST_WS_7=${HOST_WS_7:-localhost}
HOST_WS_8=${HOST_WS_8:-localhost}
HOST_WS_9=${HOST_WS_9:-localhost}
HOST_WS_10=${HOST_WS_10:-localhost}

endpoint=$1
json_file_path=$2

WEB_SERVICES=(
    "http://$HOST_WS_1:8000/$endpoint"
    "http://$HOST_WS_2:8000/$endpoint"
    "http://$HOST_WS_3:8000/$endpoint"
    "http://$HOST_WS_4:8000/$endpoint"
    "http://$HOST_WS_5:8000/$endpoint"
    "http://$HOST_WS_6:8000/$endpoint"
    "http://$HOST_WS_7:8000/$endpoint"
    "http://$HOST_WS_8:8000/$endpoint"
    "http://$HOST_WS_9:8000/$endpoint"
    "http://$HOST_WS_10:8000/$endpoint"
)

# Read the JSON file
file_data=$(cat "$json_file_path")

# Run the distribution of requests
distribute_requests "$file_data" WEB_SERVICES[@]
