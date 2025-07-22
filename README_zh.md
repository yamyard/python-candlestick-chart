# Python Candlestick Chart Generator
## 项目介绍
这是一个基于 Python 的股票K线图生成工具，使用 `yfinance` 获取股票历史数据，利用 `pyecharts` 绘制交互式K线图（HTML格式）
## 安装依赖
```
    pip install -r requirements.txt
```
## 使用说明
1. 修改配置文件  
支持json与yaml，以 `config.json` 为例如下
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
2. 运行程序
```
    python main.py
```
3. 查看结果  
用浏览器打开配置中 `output_file` 指定的 HTML 文件，查看交互式K线图

## 声明

本软件仅供教育和研究之用。并非财务建议。使用风险自负。
