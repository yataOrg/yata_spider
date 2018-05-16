#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import scrapy, json, math, random
from scrapy.http import FormRequest, HtmlResponse
from scrapy import Request
from decimal import *
from yataSpider.items import NelmItem


class NelmSpider(scrapy.Spider):
    name = "NelmSpider"
    allowed_domains = ["ele.me"]
    start_urls = ["https://www.ele.me/home/"]

    start_headers = {
        ":authority": "www.ele.me",
        ":method": "GET",
        ":path": "/home/",
        ":scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "referer": "https://www.ele.me/place",
        "upgrade-insecure-requests": '1',
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    }


    shop_headers = {
        ":authority": "www.ele.me",
        ":method": "GET",
        ":path": "/restapi/shopping/restaurant/156427001?latitude=31.223809&longitude=121.549169&terminal=web",
        ":scheme": "https",
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "referer": "https://www.ele.me/shop/56",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
        "x-shard": "shopid=156427001;loc=121.549169,31.223809",
    }

    api_cookies = {
        "ubt_ssid": "qc6hy19lrtojld9veblqwbn55qqaotwo_2018-05-10",
        "_utrace": "40056258e5b7c860e863076b79003b5d_2018-05-10",
        "eleme__ele_me": "ff20a4ab936ba5aea3874dbd40f9645f%3Ada61055c4a57ed7537d4908e3cf7883546321650",
        "track_id": "1526210865|0719f1212d7b1e16fdadc097368a2c561a6015c53e29b8e96e|9a30482d91471d0db409cdc37a34c026",
        "USERID": "28546361",
        "SID": "QrCBQQciftlRlfwZRj9axBEMgSvhrhrsby9g",
    }

    def start_requests(self):
        return [
            FormRequest("https://www.ele.me/home/", headers=self.start_headers, meta={'cookiejar': 1},
                        callback=self.get_shop)
        ]

    def get_shop(self, response):
        print("start this spider!")
        de_lat = 31.213809
        de_lon = 121.529169
        page = 55
        while page <= 10000:

            add_float_num = round(random.uniform(0.000009,0.009), 6)
            self.shop_headers['referer'] = "https://www.ele.me/shop/" +  str(page)
            self.shop_headers[':path'] = "/restapi/shopping/restaurant/" + str(page) + "?latitude=" + str(round(de_lat + add_float_num, 6)) + "&longitude=" + str(round(de_lon + add_float_num, 6)) + "&terminal=web"
            self.shop_headers['x-shard'] = "shopid=" + str(page) + ";loc=" +  str(round(de_lon + add_float_num, 6)) + "," + str(round(de_lat + add_float_num, 6))
            yield FormRequest(
                url="https://www.ele.me/restapi/shopping/restaurant/%s" % str(page),
                method="GET",
                meta={'cookiejar': response.meta['cookiejar'], 'page': page},
                formdata={
                    'latitude': str(round(de_lat + add_float_num, 6)),
                    'longitude': str(round(de_lon + add_float_num, 6)),
                    'terminal': 'web',
                },
                # cookies=self.api_cookies,
                headers=self.shop_headers,
                callback=self.export_data
            )
            page += 1

    def export_data(self, response):

        try:
            data = json.loads(response.body)
            print(data)
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
