# -*- coding: utf-8 -*-
import scrapy

# 通过scrapy genspider douban_spider movie.douban.com生成的
class DoubanSpiderSpider(scrapy.Spider):
    # 爬虫名字
    name = 'douban_spider'
    # 允许的域名
    allowed_domains = ['movie.douban.com']
    # 入口URL，扔到调度器里面
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        print('response.text')
