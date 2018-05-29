#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import scrapy, json, math, random, pymysql
from scrapy.http import FormRequest, HtmlResponse
from scrapy import Request
from decimal import *
from yataSpider.items import NelmItem


class RestaurantSpider(scrapy.Spider):
    name = 'Restaurant'
    allowed_domains = ['ele.me']

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
        self.db = pymysql.connect(host="localhost", user="root", password="", db="yata_data_01", port=3306, charset="utf8")
        self.cursor = self.db.cursor()


    def start_requests(self):
        return [
            FormRequest("https://www.ele.me/home/", headers=self.start_headers, meta={'cookiejar': 1},
                        callback=self.get_foods)
        ]

    def get_foods(self, response):
        print("start this spider!")
        self.get_restaurants()


    def get_restaurants(self):
        sql = "select distinct ele_id,address  from elm_new order by ele_id asc limit 2000"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        self.db.commit()
        self.db.close()
        if data is not None:
            for vv in data:
                print(vv)
                return


