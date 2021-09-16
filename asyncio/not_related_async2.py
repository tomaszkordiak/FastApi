import time
import requests
import asyncio
import aiohttp

api_key = 'XRTB2TWPCNYJ40QL'
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=demo'
symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'GOOG', 'TSLA', 'MSFT',
           'AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'GOOG', 'TSLA', 'MSFT',
           'AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'GOOG', 'TSLA', 'MSFT']

results = []

start = time.time()


def get_tasks(session):
    tasks = []
    for symbol in symbols:
        tasks.append(session.get(url.format(symbol, api_key), ssl=False))
    return tasks


async def get_symbols():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        responses = await asyncio.gather(*tasks)
        for response in responses:
            results.append(await response.json())


asyncio.run(get_symbols())
end = time.time()
print(f'Time: {end - start}')
