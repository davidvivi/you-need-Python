# -*- coding: utf-8 -*-

import os
import re
import pandas as pd  # 数据框操作
import matplotlib.pyplot as plt  # 绘图
import jieba  # 分词
from wordcloud import WordCloud  # 词云可视化
import matplotlib as mpl  # 配置字体
from pyecharts import Geo  # 地理图

mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 配置绘图风格
plt.rcParams["axes.labelsize"] = 16.
plt.rcParams["xtick.labelsize"] = 14.
plt.rcParams["ytick.labelsize"] = 14.
plt.rcParams["legend.fontsize"] = 12.
plt.rcParams["figure.figsize"] = [15., 15.]

# 导入数据
data = pd.read_csv(os.path.abspath(os.path.dirname(__file__)) + '\\csv\\lagoujob.csv', encoding='gbk')

# data['学历要求'].value_counts().plot(kind='barh',rot=0)
# data['工作经验'].value_counts().plot(kind='bar',rot=0,color='b')
# data['工作地点'].value_counts().plot(kind='pie', autopct='%1.2f%%')
# plt.show()

final = ''
stopwords = ['PYTHON', 'python', 'Python', '工程师', '（', '）', '/']  # 停止词
for n in range(data.shape[0]):

    seg_list = list(jieba.cut(data['招聘职位'][n]))

    for seg in seg_list:
        if seg not in stopwords:
            final = final + seg + ' '

# 指定可以显示中文的字体，否则不能显示中文
my_wordcloud = WordCloud(font_path=r'C:\Windows\Fonts\simkai.ttf', width=1000, height=600).generate(final)
plt.imshow(my_wordcloud)  # 显示图片

# 全球国家地图、中国省级地图、中国市级地图
# pip install echarts-countries-pypkg
# pip install echarts-china-provinces-pypkg
# pip install echarts-china-cities-pypkg

# 提取数据框,从lambda一直到*1000，是一个匿名函数，*1000的原因是这里显示的是几K几K的，我们把K切割掉，只要数字，就*1000了
data2 = list(map(lambda x: (data['工作地点'][x], eval(re.split('k|K', data['薪资'][x])[0]) * 1000), range(len(data))))
# 提取价格信息
data3 = pd.DataFrame(data2)
# 转化成Geo需要的格式，也是用匿名函数，在data5中，按照地区分组，然后根据地区来计算工资的平均值，将其变成序列后再分组
data4 = list(map(lambda x: (data3.groupby(0).mean()[1].index[x], data3.groupby(0).mean()[1].values[x]),
                 range(len(data3.groupby(0)))))
# 地理位置展示
geo = Geo("全国Python工资布局", "制作人:davidvivi", title_color="#fff", title_pos="center", width=1200, height=600,
          background_color='#404a59')
attr, value = geo.cast(data4)
geo.add("", attr, value, visual_range=[0, 300], maptype='china', type='heatmap', visual_text_color="#fff",
        symbol_size=15, is_visualmap=True)
geo.render("全国python工资分布图.html")
