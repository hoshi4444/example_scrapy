import scrapy
import logging
from example_scrapy.items import ModelData
import re


logger = logging.getLogger('pachi_log')
fh = logging.FileHandler('pachi_log.log')
logger.addHandler(fh)
sh = logging.StreamHandler()
logger.addHandler(sh)


class PachiModelSpiderSpider(scrapy.Spider):
    name = 'pachi_model_spider'
    allowed_domains = ['pachiseven.jp']
    num = 4400
    start_urls = [f'https://pachiseven.jp/machines/{num}']

    def parse(self, response):
        try:
            yield ModelData(
                name = response.css('h1 span::text').get(),
                spec = response.xpath('string(//*[@id="mpanel2"]//*[@class="toggle_contents"][1]//table[text()])').get().split(),
            )
        except Exception as e:
            logger.exception(f'error!: {e}')

        while self.num < 6191:
            try:
                logger.info('next')
                self.num += 1
                yield scrapy.Request(f'https://pachiseven.jp/machines/{self.num}', callback=self.parse)
            except Exception as e:
                logger.exception(f'error!: {e}')
                break
        else:
            logger.info(f'end num:{self.num}')
            return