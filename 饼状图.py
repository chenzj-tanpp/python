from pyecharts.charts import Pie
import pandas as pd
from pyecharts import options as opts

pie = Pie()
vote = pd.read_csv("data/vote_result.csv")
# print(vote)
pie.add("感兴趣的领域",vote.values.tolist(), radius=['25%', '50%'])  # vote.values.tolist
#   radius设置是否是环形图
pie.set_global_opts(title_opts=opts.TitleOpts(
        title='饼图示例'
         )
)
pie.set_series_opts(
        tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        )
)
#指向add里的首个标签
pie.render("result/饼图.html")
