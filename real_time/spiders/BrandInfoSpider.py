import scrapy
from scrapy.selector import Selector
from .. import items
class BrandInfoSpider(scrapy.Spider):
    name = "BrandInfo"
    start_urls=["http://www.tm.cn/search"]


    def parse(self, response):
        #collect 'brand_urls'
        for detailHref in response.xpath('//tbody//tr//@href'):
            keyAndValue = detailHref.extract()
            if keyAndValue is not None:
                next_page = response.urljoin(keyAndValue)
                yield scrapy.Request(next_page, callback=self.parse_Detail)




    def parse_Detail(self, response):
        item = items.RealTimeTime()
        tbodys = response.xpath('//tbody')

        sel = Selector(text=tbodys[0].extract())

        #list type
        item['RegistrationNumber'] = sel.xpath('//tr[1]//td[last()]/text()').extract()
        item['Classification'] = sel.xpath('//tr[2]//td[last()]/text()').extract()
        item['ApplyDate'] = sel.xpath('//tr[3]//td[last()]/text()').extract()
        item['RegisterDate'] = sel.xpath('//tr[4]//td[last()]/text()').extract()

        yield item



