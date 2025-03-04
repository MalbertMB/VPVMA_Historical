import pandas as pd

def calculate_TP(stock_data, symbol):
    """
    Calculates the typical price

    Parameters:
        stock_data (pd.DataFrame): The stock data
        symbol (str): The stock symbol to identify the relevant data.

    Returns:
        TP_Data (list): list containing the typical prices
    """
    
    # Calculate the typical price using vectorized operations
    high = stock_data[('High', symbol)]
    low = stock_data[('Low', symbol)]
    close = stock_data[('Close', symbol)]
    
    TP_Data = ((high + low + close) / 3).tolist()
    
    return TP_Data

"""------------------------- Potential Error -------------------------"""
#Before modification, the function returned a np.array "[np.float64(0.0)]" instead of a list "[0.0]"
