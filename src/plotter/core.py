import pyecharts.options
from pyecharts.charts import Kline

def create_candlestick_chart(stock_data, candlestick_data, output_file: str, title: str = "Candlestick Chart"):
    candlestick_chart = (
        Kline()
        .add_xaxis(stock_data.index.strftime('%Y-%m-%d').tolist())
        .add_yaxis(series_name = title, y_axis = candlestick_data)
        .set_global_opts(
            xaxis_opts = pyecharts.options.AxisOpts(is_scale = True),
            yaxis_opts = pyecharts.options.AxisOpts(is_scale = True),
            title_opts = pyecharts.options.TitleOpts(title = title),
            datazoom_opts = [pyecharts.options.DataZoomOpts()],
            toolbox_opts = pyecharts.options.ToolboxOpts(
                feature={
                    "dataZoom": {"yAxisIndex": "none"},
                    "restore": {},
                    "saveAsImage": {},
                }
            ),
        )
    )
    candlestick_chart.render(output_file)
