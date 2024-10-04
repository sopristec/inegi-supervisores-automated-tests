import asyncio
from concurrent.futures import ThreadPoolExecutor
import os
import sys
import time
import random
import json
import aiohttp
import asyncio


# Placeholder async function for sending requests
async def send_request(service_url, payload):
    # await asyncio.sleep(random.uniform(0.01, 0.05))  # Simulate network latency
    print(f"Sending to: {service_url}")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(service_url, json=payload) as response:
                response_data = await response.json()
                print(f"Response: {response_data}")
                return response_data
    except aiohttp.ClientError as e:
        print(f"Request failed: {e}")
    print(f"Request sent to {service_url} with payload {payload}")


# Worker function to handle requests for each file
async def worker(service_url, file_name, username, tracking_dict):
    payload = {"username": username, "file_name": file_name}
    await send_request(service_url, payload)
    # Increment the counter for the file name in the tracking dictionary
    tracking_dict[file_name] += 1


# Function to dynamically distribute requests to web services
async def distribute_requests(file_data, web_services):
    total_requests = sum(
        [entry["no_requests"] for entry in file_data]
    )  # Sum all requests
    num_services = len(web_services)

    # Initialize a tracking dictionary for file names
    tracking_dict = {entry["file_name"]: 0 for entry in file_data}

    # Calculate how many requests per second to fit within the hour
    requests_per_second = (
        total_requests / num_services
    ) / 3600.0  # Total requests divided by 3600 seconds (1 hour)
    time_per_request = (
        1 / requests_per_second if requests_per_second > 0 else 0
    )  # Time delay between each request

    with ThreadPoolExecutor(max_workers=5 * num_services) as pool:
        loop = asyncio.get_event_loop()

        # Create an iterator for the file data
        file_data_iter = iter(file_data)

        while total_requests > 0:
            tasks = []  # Reset tasks for each round

            # Send requests to all 10 workers in parallel
            for i, service in enumerate(web_services):
                try:
                    # Get the next file entry
                    file_entry = next(file_data_iter)
                except StopIteration:
                    # Restart the iteration if we have reached the end
                    file_data_iter = iter(file_data)
                    file_entry = next(file_data_iter)

                username = file_entry["username"]
                file_name = file_entry["file_name"]

                # Check how many requests to send
                if file_entry["no_requests"] > 0:
                    tasks.append(
                        loop.run_in_executor(
                            pool,
                            asyncio.run,
                            worker(service, file_name, username, tracking_dict),
                        )
                    )

                    file_entry["no_requests"] -= 1
                    total_requests -= 1

                if total_requests <= 0:
                    break

            # Wait for all tasks (requests) to complete
            asyncio.gather(*tasks)

            print(f"time_per_request: {time_per_request}")
            # Sleep after sending requests to all workers (10 requests per batch)
            await asyncio.sleep(time_per_request)
    # Print how many files of each name were sent
    print("\nSummary of files sent:")
    for file_name, count in tracking_dict.items():
        print(f"{file_name}: {count} requests sent")


# Function to read file and N times data from the JSON file
def load_file_data(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


if __name__ == "__main__":
    # List of 10 web services
    HOST_WS_1 = os.environ.get("HOST_WS_1", "localhost")
    HOST_WS_2 = os.environ.get("HOST_WS_2", "localhost")
    HOST_WS_3 = os.environ.get("HOST_WS_3", "localhost")
    HOST_WS_4 = os.environ.get("HOST_WS_4", "localhost")
    HOST_WS_5 = os.environ.get("HOST_WS_5", "localhost")
    HOST_WS_6 = os.environ.get("HOST_WS_6", "localhost")
    HOST_WS_7 = os.environ.get("HOST_WS_7", "localhost")
    HOST_WS_8 = os.environ.get("HOST_WS_8", "localhost")
    HOST_WS_9 = os.environ.get("HOST_WS_9", "localhost")
    HOST_WS_10 = os.environ.get("HOST_WS_10", "localhost")

    endpoint = sys.argv[1]

    WEB_SERVICES = [
        f"http://{HOST_WS_1}:8000/{endpoint}",
        f"http://{HOST_WS_2}:8000/{endpoint}",
        f"http://{HOST_WS_3}:8000/{endpoint}",
        f"http://{HOST_WS_4}:8000/{endpoint}",
        f"http://{HOST_WS_5}:8000/{endpoint}",
        f"http://{HOST_WS_6}:8000/{endpoint}",
        f"http://{HOST_WS_7}:8000/{endpoint}",
        f"http://{HOST_WS_8}:8000/{endpoint}",
        f"http://{HOST_WS_9}:8000/{endpoint}",
        f"http://{HOST_WS_10}:8000/{endpoint}",
    ]

    # Your JSON data
    json_file_path = sys.argv[2]

    # Load file information from JSON file
    file_data = load_file_data(json_file_path)

    # Run the distribution of requests
    asyncio.run(distribute_requests(file_data, WEB_SERVICES))
