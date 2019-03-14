import scrapy
from ppics.items import PpicsItem

class PornPicsSpider(scrapy.Spider):
    name       = "pornpics"

    def __init__(self, query, *args, **kwargs):
        super(PornPicsSpider, self).__init__(*args, **kwargs)

        query = query.lower().replace(" ", "+") 

        self.start_urls = ['https://www.pornpics.com/?q=' + query]

    def parse(self, response):
        gallery_urls = response.xpath('//ul[@id="tiles"]/li[@class="thumbwook "]/a/@href').getall()

        for url in gallery_urls:
            yield response.follow(url, self.parse_gallery)

        print self.image_urls


    def parse_gallery(self, response):
        item = PpicsItem()

        pics = response.xpath('//ul[@id="tiles"]/li[@class="thumbwook"]/a/@href').getall()

        item['image_urls'] = pics

        return item

# need smarter link extraction for external galleries (zishy, playboy, etc.)
