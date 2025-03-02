def calculate_TP(stock_data,symbol):
    """
    Calculates the typical price

    Parameters:
        pd.DataFrame: The stock data
        symbol (str): The stock symbol to identify the relevant data.

    Returns:
        TP_Data (list): list containing the typical prices
    """

    TP_Data = []
    for i in range(len(stock_data)):
        TP_Data.append((stock_data[('High',symbol)].iloc[i] + stock_data[('Low',symbol)].iloc[i] + stock_data[('Close',symbol)].iloc[i]) / 3)
    
    return TP_Data

