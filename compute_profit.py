def calculate_profit_timeframe(stock_data, buy_points, sell_points, symbol):
    """
    Calculate the average return and the number of winning trades based on buy and sell points.

    Parameters:
        stock_data (pd.DataFrame): A pandas DataFrame containing stock price data.
        buy_points (list): A list of indices representing buy points in the stock data.
        sell_points (list): A list of indices representing sell points in the stock data.
        symbol (str): The stock symbol to identify the relevant data.

    Returns:
        tuple: A tuple containing:
               - Average return (float): The average of all trade returns.
               - Number of winning trades (int): The count of trades with positive returns.

    Note:
        If `buy_points` and `sell_points` have mismatched lengths, the extra entries will be ignored.
    """

    # Adjust buy and sell points to match lengths
    length_buy = len(buy_points)
    length_sell = len(sell_points)
    if length_buy > length_sell:
        buy_points = buy_points[:length_sell]
    elif length_buy < length_sell:
        sell_points = sell_points[:length_buy]

    # Initialize variables
    wins = 0
    profit = []

    # Calculate profit for each trade
    for tb, ts in zip(buy_points, sell_points):
        # Ensure valid trade
        result = None
        if tb < ts:
            buy_price = stock_data[('Close', symbol)].iloc[tb]
            sell_price = stock_data[('Close', symbol)].iloc[ts]
            result = sell_price / buy_price
        elif tb > ts:
            buy_price = stock_data[('Close', symbol)].iloc[ts]
            sell_price = stock_data[('Close', symbol)].iloc[tb]
            result = buy_price / sell_price

            
        # Count wins and record profit
        if result > 1:
            wins += 1
        if result == None:
            raise ValueError("This motherfucker buys and sells at the same time")
        
        profit.append(result)

    # Handle case where no trades were valid
    if not profit:
        return 0, wins

    # Return average profit and number of wins
    return sum(profit) / len(profit), wins
