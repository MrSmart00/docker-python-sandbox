import asyncio

import greeting
import my_network

async def main():
    loop = asyncio.get_event_loop()
    task1 = loop.create_task(greeting.say_hallo_world())
    task2 = loop.create_task(my_network.async_get_request(20))
    await asyncio.gather(task1, task2)

asyncio.run(main())
