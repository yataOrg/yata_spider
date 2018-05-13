#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import scrapy, json, math
from scrapy.http import FormRequest, HtmlResponse
from scrapy import Request
from decimal import *
from yataSpider.items import NelmItem


class NelmSpider(scrapy.Spider):
    name = "NelmSpider"
    allowed_domains = ["ele.me"]
    start_urls = ["https://www.ele.me/home/"]

    shop_headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        # "referer": "https://www.ele.me/shop/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
        "x-shard": "shopid=56;loc=121.529169,31.221809",
    }

    api_cookies = {
        "ubt_ssid": "qc6hy19lrtojld9veblqwbn55qqaotwo_2018-05-10",
        "_utrace": "40056258e5b7c860e863076b79003b5d_2018-05-10",
        "eleme__ele_me": "ff20a4ab936ba5aea3874dbd40f9645f%3Ada61055c4a57ed7537d4908e3cf7883546321650",
        "track_id": "1526210865%7C0719f1212d7b1e16fdadc097368a2c561a6015c53e29b8e96e%7C9a30482d91471d0db409cdc37a34c026",
    }

    def start_requests(self):
        print("start this spider!")
        for page in range(55, 1000000):
            self.shop_headers['referer'] = "https://www.ele.me/shop/" +  str(page)
            yield FormRequest(
                url="https://www.ele.me/restapi/shopping/restaurant/%s" % str(page),
                method="GET",
                meta={'page': page},
                formdata={
                    'latitude': '31.221809',
                    'longitude': '121.529169',
                    'terminal': 'web',
                },
                cookies=self.api_cookies,
                headers=self.shop_headers,
                callback=self.export_data
            )

    def export_data(self, response):

        try:
            data = json.loads(response.body)
            if data['name'] not in ["RESTAURANT_NOT_FOUND", "UNAUTHORIZED_RESTAURANT_ERROR"]:
                page = response.meta['page']
                print("export shop id is ================ %d" % page)
                # data = json.loads(response.body)
                item = NelmItem()
                print('@@@@@@@@' * 20)
                item['address'] = data['address']
                item['description'] = data['description']

                tem_flavors = ""
                if len(data['flavors']) > 0:
                    for fla in data['flavors']:
                        tem_flavors += str(fla['name'] + ",")
                item['flavors'] = tem_flavors
                item['float_delivery_fee'] = data['float_delivery_fee']
                item['float_minimum_order_amount'] = data['float_minimum_order_amount']
                item['ele_id'] = data['id']
                item['latitude'] = data['latitude']
                item['longitude'] = data['longitude']
                item['name'] = data['name']

                if 1 == len(data['opening_hours']):
                    item['opening_hours1'] = data['opening_hours'][0]
                    item['opening_hours2'] = ''
                    item['opening_hours3'] = ''
                elif 2 == len(data['opening_hours']):
                    item['opening_hours1'], item['opening_hours2'] = data['opening_hours']
                    item['opening_hours3'] = ''
                elif 3 == len(data['opening_hours']):
                    item['opening_hours1'], item['opening_hours2'], item['opening_hours3'] = data['opening_hours']
                else:
                    item['opening_hours1'] = "|".join(data['opening_hours'])
                    item['opening_hours2'] = ''
                    item['opening_hours3'] = ''

                item['order_lead_time'] = data['order_lead_time']

                if 1 == len(data['phone'].split(" ")):
                    item['phone1'] = data['phone'].split(" ")[0]
                    item['phone2'] = ''
                elif 2 == len(data['phone'].split(" ")):
                    item['phone1'], item['phone2'] = data['phone'].split(" ", 1)
                else:
                    item['phone1'] = ''
                    item['phone2'] = ''

                item['promotion_info'] = data['promotion_info']
                item['rating'] = data['rating']
                item['rating_count'] = data['rating_count']
                item['recent_order_num'] = data['recent_order_num']

                item['recommend_reasons'] = ''
                if 'recommend_reasons' in data.keys():
                    for ii in data['recommend_reasons']:
                        item['recommend_reasons'] = item['recommend_reasons'] + ii['name'] + '|'

                tem_supports = ""
                if len(data['supports']) > 0:
                    for sup in data['supports']:
                        tem_supports += str(sup['description'] + "|")
                item['supports'] = tem_supports

                if (-1 != data['address'].find(u"上海")):
                    item['city'] = 1
                else:
                    item['city'] = 0
                yield item

        except Exception as e:
            print(e)


    def parse(self, response):
        print("end >>>" * 10)
        pass
