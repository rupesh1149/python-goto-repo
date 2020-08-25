import asyncio
import aiohttp

async def load_data(session, delay):
    print(f'starting {delay} second timer')
    async with session.get(f'http://httpbin.org/delay/{delay}') as resp:
        text = await resp.text()
        print(f'Completed {delay}' second timer)
        return text

async def main():
    start_time = default_timer()
    async with aiohttp.ClientSession()as session:
        # setup our task and get them running
        two_task = asyncio.create_task(load_data(session, 2))
        three_task = asyncio.create_task(load_data(session, 3))
        