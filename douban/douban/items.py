# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass

	# 标题
	title = scrapy.Field()	
	# 信息
	bd = scrapy.Field()
	# 评分
	star = scrapy.Field()
	# 引用
	quote = scrapy.Field()
