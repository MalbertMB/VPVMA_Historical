import statistics

def calculate_daily_volatility(prices,symbol):
    """
    Calculate the daily volatility (standard deviation) of High, Low, Close, and Open values.

    Parameters:
        pd.DataFrame: The stock data.
        symbol (str): The stock symbol to identify the relevant data.

    Returns:
        stdev (list): The standard deviation of the prices
    """

    stdev = []
    for i in range(len(prices)):
        stdev.append(statistics.stdev([prices[('High',symbol)].iloc[i],prices[('Low',symbol)].iloc[i],prices[('Close',symbol)].iloc[i],prices[('Open',symbol)].iloc[i]]))

    return stdev
