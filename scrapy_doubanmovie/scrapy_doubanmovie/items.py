# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDoubanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    sequence = scrapy.Field()
    title = scrapy.Field()  # 电影名字
    introduce = scrapy.Field()  # 电影介绍
    star = scrapy.Field()  # 电影星级
    evaluate = scrapy.Field()  # 电影评价人数
    quote = scrapy.Field()  # 电影中脍炙人口的一句话
