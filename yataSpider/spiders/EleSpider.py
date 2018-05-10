#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import scrapy, json
from scrapy.http import Request, FormRequest, HtmlResponse
from yataSpider.items import YataspiderItem

class EleSpider(scrapy.Spider):

    use_lat_lon = []
    name = "EleSpider"
    allowed_domains = ["ele.me"]
    start_urls = ["https://www.ele.me/restapi/v2/pois"]

    address_header = {
        ":authority": "www.ele.me",
        ":method": "GET",
        ":path": "/home/",
        ":scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
    }

    bang_headers = {
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://www.ele.me/place/wtw3t7yb4zh3?latitude=31.221809&longitude=121.529169",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
        "x-shard": "loc=121.529169,31.221809"
    }

    def start_requests(self):
        return [
            FormRequest("https://www.ele.me/home/", headers = self.address_header,meta={'cookiejar': 1},callback=self.address_get_geo)
        ]

    def address_get_geo(self, response):
        print('aaaaaaaaaaaaaaaaaaaaaaaa')
        self.address_header['referer'] = "https://www.ele.me/home/"
        return [
            FormRequest(url = "https://www.ele.me/restapi/v2/pois",
                        method = 'GET',
                        meta = {'cookiejar': response.meta['cookiejar']},
                        formdata = {
                            'extras[]': 'count',
                            'geohash': 'wtw3sjq6n6um',
                            'keyword': u'一百杉杉大厦',
                            'limit': '20',
                            'type': 'nearby'
                        },
                        # cookies = self.geo_cookie,
                        headers = self.address_header,
                        callback = self.get_lat_lon)
        ]


    def get_lat_lon(self, response):

        print('sssssssssssssss')
        # data = json.loads(response.body_as_unicode())
        data = json.loads(response.body)
        if data is not None:
            self.use_lat_lon.append(str(data[0]['latitude']))
            self.use_lat_lon.append(str(data[0]['longitude']))
        print(self.use_lat_lon)
        return [
            FormRequest(
                url="https://www.ele.me/restapi/shopping/restaurants",
                method="GET",
                meta={'cookiejar': response.meta['cookiejar']},
                formdata={
                    'extras[]': 'activities',
                    'geohash': 'wtw3sjq6n6um',
                    'latitude': self.use_lat_lon[0],
                    'limit': '48',
                    'longitude': self.use_lat_lon[1],
                    'offset': '0',
                    'terminal': 'web'
                },
                headers=self.bang_headers,
                callback=self.export_data
            )
        ]


    def export_data(self, response):
        print("export data" * 20)
        data = json.loads(response.body)

        for v in data:
            item = YataspiderItem()
            print('@@@@@@@@' * 20)
            item['address'] = v['address']
            item['float_delivery_fee'] = v['float_delivery_fee'] # 配送费
            item['float_minimum_order_amount'] = v['float_minimum_order_amount'] # 最低起送
            item['cuisine'] = v['flavors'][0]['name'] # 菜系
            item['latitude'] = v['latitude'] # 纬度
            item['longitude'] = v['longitude'] # 经度
            item['name'] = v['name']
            if 1 == len(v['opening_hours']):
                item['opening_hours1'] = v['opening_hours'][0]
                item['opening_hours2'] = ''
                item['opening_hours3'] = ''
            elif 2 == len(v['opening_hours']):
                item['opening_hours1'], item['opening_hours2'] = v['opening_hours']
                item['opening_hours3'] = ''
            else:
                item['opening_hours1'], item['opening_hours2'], item['opening_hours3'] = v['opening_hours']

            if 1 == len(v['phone'].split(" ")):
                item['phone1'] = v['phone'].split(" ")
                item['phone2'] = ''
            elif 2 == len(v['phone'].split(" ")):
                item['phone1'], item['phone2'] = v['phone'].split(" ", 1)

            item['rating'] = v['rating'] # 综合评价
            item['order_lead_time'] = v['order_lead_time'] # 平均送达速度
            item['recommend_reasons'] = ''
            if 'recommend_reasons' in v.keys():
                for ii in v['recommend_reasons']:
                    item['recommend_reasons'] = item['recommend_reasons'] + ii['name'] + '|'
            yield item


    def parse(self, response):
        print('abc')
        return
        pass


### 运行指令
# scrapy crawl EleSpider -o item.json