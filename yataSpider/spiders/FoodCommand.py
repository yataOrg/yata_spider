#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import scrapy, json, math, random, pymysql
from scrapy.http import FormRequest, HtmlResponse
from scrapy import Request
from decimal import *
from yataSpider.items import FoodCommentItem


class FoodCommentSpider(scrapy.Spider):
    name = 'FoodComment'
    allowed_domains = ['ele.me']

    food_comment_url = 'https://www.ele.me/restapi/ugc/v1/restaurant/%d/ratings?limit=100&offset=0&record_type=1'
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
                        callback=self.get_food_comment)
        ]

    def get_food_comment(self, response):
        print("start spider!")
        sql = "select distinct ele_id from elm_new order by ele_id asc limit 20000"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        self.db.commit()
        self.db.close()
        if data is not None:
            self.start_headers['accept'] = 'application/json, text/plain, */*'
            for vv in data:
                self.start_headers['referer'] = 'https://www.ele.me/shop/%s/rate' % vv
                self.start_headers['x-shard'] = "shopid=%s;loc=121.52669,31.2302" % vv
                yield FormRequest(
                    url= self.food_comment_url % vv,
                    method= "GET",
                    meta={'cookiejar': response.meta['cookiejar'], 'restaurant_id': vv[0]},
                    headers=self.start_headers,
                    callback=self.export_data
                )
                return

    def next_page(self, response, url, restaurant_id):
        self.start_headers['referer'] = 'https://www.ele.me/shop/%s/rate' % restaurant_id
        self.start_headers['x-shard'] = "shopid=%s;loc=121.52669,31.2302" % restaurant_id
        FormRequest(
            url=url,
            method="GET",
            meta={'cookiejar': response.meta['cookiejar'], 'restaurant_id': restaurant_id},
            headers=self.start_headers,
            callback=self.export_data
        )


    def export_data(self, response):
        print('make page_offset')
        tem = response.url.split("=", 2)
        tem1 = tem[2].split('&')[0]
        page_offset = int(tem1) + 100


        try:
            data = json.loads(response.body)
            if data is not None and data != []:
                for comment_list in data:

                    for comment in comment_list['item_rating_list']:
                        item = FoodCommentItem()
                        item['restaurant_id'] = response.meta['restaurant_id']
                        item['ele_food_id'] = comment['food_id']
                        item['rate_name'] = comment['rate_name']
                        item['rating_star'] = comment['rating_star']
                        item['rating_text'] = comment['rating_text']
                        item['reply_at'] = comment['reply_at']
                        item['reply_text'] = comment['reply_text']
                        item['rated_at'] = comment_list['rated_at']
                        item['time_spent_desc'] = comment_list['time_spent_desc']
                        item['username'] = comment_list['username']

                        yield item
                        print("inserted one ++")

                yield self.next_page(response, 'https://www.ele.me/restapi/ugc/v1/restaurant/%d/ratings?limit=100&offset=' + str(page_offset) + '&record_type=1', response.meta['restaurant_id'])

        except Exception as e:
            print(e)
