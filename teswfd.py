from pyecharts.charts import Line,Bar,Pie,Scatter,Boxplot
from pyecharts import options as opts
from pyecharts.charts import Page
import pandas as pd
import csv
import sys
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
"""
多项式拟合工具
filename="data/unemployment-rate-1948-2010.csv"
ya=[]
xa=[]
try:
    with open(filename) as f:
        reader=csv.reader(f)
        for datarow in reader:
            if reader.line_num!=-1:
                ya.append(float(datarow[3]))
                # print(datarow[3])
                xa.append(int(datarow[1]))
except csv.Error:
    print("Erroe resding")
    sys.exit(-1)
plt.figure()
plt.scatter(xa[:],ya[:],s=10,c='g',marker='o',alpha=0.5)
ploy=np.polyfit(xa,ya,deg=3)
plt.plot(xa,np.polyval(ploy,xa))
plt.show()

"""
"""
#图3-6
#pyecharts实现

data=pd.read_csv("data/world-population.csv")
datax=data["Year"]
datay=data["Population"]
line=(
    Line()
    .add_xaxis(datax)
    # .add_xaixs(datax)
    .add_yaxis("",datay)
    .set_global_opts(title_opts=opts.TitleOpts("sdfjsgjfs"),
                     xaxis_opts=opts.AxisOpts(min_="1960"),
                     yaxis_opts=opts.AxisOpts(min_=3000000000),
                     )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .render("test.html")
)

#matplotlib实现
plt.plot(datax,datay)
plt.show()
"""

"""
阶梯图
# datax = [1995,1996,1997,1998, 1999,2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,2009]
# int数据当x轴显示不出数据
datax = ['1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008','2009']
datay = [0.32, 0.32, 0.32, 0.32, 0.33, 0.33, 0.34, 0.37, 0.37, 0.37, 0.37, 0.39, 0.41, 0.42, 0.44]
line=(
    Line()
    .add_xaxis(datax)
    .add_yaxis("",datay,is_step=True)
    .set_global_opts(title_opts=opts.TitleOpts("阶梯图"),
                     yaxis_opts=opts.AxisOpts(min_=0.3),
                     )
    .set_series_opts()
    .render("result/jieti.html")
)

"""

"""柱状图
data=pd.read_csv("data/hot-dog-contest-winners.csv")
datax=data["Year"].values.tolist()
datay=data["Dogs eaten"].values.tolist()
# print(datay)
bar=(
    Bar()
    .add_xaxis(datax)
    .add_yaxis("",datay)
    .set_global_opts(title_opts=opts.TitleOpts("柱状图"))
    .render("result/zhu.html")
)
"""

"""
比例堆叠柱状图
data=pd.read_csv("data/hot-dog-places.csv")
data=data.T
datax=data.index.tolist()
y1=data[0].values.tolist()
y2=data[1].values.tolist()
y3=data[2].values.tolist()
bar=(
    Bar()
    .add_xaxis(datax)
    .add_yaxis("A",y1,stack=True)
    .add_yaxis("B",y2,stack=True)
    .add_yaxis("C",y3,stack=True)
    .set_global_opts(title_opts=opts.TitleOpts("柱状图"))
    .render("result/zhudui.html")
)
"""
"""
#图4-2
data=pd.read_csv("data/vote_result.csv")
datab=data["Areas_of_interest"].values.tolist()
data_num=data["Votes"].values.tolist()
print(data.values.tolist())
pie=(
    Pie()
    .add("感兴趣的领域",data.values.tolist(),radius=[80,150])#center=[水平,垂直]移动图形位置     radius=[内径，外径]
    .set_global_opts(title_opts=opts.TitleOpts(title="用户感兴趣的领域",#标题
                                                  subtitle="以下是读者投票结果",#副标题
                                                  pos_left="center"),
                     legend_opts=opts.LegendOpts(#is_show=False,#去掉图例
                                                pos_left=0,
                                                orient="vertical",#图例垂直
                                                 ),
                     )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False,#是否显示标签
                                               ),#
                     )
    .render("result/bing.html")
)

"""

