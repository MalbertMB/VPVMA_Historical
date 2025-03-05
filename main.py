from historical_tests import *
from fetch_stock_symbols import *


def main():
    """
    Main function to run the historical tests on a list of stock symbols.
    """
    
    print("1. Analyze Dow Jones Industrial Average stocks")
    print("2. Analyze S&P 500 stocks")
    print("3. Analyze NASDAQ stocks")
    print("4. Analyze underperforming stocks")
    print("5. Analyze custom stock symbols")
    choice = input("Enter your choice: ")

    if choice == "1":
        symbols = get_dow_jones_symbols()
    elif choice == "2":
        symbols = get_sp500_symbols()
    elif choice == "3":
        symbols = get_nasdaq_symbols()
    elif choice == "4":
        symbols = get_underperforming_symbols()
    elif choice == "5":
        symbols = input("Enter a list of stock symbols separated by a space: ").split()
    else:
        print("Invalid choice. Please enter a valid choice.")
        return 0
    
    historical_tests_xlsx(symbols, "2010-01-01", "2025-02-11",26,12,9,0.2)


def main_auxiliar():
    """
    Main function to run the historical tests on a list of stock symbols.
    Made to study the effect of the bandwidth parameter on the results.
    """
    
    dicc = {
        "Dow Jones average return" : [],
        "Dow Jones total trades" : [],
        "Dow Jones win rate" : [],
        "S&P 500 average return" : [],
        "S&P 500 total trades" : [],
        "S&P 500 win rate" : [],
        "Underperforming average return" : [],
        "Underperforming total trades" : [],
        "Underperforming win rate" : [],
    }
    for i in range(1, 10):
        bandwidth = i/10
        print("BANDWIDTH: ", bandwidth)
        print("\nDow Jones Industrial Average: \n")
        symbols = get_dow_jones_symbols()
        average_return, total_trades, win_rate =historical_tests_auxiliar(symbols, "2015-01-01", "2025-02-11",26,12,9,bandwidth)
        dicc["Dow Jones average return"].append(average_return)
        dicc["Dow Jones total trades"].append(total_trades)
        dicc["Dow Jones win rate"].append(win_rate)
        print("\n---Dow Jones Industrial Average results---")
        print("Average return: ", average_return)
        print("Total trades: ", total_trades)
        print("Win rate: ", win_rate)
        print("\n")
        print("S&P 500: \n")
        symbols = get_sp500_symbols()
        average_return, total_trades, win_rate =historical_tests_auxiliar(symbols, "2015-01-01", "2025-02-11",26,12,9,bandwidth)
        dicc["S&P 500 average return"].append(average_return)
        dicc["S&P 500 total trades"].append(total_trades)
        dicc["S&P 500 win rate"].append(win_rate)
        print("\n---S&P 500 results---")
        print("Average return: ", average_return)
        print("Total trades: ", total_trades)
        print("Win rate: ", win_rate)
        print("\n")
        print("Underperforming: \n")
        symbols = get_underperforming_symbols()
        average_return, total_trades, win_rate =historical_tests_auxiliar(symbols, "2015-01-01", "2025-02-11",26,12,9,bandwidth)
        dicc["Underperforming average return"].append(average_return)
        dicc["Underperforming total trades"].append(total_trades)
        dicc["Underperforming win rate"].append(win_rate)
        print("\n---Underperforming stocks results---")
        print("Average return: ", average_return)
        print("Total trades: ", total_trades)
        print("Win rate: ", win_rate)
        print("\n")
    
    with open('Results.txt', 'w') as file:
        file.write("VPVMA Results:\n")
        for key in dicc:
            file.write(key + ": " + str(dicc[key]) + "\n")
        

# Run the main function
main()