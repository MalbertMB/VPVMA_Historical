from data_receiver import download_stock_data
from Compute.compute_TP import calculate_TP
from Compute.compute_VWMA import calculate_vwma
from Compute.compute_Std_volatility import calculate_daily_volatility
from Compute.compute_EMA import calculate_EMA
from Compute.compute_VPVMA import calculate_VPVMA
from Compute.compute_VPVMAS import calculate_VPVMAS


def vpvma(symbol, start_date, end_date, w_long, w_short, w_signal):
    """
    Computes the Volume-Weighted Price Volatility Moving Average (VPVMA) and its smoothed version (VPVMAS)  
    for a given stock over a specified time range.

    Parameters:
        symbol (str): The stock ticker symbol.
        start_date (str): The start date for fetching stock data (format: 'YYYY-MM-DD').
        end_date (str): The end date for fetching stock data (format: 'YYYY-MM-DD').
        w_long (int): The window size for the long-term Volume-Weighted Moving Average (VWMA).
        w_short (int): The window size for the short-term Volume-Weighted Moving Average (VWMA).
        w_signal (int): The smoothing window size for VPVMA.

    Returns:
        tuple: A tuple containing:
            - stock_data (pd.DataFrame): The stock data for the period.
            - SVWMA (np.array): The short-term VWMA values.
            - LVWMA (np.array): The long-term VWMA values.
            - ESV (np.array): The exponentially smoothed short-term VWMA.
            - ELV (np.array): The exponentially smoothed long-term VWMA.
            - VPVMA (np.array): The VPVMA values.
            - VPVMAS (np.array): The smoothed VPVMA values.

    Note:
        The function processes stock price and volume data, applies VWMA and EMA calculations,  
        and derives VPVMA to assess volatility-adjusted price trends.
    """

    stock_data = download_stock_data(symbol,start_date,end_date)

    TP_Data = calculate_TP(stock_data,symbol)

    SVWMA = calculate_vwma(TP_Data,stock_data[("Volume",symbol)],w_short)
    LVWMA = calculate_vwma(TP_Data,stock_data[("Volume",symbol)],w_long)

    SVWMA = SVWMA[-len(LVWMA):] #Due to the different windows the w_short will have more values

    DV = calculate_daily_volatility(stock_data[-len(LVWMA):],symbol)
    
    ESV = calculate_EMA(SVWMA,DV,w_short)
    ELV = calculate_EMA(LVWMA,DV,w_long)

    VPVMA = calculate_VPVMA(ESV,ELV)

    VPVMAS = calculate_VPVMAS(VPVMA,w_signal)
    length_result = len(VPVMAS)
    
    return stock_data[-length_result:],SVWMA[-length_result:],LVWMA[-length_result:],ESV[-length_result:],ELV[-length_result:],VPVMA[-length_result:],VPVMAS