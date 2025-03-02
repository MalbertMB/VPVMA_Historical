import requests
import json

# URL of the raw JSON file containing NASDAQ tickers
url = 'https://raw.githubusercontent.com/rreichel3/US-Stock-Symbols/main/nasdaq/nasdaq_tickers.json'

try:
    # Fetch the data from the URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Parse the JSON content
    nasdaq_symbols = response.json()

    # Display the first 10 symbols as a sample
    print(nasdaq_symbols)

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"An error occurred: {err}")
