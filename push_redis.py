import os
import redis
import json

# Connect to Redis
r = redis.Redis(host=os.environ.get("REDIS_HOST", "localhost"), port=6379, db=0)

# Define the list key
list_key = os.environ.get("REDIS_LIST_KEY", "inegi_queue")

# Example JSON object
data = {
    "username": "USUARIO.SIM10",
    "file_name": "Eenvio_102111110_20240814_154132728_PVOLUMEN.zip",
}

# Push JSON to the Redis list (convert dict to JSON string)
r.rpush(list_key, json.dumps(data))

# # Retrieve the first element from the list
# first_element = r.lpop(list_key)

# # If not None, decode the byte and parse the JSON string back to a Python dictionary
# if first_element:
#     first_element = json.loads(first_element.decode('utf-8'))
#     print(f'First element (as JSON): {first_element}')