"""
# 图4-11
data=pd.read_excel("data/obama-approval-ratings.xls")
x=data["Issue"].values.tolist()
y1=data["Approve"].values.tolist()
y2=data["Disapprove"].values.tolist()
y3=data["None"].values.tolist()
print(y1)
bar=(
    Bar()
    .add_xaxis(x)
    .add_yaxis("Approve",y1,stack=True)
    .add_yaxis("Disapprove",y2,stack=True)
    .add_yaxis("None",y3,stack=True)
    .set_global_opts(title_opts=opts.TitleOpts("1","2"),
                     xaxis_opts=opts.AxisOpts(
                             axislabel_opts=opts.LabelOpts(rotate=30,font_size=9)),#设置大小与倾斜度
                     )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .render("result/4-11.html")
)
"""

"""
# 堆叠面积图
data=pd.read_excel("data/us-population-by-age.xls")
datax=data.iloc[ :, 0].apply(str).values.tolist()
print(datax)
y1=data["Under 5"].values.tolist()
y2=data["5 to 19"].values.tolist()
y3=data["20 to 44"].values.tolist()
y4=data["45 to 64"].values.tolist()
y5=data["65+"].values.tolist()
line=(
    Line(init_opts=opts.InitOpts(width="500px",height="500px")# 设置背景布大小
         )
    .add_xaxis(datax)
    .add_yaxis("Under 5",y1,stack=True,is_smooth=True,areastyle_opts=opts.AreaStyleOpts(opacity=0.5,color="red"))#stack是否堆叠is_smooth是否平滑，areastyle_opts区域设置
    .add_yaxis("5 to 19",y2,stack=True,is_smooth=True,areastyle_opts=opts.AreaStyleOpts(opacity=0.5,color="blue"))
    .add_yaxis("20 to 44",y3,stack=True,is_smooth=True,areastyle_opts=opts.AreaStyleOpts(opacity=0.5,color="green"))
    .add_yaxis("45 to 64",y4,stack=True,is_smooth=True,areastyle_opts=opts.AreaStyleOpts(opacity=0.5,color="yellow"))
    .add_yaxis("65+",y5,stack=True,is_smooth=True,areastyle_opts=opts.AreaStyleOpts(opacity=0.5,color="orange"))
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))#不显示标签

    .render("result/4-21.html")
)

"""


"""
# 散点图

crime = pd.read_csv("data/crimeRatesByState2005.csv")
(
    Scatter()
    .add_xaxis(crime["murder"])
    .add_yaxis("", crime["burglary"])
    .set_global_opts(
        title_opts=opts.TitleOpts(title="谋杀案和入室盗窃案的关联性散点图",pos_left="center"),
        xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True),name="谋杀案",name_location="middle",name_gap=30),
        yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True),name="入室盗窃案",name_location="center",name_gap=50),
        legend_opts=opts.LegendOpts(is_show=False)
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .render("result/5-2.html")
)
#matplotlib实现
crime = pd.read_csv("data/crimeRatesByState2005.csv")
crime=crime[crime.state!="United States"]
crime=crime[crime.state!="District of Columbia"]
plt.scatter(crime["murder"],crime["burglary"])
plt.show()

"""

"""
#散点图矩阵
crime = pd.read_csv("data/crimeRatesByState2005.csv")
crime=crime[crime.state!="United States"]
crime=crime[crime.state!="District of Columbia"]
crime=crime.drop(["population"],axis=1)
crime=crime.drop(["state"],axis=1)
g=sns.pairplot(crime,diag_kind="kde",kind='reg')#kde密度曲线reg拟合曲线
plt.show()
"""

