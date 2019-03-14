import scrapy


class PornPicsSpider(scrapy.Spider):
    name = "pornpics"

    def __init__(self, query, *args, **kwargs):
        # Normal init
        super(PornPicsSpider, self).__init__(*args, **kwargs)

        # Form the Query
        query = query.lower().replace(" ", "+") 
        print query

        # Set the start_urls
        self.start_urls = ['https://www.pornpics.com/?q=' + query]
        print self.start_urls

    def parse(self, response):
        gallaries = response.xpath('//ul[@id="tiles"]/li[@class="thumbwook "]/a/@href').getall()
        print gallaries

        for gallery in gallaries:
            download_gallary(gallary,gallaries.index(gallary))


    def download_gallary(url, number)
        # Go to the url
        # Find all the correct images
        # Create folder
        # Download each image to folder


