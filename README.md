#### you-need-Python@davidvivi

***
[![Build Status](https://img.shields.io/shippable/5444c5ecb904a4b21567b0ff.svg)](https://github.com/davidvivi/you-need-Python)
[![](https://img.shields.io/badge/language-Python-green.svg)](https://github.com/davidvivi/you-need-Python)

##### 下载安装
* 下载源码:

```python
git clone https://github.com/davidvivi/you-need-Python.git
或者直接到https://github.com/davidvivi/you-need-Python/tree/develop 下载zip文件
```
* 安装依赖:

```python
pip install -r requirements.txt
```


##### 1、Glory of Kings `王者荣耀各类英雄的出装小技巧`

* 运行环境Python 3.6:

```python
Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
```

* 依赖模块:

```python
from urllib.request import urlretrieve
import requests
import os
```

* 启动:

```python
# 如果你的依赖已经安全完成并且具备运行条件,可以直接在Glory of Kings下运行hero.py
# 到Glory of Kings目录下:
>>>python3 hero.py
```

##### 2、Lagou `Python拉钩数据采集与可视化`

* 注意项-wordcloud的安装:

```python
==== Installation of wordcloud package ====
download wordcloud‑1.3.2‑cp36‑cp36m‑win_amd64.whl from http://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud
Copy the file to your current working directory
Open command prompt from Tools
python -m pip install wordcloud-1.3.2-cp36-cp36m-win_amd64.whl
```

* 拉钩数据采集:

```python
# 如果你的依赖已经安全完成并且具备运行条件,可以直接在Lagou下运行lagou.py
>>>python3 hero.py
```
* 数据可视化:

```python
>>>python3 data_analysis.py
```


##### 3、scrapy_doubanmovie `scrapy学习爬取豆瓣电影`

* 注意项-scrapy的安装:

```python
==== Installation of scrapy package ====
利用whl文件安装，先安装Twisted再安装Scrapy
pip install Twisted-18.9.0-cp36-cp36m-win_amd64.whl
pip install Scrapy-1.5.1-py2.py3-none-any.whl
```