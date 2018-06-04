from dotenv import load_dotenv
import json
import os
import requests
from IPython import embed

load_dotenv() # loads environment variables set in a ".env" file, including the value of the ALPHAVANTAGE_API_KEY variable

# see: https://www.alphavantage.co/support/#api-key
api_key = os.environ.get("ALPHAVANTAGE_API_KEY") or "OOPS. Please set an environment variable named 'ALPHAVANTAGE_API_KEY'."

symbol = "NFLX" #TODO: capture user input

# see: https://www.alphavantage.co/documentation/#daily
# assemble the request url to get daily data for the given stock symbol
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

# issue a "GET" request to the specified url, and store the response in a variable
response = requests.get(request_url)

# parse the JSON response
response_body = json.loads(response.text)

# traverse the nested response data structure to find the latest closing price
metadata = response_body["Meta Data"]
data = response_body["Time Series (Daily)"]
dates = list(data)
latest_daily_data = data[dates[1]]
#> {'1. open': '353.8000',
#> '2. high': '355.5300',
#> '3. low': '350.2100',
#> '4. close': '351.6000',
#> '5. volume': '6921687'}
latest_price = latest_daily_data["4. close"]
latest_price = float(latest_price)
latest_price_usd = "${0:,.2f}".format(latest_price)
print(f"LATEST DAILY CLOSING PRICE FOR {symbol} IS: {latest_price_usd}")
