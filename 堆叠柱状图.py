from pyecharts.charts import Bar,Scatter3D
from pyecharts.charts import Page
import csv
from pyecharts import options as opts
import pandas as pd
page = Page()
bar1=   Bar() ##定义为柱状图
bar1.set_global_opts(title_opts=opts.TitleOpts(title='柱状图数据堆叠示例'))

filename = "data/hot-dog-places.csv"
data=pd.read_csv("data/hot-dog-places.csv")
datax = []
datay = []
with open(filename) as f:
    reader = csv.reader(f)
    for datarow in reader:
           datax.append(datarow)
y1=datax[1]
y2=datax[2]
y3=datax[3]
bar1.add_xaxis(datax[0]) ##X轴的值
bar1.add_yaxis('A',y1,stack=True)
bar1.add_yaxis('B',y2,stack=True)
bar1.add_yaxis('C',y3,stack=True)

page.add(bar1)
page.render("result/热狗.html")