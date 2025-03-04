from vpvma_indicator import vpvma
from plot_indicator import plot_buy_sell_points, plot_stock_with_indicators, plot_histogram
from compute_histogram import calculate_histogram
from compute_logic_VPVMA import buy_sell_analysis_timeframe
from compute_profit import calculate_profit_timeframe

def historical_main_VPVMA(symbol, start_date, end_date, w_long, w_short, w_signal, bandwidth, plot = False):
    """
    Implements a trading algorithm that analyzes stock data using Volume-Weighted Moving Averages (VWMA).  

    Parameters:
        symbol (str): The stock ticker symbol.  
        start_date (str): The start date for data analysis.  
        end_date (str): The end date for data analysis.  
        w_long (int): Window size for the long-term VWMA.  
        w_short (int): Window size for the short-term VWMA.  
        w_signal (int): Window size for the signal VWMA.  
        bandwidth (float): Threshold for buy/sell signal analysis.
        plot (boolean): Boolean to plot the results

    Returns:
        tuple: A tuple containing:  
            - profit (float): Total profit from executed trades.  
            - wins (int): Number of successful trades.  
            - trade_count (int): Total number of trades executed.  
    """
    stock_data, SVWMA, LVWMA, ESV, ELV, VPVMA, VPVMAS = vpvma(symbol, start_date, end_date, w_long, w_short, w_signal)
    buy_points, sell_points = buy_sell_analysis_timeframe(VPVMA, VPVMAS, bandwidth)
    profit, wins = calculate_profit_timeframe(stock_data, buy_points, sell_points, symbol)
    histogram = calculate_histogram(VPVMA, VPVMAS)

    #Plot the stock data with indicators
    if plot:
        plot_stock_with_indicators(stock_data, SVWMA, LVWMA, ESV, ELV, VPVMA, VPVMAS, symbol)
        plot_buy_sell_points(stock_data,buy_points,sell_points, symbol)
        plot_histogram(stock_data, histogram, symbol)

    return profit, wins, len(buy_points)