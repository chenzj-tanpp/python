from pyecharts.charts import Bar
from pyecharts.charts import Page
from pyecharts import options as opts
import pandas as pd
data=pd.read_excel("data/obama-approval-ratings.xls")
x=data["Issue"].values.tolist()
y1=data["Approve"].values.tolist()
y2=data["Disapprove"].values.tolist()
y3=data["None"].values.tolist()
#如果不加.values.tolist()出来的图表无数据
page=Page()
bar=Bar()
bar.add_xaxis(x)
bar.add_yaxis("支持",y1,stack=True)
bar.add_yaxis("不支持",y2,stack=True)
bar.add_yaxis("不发表意见",y3,stack=True)
bar.set_global_opts(title_opts=opts.TitleOpts(title="柱状图数据堆叠"),xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=13,rotate=-30)))
page.add(bar)
page.render("result/比例柱状堆叠图.html")