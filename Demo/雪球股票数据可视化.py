import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts

df = pd.read_csv('雪球股票.csv')
x = list(df['股票名称'].values)
y = list(df['成交量'])
c = (
    Bar()  # 新建空白柱状图
        .add_xaxis(x[:30])  # X轴数据
        .add_yaxis('成交量情况', y[:30])  # Y轴数据及名称
        .set_global_opts(
        title_opts=opts.TitleOpts(title='成交量图表'),
        datazoom_opts=opts.DataZoomOpts()
    )
)
c.render('成交量图表.html')
