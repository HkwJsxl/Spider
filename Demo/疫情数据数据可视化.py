from pyecharts.charts import Map
from pyecharts import options as opts
import pandas as pd

df = pd.read_csv('疫情数据.csv', encoding='utf-8')
print(df)
df.head()
area = df['area'].values.tolist()
curConfirm = df['curConfirm'].values.tolist()
china_map = (
    Map()  # 新建空白地图
        .add('现有确诊', [list(i) for i in zip(area, curConfirm)], 'china')
        .set_global_opts(
        title_opts=opts.TitleOpts(title='各地区确诊人数'),
        visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=True)
    )
)
china_map.render('各地区确诊人数.html')
