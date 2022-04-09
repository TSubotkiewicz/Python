import requests
from pprint import pprint

params1 = {
    "apikey": "75SSAA0C6CUP4KA7",
    "function": "TIME_SERIES_INTRADAY",
    "symbol": "IBM",
    "interval": "15min"
}

params2 = {
    "apikey": "75SSAA0C6CUP4KA7",
    "function": "INCOME_STATEMENT",
    "symbol": "AAPL",
}


def query_alphavantage(params):
    pprint(params)
    return requests.get('https://www.alphavantage.co/query?', params=params)


response1 = query_alphavantage(params1)
response2 = query_alphavantage(params2)
data = response1.json()
data2 = response2.json()

prices = data.get('Time Series (15min)')
volume = [int(price.get('5. volume')) for date, price in prices.items()]

pprint(sorted(volume))

# pprint(data2)
