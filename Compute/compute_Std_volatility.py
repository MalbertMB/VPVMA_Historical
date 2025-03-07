import pandas as pd

def calculate_daily_volatility(prices, symbol):
    """
    Calculate the daily volatility (standard deviation) of High, Low, Close, and Open values.

    Parameters:
        prices (pd.DataFrame): The stock data.
        symbol (str): The stock symbol to identify the relevant data.

    Returns:
        list: The standard deviation of the prices for each day.
    """
    
    
    # Extract the relevant columns
    high = prices[('High', symbol)]
    low = prices[('Low', symbol)]
    close = prices[('Close', symbol)]
    open_ = prices[('Open', symbol)]
    
    # Calculate the standard deviation for each row
    stdev = (pd.concat([high, low, close, open_], axis=1)
               .std(axis=1)
               .tolist())
    
    return stdev