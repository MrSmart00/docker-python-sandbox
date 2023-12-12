import asyncio

import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon/?limit=20&offset="


async def async_get_request(offset: int) -> dict:
    print(f"async request offset /{offset}")
    url = BASE_URL + str(offset)
    loop = asyncio.get_event_loop()
    res = await loop.run_in_executor(None, requests.get, url)
    json = res.json()
    print(json)
    print("=== async request done ===")
    return json
