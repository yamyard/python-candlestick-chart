import yfinance
import pandas

def fetch_stock_data(symbol: str, start: str, end: str, adjust= False) -> pandas.DataFrame:
    stock_data = yfinance.download(symbol, start=start, end=end, auto_adjust=adjust)
    if isinstance(stock_data.columns, pandas.MultiIndex):
        stock_data.columns = stock_data.columns.get_level_values(0)
    stock_data = stock_data.dropna(subset=['Open', 'High', 'Low', 'Close'])
    return stock_data

def prepare_candlestick_data(stock_data: pandas.DataFrame) -> list[list[float]]:
    candlestick_data = []
    for _, row in stock_data.iterrows():
        candlestick_data.append([row['Open'], row['Close'], row['Low'], row['High']])
    return candlestick_data
