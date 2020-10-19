from pyecharts.charts import Pie
from pyecharts import options as opts

# 构建数据
x_data = ["直接访问","营销推广","博客推广","搜索引擎"]
y_data = [880,214,300,1100]

# 为Pie设置指定格式
data_pie = [list(i) for i in zip(x_data,y_data)]

# 定义一个pie的函数
def pie_charts() -> Pie:
    # 创建实例对象
    pie = Pie(init_opts=opts.InitOpts(width='1000px',height='600px'))
    # 添加数据
    pie.add(series_name="访问来源",data_pair=data_pie)
    # 设置全局项
    pie.set_global_opts(title_opts=opts.TitleOpts(title="课程不同的来源销售分析",pos_left='center',pos_top=20))
    #设置每项数据占比
    pie.set_series_opts(tooltip_opts=opts.TooltipOpts(trigger='item',formatter="{a} <br/> {b}:{c} ({d}%)"))

    return pie

pie = pie_charts()
pie.render("result/pie_charts.html")