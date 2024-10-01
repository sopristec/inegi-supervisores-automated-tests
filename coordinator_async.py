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
    async with aiohttp.ClientSession() as session:
        async with session.post(service_url, json=payload) as response:
            response_data = await response.json()
            print(f"Response: {response_data}")
            return response_data
    print(f"Request sent to {service_url} with payload {payload}")


# Worker function to handle requests for each file
async def worker(service_url, file_name, request_count, username, time_per_request):
    tasks = []
    payload = {"username": username, "file_name": file_name}

    print(f"count: {request_count}")

    for _ in range(request_count):
        tasks.append(asyncio.create_task(send_request(service_url, payload)))
        await asyncio.sleep(
            time_per_request
        )  # Pace the requests evenly within the hour

    await asyncio.gather(*tasks)


# Function to dynamically distribute requests to web services
async def distribute_requests(file_data, web_services):
    total_requests = sum(
        [entry["no_requests"] for entry in file_data]
    )  # Sum all requests
    num_services = len(web_services)

    # Calculate how many requests per second to fit within the hour
    requests_per_second = (
        total_requests / 3600.0
    )  # Total requests divided by 3600 seconds (1 hour)
    time_per_request = (
        1 / requests_per_second if requests_per_second > 0 else 0
    )  # Time delay between each request

    with ThreadPoolExecutor(max_workers=5 * num_services) as pool:
        loop = asyncio.get_event_loop()
        tasks = []

        for file_entry in file_data:
            username = file_entry["username"]
            file_name = file_entry["file_name"]
            no_requests = file_entry["no_requests"]

            # Distribute the requests evenly across the web services
            requests_per_service = no_requests // num_services
            remainder = no_requests % num_services  # Remainder for uneven distribution

            print(f"request_per_ {requests_per_service}")

            for i, service in enumerate(web_services):
                # Add one extra request for the first 'remainder' services
                extra_request = 1 if i < remainder else 0
                total_requests_for_service = requests_per_service + extra_request

                tasks.append(
                    loop.run_in_executor(
                        pool,
                        asyncio.run,
                        worker(
                            service,
                            file_name,
                            total_requests_for_service,
                            username,
                            time_per_request,
                        ),
                    )
                )

        await asyncio.gather(*tasks)


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

    WEB_SERVICES = [
        f"http://{HOST_WS_1}:8000/supervisores",
        f"http://{HOST_WS_2}:8000/supervisores",
        f"http://{HOST_WS_3}:8000/supervisores",
        f"http://{HOST_WS_4}:8000/supervisores",
        f"http://{HOST_WS_5}:8000/supervisores",
        f"http://{HOST_WS_6}:8000/supervisores",
        f"http://{HOST_WS_7}:8000/supervisores",
        f"http://{HOST_WS_8}:8000/supervisores",
        f"http://{HOST_WS_9}:8000/supervisores",
        f"http://{HOST_WS_10}:8000/supervisores",
    ]

    # Your JSON data
    json_file_path = sys.argv[1]

    # Load file information from JSON file
    file_data = load_file_data(json_file_path)

    # Run the distribution of requests
    asyncio.run(distribute_requests(file_data, WEB_SERVICES))
