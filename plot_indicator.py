import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def plot_stock_with_indicators(stock_data, svwma, lvwma, esv, elv, vpvma, vpvmas, symbol):
    """
    Plots stock price data along with various technical indicators.

    This function generates three separate plots:
    1. Stock closing prices overlaid with Short and Long Volume Weighted Moving Averages (SVWMA, LVWMA).
    2. Exponential Moving Averages (ESV, ELV).
    3. Volume Price Volatility Moving Average (VPVMA) and its signal line (VPVMAS).

    Parameters:
        stock_data (pd.DataFrame): A DataFrame with a DateTimeIndex and columns including 'Open', 'High', 'Low', and 'Close'.
        svwma (list or np.array): Short Volume Weighted Moving Average.
        lvwma (list or np.array): Long Volume Weighted Moving Average.
        esv (list or np.array): Exponential Short Volume Moving Average.
        elv (list or np.array): Exponential Long Volume Moving Average.
        vpvma (list or np.array): Volume Price Volatility Moving Average.
        vpvmas (list or np.array): Signal line of VPVMA.
        symbol (str): Stock ticker symbol, used for naming saved plots.

    Returns:
        None: The function saves three separate PNG files in the "Results/Plots/" directory with filenames:
              "<symbol>1.png", "<symbol>2.png", and "<symbol>3.png".
    """

    # Ensure the inputs are consistent
    dates = stock_data.index
    Close_prices = stock_data[('Close',symbol)]
    save_path = "Results/Plots/" + symbol

    # Create the first figure for stock data, SVWMA, and LVWMA
    plt.figure(figsize=(12, 6))
    plt.plot(dates, Close_prices, label='Close Price', color='black', linewidth=1.5)
    plt.plot(dates, svwma, label='SVWMA', color='blue', linestyle='--')
    plt.plot(dates, lvwma, label='LVWMA', color='red', linestyle='--')

    # Format the chart
    plt.title('Stock Price with SVWMA and LVWMA')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    plt.xticks(rotation=45)

    # Save or show the first plot
    if save_path:
        plt.savefig(save_path + "1.png", dpi=300, bbox_inches='tight')


    # Create the second figure for stock data, ESV, and ESV
    plt.figure(figsize=(12, 6))
    plt.plot(dates, esv, label='ESV', color='blue', linestyle='--')
    plt.plot(dates, elv, label='ELV', color='red', linestyle='--')

    # Format the chart
    plt.title('ESV and ELV')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    plt.xticks(rotation=45)

    # Save or show the first plot
    if save_path:
        plt.savefig(save_path + "2.png", dpi=300, bbox_inches='tight')


    # Create the third figure for VPVMA and VPVMAS
    plt.figure(figsize=(12, 6))
    plt.plot(dates, vpvma, label='VPVMA', color='green', linewidth=1.5)
    plt.plot(dates, vpvmas, label='VPVMAS (Signal)', color='orange', linestyle='--')

    # Format the chart
    plt.title('VPVMA and Signal Line')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    plt.xticks(rotation=45)

    # Save or show the second plot
    if save_path:
        plt.savefig(save_path + "3.png", dpi=300, bbox_inches='tight')


def plot_buy_sell_points(stock_data, buy_points, sell_points, symbol):
    """
    Plots the stock price with buy and sell points.

    Parameters:
        stock_data (pd.DataFrame): The stock data containing the closing prices, indexed by date.
        buy_points (list): Indices representing the buy signals.
        sell_points (list): Indices representing the sell signals.
        symbol (str): The stock ticker symbol, used for naming the saved plot.

    Returns:
        None: The function saves the PNG file in the "Results/Plots/" directory with filename:
            "<symbol>5.png", 
    """

    plt.figure(figsize=(12,8))
    plt.style.use('default')

    # Fixed typo in 'label'
    plt.plot(stock_data.index, stock_data[('Close',symbol)], label='Market Close', color='Black', linewidth=1.5)
    
    # Ensure indices are within bounds
    for buy in buy_points:
        if buy < len(stock_data.index):
            plt.scatter(stock_data.index[buy], stock_data[('Close',symbol)].iloc[buy], color='#d62728', marker='o', s=100)

    for sell in sell_points:
        if sell < len(stock_data.index):
            plt.scatter(stock_data.index[sell], stock_data[('Close',symbol)].iloc[sell], color='#ff7f0e', marker='x', s=100)
    
    plt.title('VPVMA buy and sell points', fontsize=16)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Price', fontsize=14)
    plt.legend(facecolor='white', framealpha=1, edgecolor='black')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    save_path = "Results/Plots/" + symbol + "5.png"
    plt.savefig(save_path, dpi=300, bbox_inches='tight')


def plot_histogram(stock_data, histogram, symbol):
    """
    Plots a histogram representing the trading method.

    Parameters:
        stock_data (pd.DataFrame): The stock data.
        histogram (list or np.array): The calculated histogram values.
        symbol (str): The stock ticker symbol.

    Returns:
        None: The function saves the PNG file in the "Results/Plots/" directory with filename:
              "<symbol>4.png", 
    """
    plt.figure(figsize=(12, 8))
    plt.style.use('default')
    
    # Use bar plot for histogram with different colors for positive and negative values
    colors = ['green' if val > 0 else 'red' for val in histogram]
    plt.bar(stock_data.index, histogram, color=colors, width=1.0, label='Histogram')
    
    plt.title('VPVMA Histogram', fontsize=16)
    plt.xlabel('Date', fontsize=14)
    plt.legend(facecolor='white', framealpha=1, edgecolor='black')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    save_path = "Results/Plots/" + symbol + "4.png"
    plt.savefig(save_path, dpi=300, bbox_inches='tight')

