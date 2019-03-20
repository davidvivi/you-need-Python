# -*- coding: utf-8 -*-

from scrapy import cmdline

"""
scrapy crawl -h查看帮助
Feed exports 链接介绍:https://docs.scrapy.org/en/latest/topics/feed-exports.html
后缀支持('json', 'jsonlines', 'jl', 'csv', 'xml', 'marshal', 'pickle')
1、 FEED_EXPORT_ENCODING 修改json的编码方式，不加这一句会默认使用unicode编码。
    或者在setting.py加上FEED_EXPORT_ENCODING = 'utf-8'
"""
cmdline.execute('scrapy crawl douban_spider -o test.json -s FEED_EXPORT_ENCODING=UTF-8'.split())
# cmdline.execute('scrapy crawl douban_spider -o test.jsonlines -s FEED_EXPORT_ENCODING=UTF-8'.split())
# cmdline.execute('scrapy crawl douban_spider -o test.csv'.split())
# cmdline.execute('scrapy crawl douban_spider -o test.xml'.split())
# cmdline.execute('scrapy crawl douban_spider -o test.marshal'.split())
# cmdline.execute('scrapy crawl douban_spider -o test.pickle'.split())
