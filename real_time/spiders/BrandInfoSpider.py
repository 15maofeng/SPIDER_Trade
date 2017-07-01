import scrapy
from scrapy.selector import Selector
from .. import items
from openpyxl import Workbook
from scrapy import log
class BrandInfoSpider(scrapy.Spider):
    name = "BrandInfo"

    def __init__(self, value=None, searchType=None):
        super(BrandInfoSpider, self).__init__()
        self.start_urls = ['http://www.tm.cn/search?value=%s&searchType=%s' %(value, searchType)]

    def parse(self, response):
        for detailHref in response.xpath('//tbody//tr//@href'):
            keyAndValue = detailHref.extract()
            if keyAndValue is not None:
                next_page = 'http://www.tm.cn'+keyAndValue
                yield scrapy.Request(next_page, callback=self.parse_Detail)


    def parse_Detail(self, response):
        item = items.RealTimeItem()
        tbodys = response.xpath('//tbody')

        sel = Selector(text=tbodys[0].extract())

        #list type
        item['RegistrationNumber'] = sel.xpath('//tr[1]//td[last()]/text()').extract()
        item['Classification'] = sel.xpath('//tr[2]//td[last()]/text()').extract()
        item['ApplyDate'] = sel.xpath('//tr[3]//td[last()]/text()').extract()
        item['RegisterDate'] = sel.xpath('//tr[4]//td[last()]/text()').extract()

        file = open('temp.txt','wb')
        with file as fp:
            if len(item['RegistrationNumber']) != 0:
                fp.write(item['RegistrationNumber'][0])

        yield item



