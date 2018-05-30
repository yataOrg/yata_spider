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




class RestaurantItem(scrapy.Item):

    restaurant_id = scrapy.Field()
    category_description = scrapy.Field()
    food_description = scrapy.Field()
    ele_food_id = scrapy.Field()
    is_essential = scrapy.Field()
    is_featured = scrapy.Field()
    min_purchase = scrapy.Field()
    month_sales = scrapy.Field()
    name = scrapy.Field()
    rating = scrapy.Field()
    rating_count = scrapy.Field()
    satisfy_count = scrapy.Field()
    satisfy_rate = scrapy.Field()
    category_name = scrapy.Field()
    packing_fee = scrapy.Field()
    price = scrapy.Field()

    def get_insert_sql(self):
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        insert_sql = """
                   insert into restaurant_foods(restaurant_id, 
                   category_description, 
                   food_description, 
                   ele_food_id,
                   is_essential,
                   is_featured,
                   min_purchase,
                   month_sales,
                   name,
                   rating,
                   rating_count,
                   satisfy_count,
                   satisfy_rate,
                   category_name,
                   packing_fee,
                   price,
                   created_at, updated_at)
                    VALUES (%d, '%s', '%s', %d, %d, %d, %d, %d, '%s', %f, %d, %d, %d, '%s', %f, %f, '%s', '%s');
               """
        params = (
        self["restaurant_id"], self["category_description"], self["food_description"], self["ele_food_id"], self["is_essential"], self["is_featured"],
            self["min_purchase"], self["month_sales"], self["name"], self["rating"], self["rating_count"], self["satisfy_count"], self["satisfy_rate"],
            self["category_name"], self["packing_fee"], self['price'], now_time, now_time
        )
        print("target insert one row data" + '**' * 6)
        return insert_sql, params


class FoodCommentItem(scrapy.Item):

    restaurant_id = scrapy.Field()
    ele_food_id = scrapy.Field()
    rate_name = scrapy.Field()
    rating_star = scrapy.Field()
    rating_text = scrapy.Field()
    reply_at = scrapy.Field()
    reply_text = scrapy.Field()
    rated_at = scrapy.Field()
    time_spent_desc = scrapy.Field()
    username = scrapy.Field()
    my_code = scrapy.Field()

    def get_insert_sql(self):
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print(now_time)
        insert_sql = """
                   insert into foods_comment(restaurant_id, 
                   ele_food_id, 
                   rate_name, 
                   rating_star,
                   rating_text,
                   reply_at,
                   reply_text,
                   rated_at,
                   time_spent_desc,
                   username,
                   my_code,
                   created_at,
                   updated_at) 
                   VALUES (%d, %d, '%s', %d, '%s', '%s', '%s', '%s', '%s', "%s", '%s', '%s', '%s');"""
        params = (
        self["restaurant_id"], self["ele_food_id"], self["rate_name"], self["rating_star"], self["rating_text"], self["reply_at"],
            self["reply_text"], self["rated_at"], self["time_spent_desc"], self["username"], self["my_code"], now_time, now_time
        )
        print("target insert one row data" + '**' * 6)
        # print(insert_sql % params)
        return insert_sql, params