# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy_doubanmovie.scrapy_doubanmovie.items import ScrapyDoubanmovieItem
from urllib.parse import urljoin

# 通过scrapy genspider douban_spider movie.douban.com生成的
class DoubanSpiderSpider(scrapy.Spider):
    # 爬虫名字
    name = 'douban_spider'
    # 允许的域名
    allowed_domains = ['movie.douban.com']
    # 入口URL，扔到调度器里面
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        item = ScrapyDoubanmovieItem()
        selector = Selector(response)
        Movies = selector.xpath('//div[@class="info"]')
        for eachMovie in Movies:
            title = eachMovie.xpath('div[@class="hd"]/a/span/text()').extract()  # 多个span标签
            fullTitle = "".join(title)  # 将多个字符串无缝连接起来
            introduce = eachMovie.xpath('div[@class="bd"]/p/text()').extract()
            star = eachMovie.xpath('div[@class="bd"]/div[@class="star"]/span/text()').extract()[0]
            evaluate = eachMovie.xpath('div[@class="bd"]/div[@class="star"]/span/text()').extract()[1]
            quote = eachMovie.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            # quote可能为空，因此需要先进行判断
            if quote:
                quote = quote[0]
            else:
                quote = ''
            item['title'] = fullTitle
            item['introduce'] = ';'.join([x.strip() for x in introduce if x.strip() != ''])
            item['star'] = star
            item['evaluate'] = evaluate
            item['quote'] = quote
            yield item
        nextLink = selector.xpath('//span[@class="next"]/link/@href').extract()
        # 第10页是最后一页，没有下一页的链接
        if nextLink:
            nextLink = nextLink[0]
            yield Request(urljoin(response.url, nextLink), callback=self.parse)
