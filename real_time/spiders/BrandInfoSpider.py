import scrapy
from scrapy.selector import Selector
from .. import items

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
                yield scrapy.Request(next_page, callback=self.parse_Content)


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


    def parse_Content(self, response):
        select = Selector(text=response.text)

        #todo 将字符串对应存进BrandItem中
        item = items.BrandItem()

        div_list = select.xpath(
            "//div[@class='container']/div[@class='info_table_box info_box']/div[@class='zxzc_tit']")
        for div in div_list:
            div_string_list = div.xpath("string(.)").extract()
            div_string = "".join(div_string_list)
            div_string = div_string.strip()
            print div_string

        tr_list = select.xpath(
            "//div[@class='container']/div[@class='info_table_box info_box']/div[@class='sort_sec clearfix']/div[@class='w_515 sort_sec_table']/table/tbody/tr/td[@class='c_blue']")
        # base_dict = {}
        i = 0
        for tr in tr_list:
            i = i + 1
            tr_string_list = tr.xpath("string(.)").extract()
            tr_string = "".join(tr_string_list)
            tr_string = tr_string.strip()
            # print i
            if not tr_string:
                tr_string = "Null"
            if i == 1:
                registernumber = tr_string
            elif i == 2:
                classification = tr_string
            elif i == 3:
                applydate = tr_string
            else:
                register = tr_string

        img_list = select.xpath(
            "//div[@class='container']/div[@class='info_table_box info_box']/div[@class='sort_sec clearfix']/div[@class='carte_box']/img/@src")
        # img_list = select.xpath('//img/@src')
        for img in img_list:
            img_string = str(img)
            imgstr = img_string.split("u'")
            trademarkpic = "http://www.tm.cn" + imgstr[1].strip("'>")
            print trademarkpic

        t_list = select.xpath(
            "//div[@class='container']/div[@class='info_table_box info_box']/div[@class='sort_sec sort_sec_table']/table[@width='100%']/tbody/tr/td[@class='c_blue']")
        for t in t_list:
            i = i + 1
            t_string_list = t.xpath("string(.)").extract()
            t_string = "".join(t_string_list)
            t_string = t_string.strip("\t").lstrip("\t").rstrip("\t")
            # print i
            if not t_string:
                t_string = "Null"
            if i == 5:
                applicantname = t_string
            elif i == 6:
                applicantaddress = t_string
            elif i == 7:
                preliminarynoticeno = t_string
            elif i == 8:
                preliminarynoticedate = t_string
            elif i == 9:
                registernoticeno = t_string
            elif i == 10:
                registernoticedate = t_string
            elif i == 11:
                exclusiverighttime = t_string
            elif i == 12:
                typ = t_string
            elif i == 13:
                togethertrademark = t_string
            elif i == 14:
                remark = t_string
            elif i == 15:
                agentname = t_string
            elif i == 16:
                service = t_string
            elif i == 17:
                similargroups = t_string
            elif i == 18:
                process = t_string.split()
            else:
                processtime = t_string.split()