"""
气泡图

"""
"""
#来源pyecharts官方文档
import json

from pyecharts import options as opts
from pyecharts.charts import Graph

with open("weibo.json", "r", encoding="utf-8") as f:
    j = json.load(f)
    nodes, links, categories, cont, mid, userl = j
c = (
    Graph()
    .add(
        "",
        nodes,
        links,
        categories,
        repulsion=50,
        linestyle_opts=opts.LineStyleOpts(curve=0.2),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        legend_opts=opts.LegendOpts(is_show=False),
        title_opts=opts.TitleOpts(title="Graph-微博转发关系图"),
    )
    .render("graph_weibo.html")
)

"""
"""
#图8-11
df=pd.read_csv("data/beijing_AQI_2018.csv")
attr=df['Date']
vl=df['AQI']
line = (
    Line()
    .add_xaxis(list(attr))
    .add_yaxis("AQI:",list(vl))
    .set_global_opts(title_opts=opts.TitleOpts(
            title="AQI全年走势图"
        ),

    )
    .set_series_opts(
        markpoint_opts=opts.MarkPointOpts(data=[
            opts.MarkPointItem(type_="max",),#显示最大值
            opts.MarkPointItem(type_="min",),#显示最小值
        ]),
        markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),#显示平均线
        areastyle_opts= opts.AreaStyleOpts(color="#000",opacity=0.3),
        label_opts=opts.LabelOpts(is_show=False)
    )
    .render("result/8_11.html")
)
"""

"""
# 图8-13
df=pd.read_csv("data/beijing_AQI_2018.csv")
dom=df[["Date","AQI"]]
list1=[]
for i in dom["Date"]:
    time=i.split('-')[1]
    list1.append(time)
df["month"]=list1
month_message=df.groupby(["month"])
monyh_com=month_message["AQI"].agg(["mean"])
monyh_com.reset_index(inplace=True)
monyh_com_last=monyh_com.sort_index()
attr=["{}".format(str( i )+"月") for i in range(1,13)]
vl=np.array(monyh_com_last["mean"])
vl=["{}".format(int(i)) for i in vl]
line = (
    Line()
    .add_xaxis(attr)
    .add_yaxis("AQI:",vl)
    .set_global_opts(title_opts=opts.TitleOpts(title="AQI月均全年走势图"),)
    .set_series_opts(
        markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max",),opts.MarkPointItem(type_="min",)]),)
    .render("result/8_13.html")
)
"""

"""
# 图8-15
df=pd.read_csv("data/beijing_AQI_2018.csv")
dom = df[['Date', 'AQI']]
data = [[], [], [], []]
dom1, dom2, dom3, dom4 = data
for i, j in zip(dom['Date'], dom['AQI']):
    time = i.split('-')[1]
    if time in ['01', '02', '03']:
        dom1.append(j)
    elif time in ['04', '05', '06']:
        dom2.append(j)
    elif time in ['07', '08', '09']:
        dom3.append(j)
    else:
        dom4.append(j)

boxplot = Boxplot()
boxplot = (
    boxplot.add_xaxis(['第一季度', '第二季度', '第三季度', '第四季度'])
    .add_yaxis("", boxplot.prepare_data([dom1, dom2, dom3, dom4]))
    .set_global_opts(title_opts=opts.TitleOpts(title='2018年北京季度AQI箱型图'),)
)
boxplot.render("result/8_15.html")

"""

"""
# 图8-17
df=pd.read_csv("data/beijing_AQI_2018.csv")
rank_message = df.groupby(['Quality_grade'])
rank_com = rank_message['Quality_grade'].agg(['count'])
rank_com.reset_index(inplace=True)
rank_com_last = rank_com.sort_values('count', ascending=False)

attr = rank_com_last['Quality_grade']
v1 = rank_com_last['count']

pie = (
    Pie()
    .add("空气质量", [list(z) for z in zip(attr, v1)], radius=[80, 180],
         tooltip_opts=opts.TooltipOpts(textstyle_opts=opts.TextStyleOpts(align='center'),
                                       formatter='{a}'+'<br/>'+'{b}: {c} ({d}%)'))
    .set_global_opts(title_opts=opts.TitleOpts(title='2018年北京全年空气质量情况', pos_left='center'),
                     legend_opts=opts.LegendOpts(orient='vertical', pos_top='5%', pos_left='2%'),
                    )
)
pie.render("result/8_17.html")
"""
