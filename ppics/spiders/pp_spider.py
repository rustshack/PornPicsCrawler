import scrapy
import json
from ppics.items import PpicsItem

class PornPicsSpider(scrapy.Spider):
    name       = "pornpics"
    search_list = list() # list of models for which to crawl
    current_model = 0    # current model index
    item = PpicsItem()   # item we'll return to the item pipeline

    def __init__(self, path, *args, **kwargs):
        super(PornPicsSpider, self).__init__(*args, **kwargs)

        # Load Search List
        with open(path, "r") as json_file:
             data = json.load(json_file)
             
             for element in data["queries"]:
                 self.search_list.append(element)

        # Generate a starting URL for each query in the search list
        for query in self.search_list:
            query = query.lower().replace(" ", "+") 
            self.start_urls.append('https://www.pornpics.com/?q=' + query)

    def parse(self, response):
        # Set model name in PpicsItem
        print "Parse current model" + str(self.current_model)

        self.item["model_name"] = self.search_list[ self.current_model]

        gallery_urls = response.xpath(
                '//ul[@id="tiles"]/li[@class="thumbwook "]/a/@href').getall()

        gallery_titles = response.xpath(
                '//ul[@id="tiles"]/li[@class="thumbwook "]/a/@title').getall()

        for i, url in enumerate(gallery_urls):
            yield response.follow( url, self.parse_gallery)

        self.current_model += 1

    def parse_gallery(self, response):
        # print "Parse Gallery current model" + str(self.current_model)
        # initialize the PpicsItem with model name
        m = self.item["model_name"]
        print "Crawling:" + m

        # Get image links
        pics = response.xpath(
                '//ul[@id="tiles"]/li[@class="thumbwook"]/a/@href').getall()

        # Send to image pipeline
        self.item['image_urls'] = pics

        return self.item

# need smarter link extraction for external galleries (zishy, playboy, etc.)
