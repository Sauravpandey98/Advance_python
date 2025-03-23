import aiohttp
import asyncio
import time
import requests

async def main():
    # let's get top 100 ranked pokemons
    url = "https://pokeapi.co/api/v2/pokemon"

    async with aiohttp.ClientSession() as session:
        for i in range(1, 101):
            async with session.get(url+f"/{i}") as response:
                data = await response.json()
                print(data["forms"][0]["name"])


def main_sync():
    url = "https://pokeapi.co/api/v2/pokemon"

    for i in range(1, 101):
        response = requests.get(url+f"/{i}")
        data = response.json()
        print(data["forms"][0]["name"])

#but is is important to implement the rate limiting in case of async requests
# to avoid getting banned from the server
# that can be done using semaphore and asyncio.sleep

async def main_with_rate_limit():
    url = "https://pokeapi.co/api/v2/pokemon"
    semaphore = asyncio.Semaphore(10)

    async with aiohttp.ClientSession() as session:
        for i in range(1, 101):
            async with semaphore: #will allow only 10 requests at a time
                async with session.get(url+f"/{i}") as response:
                    data = await response.json()
                    print(data["forms"][0]["name"])
                    await asyncio.sleep(1)

if __name__ == "__main__":
    start_time = time.time()
    # asyncio.run(main()) # 16 seconds
    # main_sync() #77.10 seconds
    asyncio.run(main_with_rate_limit())
    end_time = time.time()
    print(f"Time taken: {end_time-start_time} seconds")