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


async def get_symbols():
    async with aiohttp.ClientSession() as session:
        for symbol in symbols:
            print(f'Working on symbol {symbol}')
            response = await session.get(url.format(symbol, api_key), ssl=False)
            results.append(await response.json())


asyncio.run(get_symbols())
end = time.time()
print(f'Time: {end - start}')
