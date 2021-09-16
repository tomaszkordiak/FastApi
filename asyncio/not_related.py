import time

import requests
import os

api_key = 'XRTB2TWPCNYJ40QL'
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=demo'
symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'GOOG', 'TSLA', 'MSFT',
           'AAPL', 'GOOG', 'TSLA', 'MSFT','AAPL', 'GOOG', 'TSLA', 'MSFT','AAPL', 'GOOG', 'TSLA', 'MSFT',
           'AAPL', 'GOOG', 'TSLA', 'MSFT','AAPL', 'GOOG', 'TSLA', 'MSFT','AAPL', 'GOOG', 'TSLA', 'MSFT']

results = []
start = time.time()
for symbol in symbols:
    print(f'Working on symbol {symbol}')
    response = requests.get(url.format(symbol, api_key))
    results.append(response.json())
end = time.time()
print(f'It took {end - start} seconds to make {len(symbols)} API calls')
print('You did it!')
