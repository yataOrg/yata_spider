#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import scrapy, json, math, random, pymysql
from scrapy.http import FormRequest, HtmlResponse
from scrapy import Request
from decimal import *
from yataSpider.items import RestaurantItem


class RestaurantSpider(scrapy.Spider):
    name = 'Restaurant'
    allowed_domains = ['ele.me']
    food_url = 'https://www.ele.me/restapi/shopping/v2/menu?restaurant_id=%s&terminal=web'
    db = None
    cursor = None
    start_headers = {
        # ":authority": "www.ele.me",
        # ":method": "GET",
        # ":path": "/home/",
        # ":scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "referer": "https://www.ele.me/place",
        "upgrade-insecure-requests": '1',
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    }
    # 'accept': 'application/json, text/plain, */*'
    # 'referer': 'https://www.ele.me/shop/156427001',
    # 'x-shard': 'shopid=156427001;loc=121.52669,31.2302'

    def __init__(self):
        self.db = pymysql.connect(host="140.143.32.44", user="root", password="yata123", db="yata_data_01", port=3306, charset="utf8")
        self.cursor = self.db.cursor()


    def start_requests(self):
        return [
            FormRequest("https://www.ele.me/home/", headers=self.start_headers, meta={'cookiejar': 1},
                        callback=self.get_restaurants)
        ]

    def get_foods(self, response):
        print("start this spider!")
        self.get_restaurants()


    def get_restaurants(self, response):
        print("start spider!")
        sql = "select distinct ele_id from elm_new order by ele_id asc limit 2000"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        self.db.commit()
        self.db.close()
        if data is not None:
            self.start_headers['accept'] = 'application/json, text/plain, */*'
            for vv in data:
                self.start_headers['referer'] = 'https://www.ele.me/shop/%s' % vv
                self.start_headers['x-shard'] = "shopid=%s;loc=121.523862,31.219215" % vv
                yield FormRequest(
                    url= self.food_url % vv,
                    method= "GET",
                    meta={'cookiejar': response.meta['cookiejar'], 'restaurant_id': vv[0]},
                    headers=self.start_headers,
                    callback=self.export_data
                )


    def export_data(self, response):
        try:
            data = json.loads(response.body)
            if data is not None:
                for food_list in data:

                    for food in food_list['foods']:
                        item = RestaurantItem()
                        item['restaurant_id'] = response.meta['restaurant_id']
                        item['category_description'] = food_list['description']
                        item['food_description'] = food['description']
                        item['ele_food_id'] = food['specfoods'][0]['food_id']
                        if 'false' == food['is_essential']: is_essential = 0
                        else: is_essential = 1
                        item['is_essential'] = is_essential
                        item['is_featured'] = food['is_featured']
                        item['min_purchase'] = food['min_purchase']
                        item['month_sales'] = food['month_sales']
                        item['name'] = food['name']
                        item['rating'] = food['rating']
                        item['rating_count'] = food['rating_count']
                        item['satisfy_count'] = food['satisfy_count']
                        item['satisfy_rate'] = food['satisfy_rate']
                        item['category_name'] = food_list['name']
                        item['packing_fee'] = food['specfoods'][0]['packing_fee']  # 餐盒费
                        item['price'] = food['specfoods'][0]['price']
                        yield item
                        print("inserted one ++")

        except Exception as e:
            print(e)
