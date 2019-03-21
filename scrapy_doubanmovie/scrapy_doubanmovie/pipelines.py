# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from . import settings


class ScrapyDoubanmoviePipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            password=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                """
                    insert into doubantop250(title,introduce,star,evaluate,quote) value (%s,%s,%s,%s,%s)
                """, (
                    item['title'],
                    item['introduce'],
                    item['star'],
                    item['evaluate'],
                    item['quote']
                )
            )
            self.connect.commit()
        except Exception as e:
            print("错误信息为：" + str(e))
        return item
