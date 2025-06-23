# Python Candlestick Chart Generator

## 项目介绍
这是一个基于 Python 的股票K线图生成工具，使用 `yfinance` 获取股票历史数据，利用 `pyecharts` 绘制交互式K线图（HTML格式）。
## 目录结构
```
    python-candlestick-chart/
    │
    ├── fetcher.py # 数据获取与预处理模块
    ├── plotter.py # K线图绘制模块
    ├── runner.py # 运行流程控制模块
    ├── main.py # 程序入口，读取配置并启动
    ├── config.json # 配置文件示例
    └── README.md # 项目说明文件
```
## 安装依赖
```
    pip install yfinance pyecharts pandas
```
## 使用说明
1. 修改配置文件 `config.json`，示例如下
```
    {
      "symbol": "000001.SS",
      "start_date": "2024-01-01",
      "end_date": "2024-12-31",
      "output_file": "shanghai_index_kline.html",
      "title": "SSE Candlestick Chart",
      "adjust": false
    }
```
2. 运行程序
```
    python main.py
```
3. 查看结果
用浏览器打开配置中 `output_file` 指定的 HTML 文件，查看交互式K线图
