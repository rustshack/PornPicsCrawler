# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PpicsItem(scrapy.Item):
    image_urls = scrapy.Field()
    image = scrapy.Field()
    model_name = scrapy.Field()
    gallery_name = scrapy.Field()
