# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import Workbook

class RealTimePipeline(object):
    def process_item(self, item, spider):
        pass


class DetailPipeline(object):
    wb = Workbook()
    ws = wb.active
    ws.append(['注册号','国际分类','申请日期','注册日期','申请人名称','初审公告期号','初审公告日期','注册公告期号','注册公告日期','专用权期限','商标类型','是否共有商标','备注','代理人名称','商品/服务','类似群组','商标流程'])

    def process_item(self, item, spider):
        line = [item['RegistrationNumber'],item['Classification'], item['ApplyDate'], item['RegisterDate']]
        self.ws.append(line)
        self.ws.save('../BrandInfo.xlsx')
        return item