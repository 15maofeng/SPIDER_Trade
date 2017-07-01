# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import Workbook

class DetailPipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(
            ['注册号', '国际分类', '申请日期', '注册日期', '申请人名称', '初审公告期号', '初审公告日期', '注册公告期号', '注册公告日期', '专用权期限', '商标类型', '是否共有商标',
             '备注', '代理人名称', '商品/服务', '类似群组', '商标流程'])

    def process_item(self, item, spider):
        #pipelines主要用于数据的进一步处理，比如类型转换、存储入数据库、写到本地等。
        #类型转换
        line = []
        for i in item:
            line.append(i)

        self.ws.append(line)
        self.wb.save('BrandInfo.xlsx')
        return item