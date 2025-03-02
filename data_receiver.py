import yfinance as yf
import pandas as pd

def download_stock_data(symbol, start_date, end_date):
    """
    Download stock data for a given symbol between a specified start and end date.

    Parameters:
        symbol (str): The stock symbol to download data for.
        start_date (str): The starting date of the period to include, in the format "%Y-%m-%d".
        end_date (str): The ending date of the period to include, in the format "%Y-%m-%d".
    
    Returns:
        pd.DataFrame: The stock data with relevant columns: 'Open', 'High', 'Low', 'Close', and 'Volume'.
    """

    # Convert start_date and end_date from string to datetime
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    
    # Download stock data
    stock_data = yf.download(symbol, start=start_date.strftime("%Y-%m-%d"), end=end_date.strftime("%Y-%m-%d"))

    # Ensure relevant columns are available
    relevant_columns = ['Close', 'High', 'Low', 'Open', 'Volume']
    missing_columns = [col for col in relevant_columns if col not in stock_data.columns]
    if missing_columns:
        raise ValueError(f"download_stock_data: Some required columns are missing from the stock data: {missing_columns}")

    # Filter to keep only the relevant columns
    stock_data = stock_data[relevant_columns]
    return stock_data