# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy, time


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
    distance = scrapy.Field()
    ele_distance = scrapy.Field()
    ele_id = scrapy.Field()
    ele_authentic_id = scrapy.Field()
    search_jwd = scrapy.Field()



    def get_insert_sql(self):
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        insert_sql = """
                   insert into elm_new(address, float_delivery_fee, float_minimum_order_amount, cuisine,latitude, longitude, name, opening_hours1, 
                   opening_hours2, opening_hours3, phone1, phone2, rating, order_lead_time, recommend_reasons, distance, ele_distance, ele_id, ele_authentic_id, search_jwd, created_at, updated_at)
                   VALUES ('%s', %f, %f, '%s', %f, %f, '%s', '%s', '%s', '%s', '%s', '%s', %f, '%s', '%s', %f, %f, %d, %d, '%s', '%s', '%s');
               """
        params = (
        self["address"], self["float_delivery_fee"], self["float_minimum_order_amount"], self["cuisine"], self["latitude"], self["longitude"],
            self["name"], self["opening_hours1"], self["opening_hours2"], self["opening_hours3"], self["phone1"], self["phone2"], self["rating"],
            self["order_lead_time"], self["recommend_reasons"], self['distance'], self['ele_distance'], self['ele_id'], self['ele_authentic_id'], self['search_jwd'], now_time, now_time
        )
        print("insert data ***" * 6)
        return insert_sql, params



class NelmItem(scrapy.Item):

    address = scrapy.Field()
    description = scrapy.Field()
    flavors = scrapy.Field()
    float_delivery_fee = scrapy.Field()

    float_minimum_order_amount = scrapy.Field()
    ele_id = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    name = scrapy.Field()
    opening_hours1 = scrapy.Field()
    opening_hours2 = scrapy.Field()
    opening_hours3 = scrapy.Field()
    order_lead_time = scrapy.Field()
    phone1 = scrapy.Field()
    phone2 = scrapy.Field()
    promotion_info = scrapy.Field()
    rating = scrapy.Field()
    rating_count = scrapy.Field()
    recent_order_num = scrapy.Field()
    recommend_reasons = scrapy.Field()
    supports = scrapy.Field()
    city = scrapy.Field()


    def get_insert_sql(self):
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        insert_sql = """
                   insert into elm_restaurant(address, 
                   description, 
                   flavors, 
                   float_delivery_fee, 
                   float_minimum_order_amount, 
                   ele_id, 
                   latitude, 
                   longitude, 
                   name, 
                   opening_hours1, opening_hours2, opening_hours3,
                   order_lead_time,
                   phone1, phone2,
                   promotion_info,
                   rating,
                   rating_count,
                   recent_order_num,
                   recommend_reasons,
                   supports,
                   city,
                   created_at, updated_at)
                    VALUES ('%s', '%s', '%s', %f, %f, %d, %f, %f, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %f, %d, %d, '%s', '%s', %d, '%s', '%s');
               """
        params = (
        self["address"], self["description"], self["flavors"], self["float_delivery_fee"], self["float_minimum_order_amount"], self["ele_id"],
            self["latitude"], self["longitude"], self["name"], self["opening_hours1"], self["opening_hours2"], self["opening_hours3"], self["order_lead_time"],
            self["phone1"], self["phone2"], self['promotion_info'], self['rating'], self['rating_count'], self['recent_order_num'], self['recommend_reasons'], self['supports'], self['city'], now_time, now_time
        )
        print("@@@@@@@@@@@@@@@@@@@>>>>>>" * 6)
        return insert_sql, params