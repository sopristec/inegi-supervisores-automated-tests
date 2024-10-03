import os
import aiohttp
import asyncio


async def send_request():
    payload = {
        "username": "USUARIO.SIM10",
        "file_name": "Eenvio_102111110_20240814_154132728_PVOLUMEN.zip",
        "no_requests": 1,
    }
    HOST_WS_1 = os.environ.get("HOST_WS_1", "localhost")
    service_url = f"http://{HOST_WS_1}:8000/supervisores"

    print(f"Sending to: {service_url}")

    async with aiohttp.ClientSession() as session:
        async with session.post(service_url, json=payload) as response:
            response_data = await response.json()
            print(f"Response: {response_data}")
            return response_data


# Run the asyncio loop
if __name__ == "__main__":
    asyncio.run(send_request())
