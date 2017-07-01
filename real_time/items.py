# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BrandItem(scrapy.Item):
    # define the Fields for your item here like:
    # name = scrapy.Field()
    TrademarkName = scrapy.Field() #商标名
    #tbody 1
    RegistrationNumber = scrapy.Field() #注册号
    Classification = scrapy.Field() #国际分类
    ApplyDate = scrapy.Field() #申请日期
    RegisterDate = scrapy.Field() #注册日期

    TrademarkPic = scrapy.Field() #商标图片
    #tbody2
    ApplicantName = scrapy.Field() #申请人名称
    ApplicantAddress = scrapy.Field() #申请人地址
    #tbody 3
    PreliminaryNoticeNo = scrapy.Field() #初审公告期号
    PreliminaryNoticeDate = scrapy.Field() #初审公告日期
    RegisterNoticeNo = scrapy.Field() #注册公告期号
    RegisterNoticeDate = scrapy.Field() #注册公告日期
    ExclusiveRightTime = scrapy.Field() #专用权期限
    Type = scrapy.Field() #商标类型
    TogetherTrademark = scrapy.Field() #是否共有商标
    Remark = scrapy.Field() #备注
    #tbody 4
    AgentName = scrapy.Field() #代理人名称
    #tbody 5
    Service = scrapy.Field() #商品/服务
    SimilarGroups = scrapy.Field() #类似群组
    #tbody 6
    Process = scrapy.Field() #商标流程