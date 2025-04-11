# fetch_from_api.py

import requests

API_KEY = "your_alpha_vantage_api_key"
SYMBOL = "AAPL"
INTERVAL = "5min"

url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={SYMBOL}&interval={INTERVAL}&apikey={API_KEY}"

response = requests.get(url)
data = response.json()

print(data)