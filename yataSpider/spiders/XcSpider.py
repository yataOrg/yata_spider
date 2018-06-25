#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import scrapy, json, math, time
from scrapy.http import FormRequest, HtmlResponse
from urllib.parse import urlencode
from scrapy import Request
from decimal import *
from yataSpider.items import YataspiderItem

class XcSpider(scrapy.Spider):

    name = "XcSpider"
    allowed_domains = ["m.ctrip.com", "hotels.ctrip.com"]
    search_url = 'http://m.ctrip.com/restapi/h5api/searchapp/search?'
    search_dict = {
        'action': 'autocomplete',
        'source': 'globalonline',
        'keyword': u'上海',
        't': '1529929807965'
    }
    search_header = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Host': 'm.ctrip.com',
        'Origin': 'http://www.ctrip.com',
        'Pragma': 'no-cache',
        'Referer': 'http://www.ctrip.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    }

    data_cookies = {
        '_RGUID': '1602ab31-5c24-491f-a572-e09684abaebc',
        '_RSG': 'Va49S5pg2O1ywwg4Q9uoLA',
        '_RDG': '2879421ee4a8e1233a350e00219d4c609b',
        '_bfi': 'p1%3D102003%26p2%3D0%26v1%3D1%26v2%3D0'
    }

    def start_requests(self):
        return [
            Request(self.search_url + urlencode(self.search_dict), method='GET', headers = self.search_header, meta={'cookiejar': 1}, callback=self.get_list)
        ]


    def get_list(self, response):

        data_list = json.loads(response.body)
        if data_list is not None:
            for k_index, item_data in enumerate(data_list['data']):
                if k_index > 3:
                    print(item_data['url'])
                    print('@@@@@@@'*10)
                    yield Request(item_data['url'], method='GET', headers = self.search_header, cookies=self.data_cookies, callback=self.get_data)
                    break

    def get_data(self, response):
        print('ssssssssssssssssssssssssssssssssssssssssssssssssssssssss'*10)
        print(response.body)