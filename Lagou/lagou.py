# -*- coding: utf-8 -*-

import requests  # 网络请求
import re
import os
import pandas as pd  # 数据框操作
# import numpy as np
# import matplotlib.pyplot as plt  # 绘图
# import matplotlib as mpl  # 配置字体
# from pyecharts import Geo  # 地理图
import time  # 增加延时
import random

# post的网址
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

header = {'Accept': 'application/json, text/javascript, */*; q=0.01',
          'Accept-Encoding': 'gzip, deflate, br',
          'Accept-Language': 'zh-CN,zh;q=0.9',
          'Connection': 'keep-alive',
          'Content-Length': '25',
          'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'Cookie': '_ga=GA1.2.888264978.1526124456; user_trace_token=20180512192736-78cc78dc-55d7-11e8-8229-5254005c3644; LGUID=20180512192736-78cc7ce4-55d7-11e8-8229-5254005c3644; LG_LOGIN_USER_ID=0a39df7d4b722c60a44c3d78ae6d162c000c476b0cbd4789; JSESSIONID=ABAAABAAADEAAFI73F945FD2DF58C040E2D5FA97B9F2036; _gid=GA1.2.2122724175.1528814515; LGSID=20180612224200-c36d2919-6e4e-11e8-9b2c-525400f775ce; index_location_city=%E5%8C%97%E4%BA%AC; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1526902554,1527498533,1528814517,1528814855; TG-TRACK-CODE=search_code; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1528817650; LGRID=20180612233411-0df13db0-6e56-11e8-947a-5254005c3644; SEARCH_ID=2ce15384d664427a9d76c5577cbe84e4',
          'Host': 'www.lagou.com',
          'Origin': 'https://www.lagou.com',
          'Referer': 'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
          'X-Anit-Forge-Code': '0',
          'X-Anit-Forge-Token': None,
          'X-Requested-With': 'XMLHttpRequest'}

for n in range(1, 31):
    # 要提交的数据,kd是查询关键词，pn是页数
    form_data = {'first': 'false',
                 'kd': 'Python',
                 'pn': str(n)}
    time.sleep(random.randint(2, 5))
    # 提交数据
    html = requests.post(url, data=form_data, headers=header)
    # 提取数据
    data = re.findall('{"companyId":.*?,"workYear":"(.*?)","education":"(.*?)","city":"(.*?)","positionName":"(.*?)","companyLogo":".*?","companyShortName":"(.*?)","positionLables":.*?,"industryLables":.*?,"businessZones":.*?,"score":.*?,"approve":.*?,"jobNature":".*?","companyLabelList":(.*?),"publisherId":.*?,"district":"(.*?)","companySize":".*?","createTime":".*?","positionAdvantage":".*?","salary":"(.*?)"}',html.text)
    data_frame = pd.DataFrame(data)
    data_frame.to_csv(os.path.abspath(os.path.dirname(__file__)) + '\\csv\\lagoujob.csv', header=False, index=False,
                      mode='a+')
