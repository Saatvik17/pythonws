from timeit import default_timer
import asyncio
import aiohttp

async def load_data(session , delay):
    print(f"Starting {delay} second timer")
    async with session.get(f"https://httpbin.org/delay/{delay}") as resp:
        text = await resp.text()
        print(f"Completed {delay} second timer")
        return text

async def main():
    start_time = default_timer()

    async with aiohttp.ClientSession() as session :

        task_two = asyncio.create_task(load_data(session , 2))
        task_three = asyncio.create_task(load_data(session , 3))


        await asyncio.sleep(1)
        print("entering concurrency sorta")

        result_two = await task_two
        result_three = await task_three

        

        elapsed_time = default_timer() - start_time

        print(f"The program took {elapsed_time:.2} seconds")

asyncio.run(main())        