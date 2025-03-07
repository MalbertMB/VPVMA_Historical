from vpvma_interpreter import historical_main_VPVMA
import pandas as pd

def historical_tests_xlsx(symbols, start_date, end_date, w_long, w_short, w_signal, bandwidth):
    """
    Runs historical tests on a list of stock symbols using the Volume-Price Volatility Moving Average (VPVMA) indicator and saves the results to an Excel file.

    Parameters:
        symbols (list): A list of stock ticker symbols.
        start_date (str): The start date for data analysis.
        end_date (str): The end date for data analysis.
        w_long (int): Window size for the long-term VWMA.
        w_short (int): Window size for the short-term VWMA.
        w_signal (int): Window size for the signal VWMA.
        bandwidth (float): Threshold for buy/sell signal analysis.

    Returns:
        None
    """
    results = []
    errors = []
    total_trades = 0
    total_wins = 0
    total_profit = []
    
    for symbol in symbols:
        try:
            aux_profit, wins, aux_trades = historical_main_VPVMA(symbol, start_date, end_date, w_long, w_short, w_signal, bandwidth)
            profit_percentage = (aux_profit - 1) * 100
            win_rate = (wins / aux_trades) * 100 if aux_trades > 0 else 0
            
            results.append([symbol, profit_percentage, aux_trades, win_rate])
            
            total_profit.append(aux_profit)
            total_trades += aux_trades
            total_wins += wins
            
            print(f"{symbol}: Average Profit per Trade: {profit_percentage:.2f}%, Number of Trades: {aux_trades}, Win Rate: {win_rate:.2f}%")
        except Exception as e:
            print(f"Error with symbol: {symbol}")
            errors.append(symbol +": "+ str(e))
    
    # Convert results to DataFrame
    df = pd.DataFrame(results, columns=["Symbol", "Average Profit per Trade (%)", "Number of Trades", "Win Rate (%)"])
    df.to_excel("Results.xlsx", index=False)
    
    # Save errors to text file
    with open("Errors.txt", "w") as file:
        for error in errors:
            file.write(error + "\n")
    
    print("Results and Errors saved to Results.xlsx and Errors.txt")
    return None


def historical_tests_txt(symbols, start_date, end_date, w_long, w_short, w_signal, bandwidth):
    """
    Runs historical tests on a list of stock symbols using the Volume-Price Volatility Moving Average (VPVMA) indicator and saves the results to a text file.

    Parameters:
        symbols (list): A list of stock ticker symbols.
        start_date (str): The start date for data analysis.
        end_date (str): The end date for data analysis.
        w_long (int): Window size for the long-term VWMA.
        w_short (int): Window size for the short-term VWMA.
        w_signal (int): Window size for the signal VWMA.
        bandwidth (float): Threshold for buy/sell signal analysis.

    Returns:
        None
    """

    profit = []
    trades = 0
    total_wins = 0
    with open('Results.txt', 'w') as file:
        file.write("VPVMA Results:\n")
        for symbol in symbols:
            try:
                aux_profit, wins, aux_trades = historical_main_VPVMA(symbol, start_date, end_date, w_long, w_short, w_signal, bandwidth)
                string = symbol + ": " + str((aux_profit-1)*100) +"% Number of trades: "+ str(aux_trades) + "\n"
                file.write(string)
                profit.append(aux_profit)
                trades += aux_trades
                total_wins += wins
                print(symbol + ": " + str(aux_profit) + "\nWins: " + str(wins) + "\nTotal trades: " + str(aux_trades))
                print("Average profit: " + str((sum(profit)/len(profit) - 1) * 100) + "%\nTotal trades: " + str(trades) + "\nWin rate: " + str((total_wins/trades)*100) +"%")
                string = symbol + ": Average profit: " + str((sum(profit)/len(profit) - 1) * 100) + "% Total trades: " + str(trades) + " Win rate: " + str((total_wins/trades)*100) +"%"
                file.write(string)
            except Exception as e: 
                print("Error with symbol: " + symbol + " " + str(e))
                file.write("Error with symbol: " + symbol + " " + str(e))
    print("Results saved to Results.txt")
    return None


def historical_tests_auxiliar(symbols, start_date, end_date, w_long, w_short, w_signal, bandwidth):
    """
    Runs historical tests on a list of stock symbols using the Volume-Price Volatility Moving Average (VPVMA) indicator.

    Parameters:
        symbols (list): A list of stock ticker symbols.
        start_date (str): The start date for data analysis.
        end_date (str): The end date for data analysis.
        w_long (int): Window size for the long-term VWMA.
        w_short (int): Window size for the short-term VWMA.
        w_signal (int): Window size for the signal VWMA.
        bandwidth (float): Threshold for buy/sell signal analysis.
    
    Returns:
        average_profit (float): The average profit percentage across all symbols.
        total_trades (int): The total number of trades executed.
        win_rate (float): The win rate percentage across all symbols.
    """


    profit = []
    trades = 0
    total_wins = 0
    for symbol in symbols:
        try:
            aux_profit, wins, aux_trades = historical_main_VPVMA(symbol, start_date, end_date, w_long, w_short, w_signal, bandwidth)
            profit.append(aux_profit)
            trades += aux_trades
            total_wins += wins
            print(symbol + ": " + str(aux_profit) + "\nWins: " + str(wins) + "\nTotal trades: " + str(aux_trades))
            print("Average profit: " + str((sum(profit)/len(profit) - 1) * 100) + "%\nTotal trades: " + str(trades) + "\nWin rate: " + str((total_wins/trades)*100) +"%")
        except Exception as e: 
            print("Error with symbol: " + symbol + " " + str(e))
    return (sum(profit)/len(profit) - 1) * 100, trades, (total_wins/trades)*100
