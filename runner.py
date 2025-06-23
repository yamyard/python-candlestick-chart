from fetcher import fetch_stock_data, prepare_candlestick_data
from plotter import create_candlestick_chart

def run_candlestick_workflow(
    symbol: str,
    start_date: str,
    end_date: str,
    output_file: str = "candlestick_chart.html",
    title: str = "Candlestick Chart",
    adjust: bool = False
):
    stock_data = fetch_stock_data(symbol, start = start_date, end = end_date, adjust = adjust)
    candlestick_data = prepare_candlestick_data(stock_data)
    create_candlestick_chart(stock_data, candlestick_data, output_file, title = title)
