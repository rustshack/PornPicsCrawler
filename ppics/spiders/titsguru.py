# -*- coding: utf-8 -*-
import scrapy
from ppics.items import PpicsItem

class TitsguruSpider(scrapy.Spider):
    name = 'titsguru'

    def __init__(self, crawl_type, *args, **kwargs):
        super(TitsguruSpider, self).__init__(*args, **kwargs)

        if crawl_type == "b":
            self.start_urls.append('https://tits-guru.com/thebest')

        elif crawl_type == "n":
            self.start_urls.append('https://tits-guru.com')

        else:
            self.start_urls.append('https://tits-guru.com/boobs-model' + crawl_type)

    def parse(self, response):

        # Get items
        item = PpicsItem()
        item['image_urls'] = response.xpath('//meta[@itemprop="contentUrl"]/./@content').getall()
        yield item

        # Go to next page
        next_page = response.xpath('//div[@class="paginator-block"]//a[@aria-label="Next"]/./@href').get()

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request( next_page, callback=self.parse)

# images - response.xpath('//meta[@itemprop="contentUrl"]/./@content').getall()
# pagination - response.xpath('//div[@class="paginator-block"]//a[@aria-label="Next"]/./@href').get()

