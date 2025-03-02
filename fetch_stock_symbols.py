import pandas as pd
import requests
import json

def get_dow_jones_symbols():
    """
    Returns the list of Dow Jones Industrial Average stock symbols.

    Returns:
        list: A list of Dow Jones Industrial Average stock symbols.
    """

    dow_jones_symbols = [
        "AAPL", "AMZN", "AXP", "AMGN", "BA", "CAT", "CVX", "CSCO", "KO", "GS",
        "HD", "HON", "IBM", "INTC", "JNJ", "JPM", "MCD", "MMM", "MRK", "MSFT",
        "NKE", "PG", "TRV", "UNH", "VZ", "V", "WBA", "WMT", "DIS", "DOW", "CRM"]
    return dow_jones_symbols



def get_sp500_symbols():
    """
    Fetches the S&P 500 stock symbols from Wikipedia.

    Returns:
        list: A list of S&P 500 stock symbols.
    """

    url_sp500 = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    tables = pd.read_html(url_sp500)
    sp500_table = tables[0]
    sp500_symbols = sp500_table['Symbol'].tolist()
    return sp500_symbols


def get_nasdaq_symbols():
    """
    Fetches the NASDAQ stock symbols from a JSON file.
    
    Returns:
        dict: A dictionary containing NASDAQ stock symbols.
    """

    url = 'https://raw.githubusercontent.com/rreichel3/US-Stock-Symbols/main/nasdaq/nasdaq_tickers.json'
    response = requests.get(url)
    response.raise_for_status()
    nasdaq_symbols = response.json()
    return nasdaq_symbols

def get_underperforming_symbols():
    """
    Returns a list of underperforming stock symbols.

    Returns:
        list: A list of underperforming stock symbols.
    """

    stock_symbols = [
        "XOM", "CVX", "OXY", "MRO", "PXD", "HAL", "HES", "FTI", "VLO", "RIG", "APA", "COP", "MUR",
        "CRK","AA", "NEM", "FCX", "MOS", "DD", "LYB", "BHP", "RIO", "CF", "FMC",
        "GE", "F", "BA", "MMM", "UPS", "FDX", "RTX", "EMR", "ITT", "PPG", "X", "PWR",
        "KSS", "GPS", "JWN", "ODP", "DDS", "M", "DSW", "RL",
        "KHC", "GIS", "CPB", "K", "SJM", "CAG", "MO", "PM",
        "C", "BAC", "WFC", "USB", "PNC", "KEY", "RF", "TFC", "MET", "AIG", "COF",
        "BK", "TRV", "LNC", "PRU","T", "VZ", "LUMN",
        "DUK", "SO", "D", "EXC", "AEP", "XEL", "ED", "PEG",
        "PFE", "GILD", "BMY", "MRK", "BIIB", "UHS", "TEVA", "CVS",
        "IBM", "HPQ", "DELL", "CSCO", "INTC", "ORCL", "WDC", "NTAP", "XRX", "DXC",
        "SPG", "VNO", "SLG", "VTR", "EQR", "FRT", "WELL",
        "EMN", "WAB", "DOV", "SNA", "RSG", "CLX", "CHD", "KR", "WBA", "CCI",
        "MTB", "FRC", "FITB", "HBAN", "KSU", "ITW", "TXT", "CCL", "NCLH", "RCL",
        "LUV", "DAL", "AAL", "UAL", "DTE", "PCG", "WEC", "AES", "EXR", "OHI",
        "WST", "PKI", "IR", "QCOM", "MCK", "GD", "LHX", "NOC", "SWK", "URI",
        "FLS", "PRGO", "HUM", "RHI", "WMB", "KMI", "CMS", "WU", "SCHW", "HST",
        "O", "DRE", "AGNC", "INN", "WPC",
        "CINF", "MTZ", "SYY", "VFC", "KORS", "FL", "CZR", "MLM", "HIG", "PFG",
        "ZBH", "ITRI", "CSX", "SU", "BKR", "STT", "SIVB", "FSLR", "IRM", "CBRE",
        "JBHT", "CHRW", "PCAR", "TEL", "PKG", "DLTR", "KMX",
        "CFG", "FLO", "STX", "RMD", "EXPD", "ALLE", "HOLX", "CERN", "CTXS", "KRON",
        "EXPE", "TAP", "SEE", "VTRS", "ALK"]
    return stock_symbols


