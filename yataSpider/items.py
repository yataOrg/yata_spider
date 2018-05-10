# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YataspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    address = scrapy.Field()
    float_delivery_fee = scrapy.Field()
    float_minimum_order_amount = scrapy.Field()
    cuisine = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    name = scrapy.Field()
    opening_hours1 = scrapy.Field()
    opening_hours2 = scrapy.Field()
    opening_hours3 = scrapy.Field()
    phone1 = scrapy.Field()
    phone2 = scrapy.Field()
    rating = scrapy.Field()
    order_lead_time = scrapy.Field()
    recommend_reasons = scrapy.Field()