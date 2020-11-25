import scrapy


class PachiDataSpiderSpider(scrapy.Spider):
    name = 'pachi_data_spider'
    allowed_domains = ['daidata.goraggio.com']
    start_urls = ['http://daidata.goraggio.com/']

    def parse(self, response):
        pass
