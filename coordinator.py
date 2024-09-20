import os
import redis
import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor

# Redis configuration
REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = 6379
REDIS_LIST_KEY = os.environ.get("REDIS_LIST_KEY", "inegi_queue")

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
    f"http://{HOST_WS_1}:8000/supervisor",
    f"http://{HOST_WS_2}:8000/supervisor",
    f"http://{HOST_WS_3}:8000/supervisor",
    f"http://{HOST_WS_4}:8000/supervisor",
    f"http://{HOST_WS_5}:8000/supervisor",
    f"http://{HOST_WS_6}:8000/supervisor",
    f"http://{HOST_WS_7}:8000/supervisor",
    f"http://{HOST_WS_8}:8000/supervisor",
    f"http://{HOST_WS_9}:8000/supervisor",
    f"http://{HOST_WS_10}:8000/supervisor",
]

# Number of concurrent workers
NUM_WORKERS = os.environ.get("NUM_WORKERS", 10)

# Connect to Redis
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)


def send_to_web_service(message, service_url):
    """
    Send a message (JSON) to a web service.
    """
    try:
        response = requests.post(service_url, json=message)
        print(response.text)
        response.raise_for_status()  # Raise exception for HTTP errors
        print(f"Message sent to {service_url} with status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send message to {service_url}: {e}")


def distribute_message(message):
    """
    Distribute message to one of the web services.
    Use round-robin or random strategy.
    """
    # Round-robin example:
    service_index = distribute_message.counter % len(WEB_SERVICES)
    distribute_message.counter += 1
    service_url = WEB_SERVICES[service_index]

    # Send the message to the selected service
    send_to_web_service(message, service_url)


distribute_message.counter = 0  # Initialize counter for round-robin


def worker():
    """
    Worker that pulls messages from Redis and distributes them.
    """
    while True:
        # Pull message from Redis list (blocking call)
        message = r.lpop(REDIS_LIST_KEY)

        if message:
            # Convert message from bytes to JSON
            message = json.loads(message.decode("utf-8"))
            # Distribute the message to a web service
            distribute_message(message)
        else:
            # Sleep if no message is available to prevent busy waiting
            time.sleep(1)


def main():
    # Use a ThreadPoolExecutor to create concurrent workers
    with ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
        for _ in range(NUM_WORKERS):
            executor.submit(worker)


if __name__ == "__main__":
    main()
