import scrapy
from scrapy.selector import Selector
from .. import items
class BrandInfoSpider(scrapy.Spider):
    name = "BrandInfo"
    start_urls=["http://www.tm.cn/search"]


    def parse_BrandInfo(self, response):
        sel = Selector(response)

        for detailHref in sel.xpath('//tbody//tr//@href').extract():
            if detailHref is not None:
                next_page = response.urljoin(detailHref)
                yield scrapy.Request(next_page, callback=self.parse_Detail())



    def parse_Detail(self, response):
        sel = Selector(response)
        item = items.RealTimeTime()
        tbodys = sel.xpath('//tbody')

        item['RegistrationNumber'] = tbodys[0].xpath('/tr[1]//td[last()]/text()').extract()
        item['Classification'] = tbodys[0].xpath('/tr[2]//td[last()]/text()').extract()
        item['ApplyDate'] = tbodys[0].xpath('/tr[3]//td[last()]/text()').extract()
        item['RegisterDate'] = tbodys[0].xpath('/tr[4]//td[last()]/text()').extract()

        yield item



