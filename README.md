# Python Candlestick Chart Generator
## Project Overview
This is a Python-based tool for generating candlestick (K-line) charts for stock data. It uses `yfinance` to fetch historical stock data and `pyecharts` to render interactive candlestick charts in HTML format.
## Install Dependencies
```
    pip install -r requirements.txt
```
## Usage Instructons
1. Edit the configuration file (supports JSON and YAML). Here is an example using `config.json` :
```
    {
      "symbol": "^IXIC",
      "start_date": "2024-01-01",
      "end_date": "2024-12-31",
      "output_file": "nasdaq_candlestick_chart.html",
      "title": "NASDAQ Composite Index",
      "adjust": false
    }
```
2.  Run Program
```
    python main.py
```
3. View Result  
Open the HTML file specified in `output_file` with a browser to see the interactive candlestick chart.
