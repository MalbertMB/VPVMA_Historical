import json

def get_dow_jones_symbols():
    """
    Returns the list of Dow Jones Industrial Average stock symbols.

    Returns:
        list: A list of Dow Jones Industrial Average stock symbols.
    """
    # Load the data from the JSON file
    with open('Tickers/dow_jones_tickers.json', 'r') as file:
        data = json.load(file)

    return data


def get_sp500_symbols():
    """
    Fetches the S&P 500 stock symbols from Wikipedia.

    Returns:
        list: A list of S&P 500 stock symbols.
    """
    # Load the data from the JSON file
    with open('Tickers/sp500_tickers.json', 'r') as file:
        data = json.load(file)

    return data




get_sp500_symbols()

def get_nasdaq_symbols():
    """
    Fetches the NASDAQ stock symbols from a JSON file.
    
    Returns:
        dict: A dictionary containing NASDAQ stock symbols.
    """
    # Load the data from the JSON file
    with open('Tickers/nasdaq_tickers.json', 'r') as file:
        data = json.load(file)

    return data

    

def get_underperforming_symbols():
    """
    Returns a list of underperforming stock symbols.

    Returns:
        list: A list of underperforming stock symbols.
    """
    # Load the data from the JSON file
    with open('Tickers/underperforming_tickers.json', 'r') as file:
        data = json.load(file)

    return data



