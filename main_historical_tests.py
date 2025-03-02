from main_VPVMA import historical_main_VPVMA
import pandas as pd


def historical_tests(symbols, start_date, end_date, w_long, w_short, w_signal, bandwidth):
    """
    Runs historical tests on a list of stock symbols using the Volume-Price Volatility Moving Average (VPVMA) indicator.

    Parameters:
        symbols (list): A list of stock ticker symbols.

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
        

def historical_tests_xlsx(symbols, start_date, end_date, w_long, w_short, w_signal, bandwidth):
    """
    Runs historical tests on a list of stock symbols using the Volume-Price Volatility Moving Average (VPVMA) indicator.

    Parameters:
        symbols (list): A list of stock ticker symbols.

    Returns:
        None
    """
    results = []
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
            print(f"Error with symbol: {symbol} {str(e)}")
            results.append([symbol, "Error", "Error", "Error"])
    
    # Convert results to DataFrame
    df = pd.DataFrame(results, columns=["Symbol", "Average Profit per Trade (%)", "Number of Trades", "Win Rate (%)"])
    df.to_excel("Results.xlsx", index=False)
    
    print("Results saved to Results.xlsx")



def historical_tests_auxiliar(symbols, start_date, end_date, w_long, w_short, w_signal, bandwidth):

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
