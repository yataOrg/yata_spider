#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import scrapy, json, math
from scrapy.http import FormRequest, HtmlResponse
from scrapy import Request
from decimal import *
from yataSpider.items import YataspiderItem


class EleSpider(scrapy.Spider):

    math_distance = []
    use_lat_lon = []
    name = "EleSpider"
    allowed_domains = ["ele.me"]
    start_urls = ["https://www.ele.me/restapi/v2/pois"]

    list_all_gps = []

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
        "x-shard": "loc=121.596282,31.268485"
    }

    # 登录头
    login_headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '86',
        'content-type': 'application/json; charset=utf-8',
        'Host': 'h5.ele.me',
        'Origin': 'https://h5.ele.me',
        'Pragma': 'no-cache',
        'Referer': 'https://h5.ele.me/login/',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
    }


    earth_radius = 6371  # 地球近似半径

    def hav(self, theta):
        s = math.sin(theta / 2)
        return s * s

    def get_distance_hav(self, jwd):

        # 经纬度转换成弧度
        lat0, lng0 = jwd[0]
        lat1, lng1 = jwd[1]
        lat0 = float(lat0)
        lng0 = float(lng0)
        lat1 = float(lat1)
        lng1 = float(lng1)

        lat0 = math.radians(lat0)
        lat1 = math.radians(lat1)
        lng0 = math.radians(lng0)
        lng1 = math.radians(lng1)

        dlng = math.fabs(lng0 - lng1)
        dlat = math.fabs(lat0 - lat1)
        h = self.hav(dlat) + math.cos(lat0) * math.cos(lat1) * self.hav(dlng)
        distance = 2 * self.earth_radius * math.asin(math.sqrt(h))

        distance_km = Decimal(str(distance)).quantize(Decimal('0.000'))
        return distance_km



    def start_requests(self):
        return [
            FormRequest("https://www.ele.me/home/", headers=self.address_header, meta={'cookiejar': 1},
                        callback=self.address_get_geo)
        ]

    def login_in(self, response):
        print("###login" * 10)
        post_data = json.dumps({
            'captcha_hash': "",
            'captcha_value': "",
            'password': "5201314qq",
            'username': '18521568316',
        }, ensure_ascii=False)
        return [
            Request("https://h5.ele.me/restapi/eus/login/login_by_password",
                    method='POST',
                    body="{'captcha_hash': '', 'captcha_value': '', 'password': '5201314qq','username': '18521568316'}",
                    meta={'cookiejar': 1},
                    # meta={'cookiejar': response.meta['cookiejar']},
                    headers=self.login_headers,
                    callback=self.get_lat_lon
                    )
        ]


    def address_get_geo(self, response):
        print('aaaaaaaaaaaaaaaaaaaaaaaa'*10)

        self.address_header['referer'] = "https://www.ele.me/home/"
        return [
            FormRequest(url="https://www.ele.me/restapi/v2/pois",
                        method='GET',
                        meta={'cookiejar': response.meta['cookiejar']},
                        formdata={
                            'extras[]': 'count',
                            'geohash': 'wtw3sjq6n6um',
                            'keyword': u'东二小区',
                            'limit': '20',
                            'type': 'nearby'
                        },
                        # cookies = self.geo_cookie,
                        headers=self.address_header,
                        callback=self.get_lat_lon)
        ]

    def get_lat_lon(self, response):

        print('sssssssssssssss')
        # data = json.loads(response.body_as_unicode())
        data = json.loads(response.body)
        if data is not None:
            self.use_lat_lon.append(str(data[0]['latitude']))
            self.use_lat_lon.append(str(data[0]['longitude']))
        print(self.use_lat_lon)




        # 生成经纬度
        start_lon = float(121.17625)  #经度
        # self.list_all_gps = []
        while start_lon <= 122.015627:
            start_lat = float(30.736015)  # 纬度
            while start_lat <= 31.39919:
                self.list_all_gps.append([start_lon, start_lat])

                start_lat += float(Decimal(str(6 / 111)).quantize(Decimal('0.0000000')))
                start_lat = float(Decimal(start_lat).quantize(Decimal('0.0000000')))
                # Decimal(str(distance)).quantize(Decimal('0.000'))
                # start_lon += 6 / (111 * math.cos(start_lat))


            start_lon += float(Decimal(str(6 / (111 * math.cos(30.736015)))).quantize(Decimal('0.0000000')))
            start_lon = float(Decimal(start_lon).quantize(Decimal('0.0000000')))

        # 第二层添加 圆圈之间的间隙
        start_lon = 121.17625 + float(Decimal(str(3 / (111 * math.cos(30.736015)))).quantize(Decimal('0.0000000')))
        start_lon1 = float(Decimal(start_lon).quantize(Decimal('0.0000000')))
        start_lat = 30.736015 + float(Decimal(str(3 / 111)).quantize(Decimal('0.0000000')))
        start_lat = float(Decimal(start_lat).quantize(Decimal('0.0000000')))

        while start_lon1 <= 122.015627:
            start_lat1 = float(start_lat)  # 纬度
            while start_lat1 <= 31.39919:
                self.list_all_gps.append([start_lon1, start_lat1])

                start_lat1 += float(Decimal(str(6 / 111)).quantize(Decimal('0.0000000')))
                start_lat1 = float(Decimal(start_lat1).quantize(Decimal('0.0000000')))
                # Decimal(str(distance)).quantize(Decimal('0.000'))
                # start_lon += 6 / (111 * math.cos(start_lat))


            start_lon1 += float(Decimal(str(6 / (111 * math.cos(30.736015)))).quantize(Decimal('0.0000000')))
            start_lon1 = float(Decimal(start_lon1).quantize(Decimal('0.0000000')))

        print('#####################################################'*2)
        print(len(self.list_all_gps))
        # return
        # 进行循环遍历
        for jwd in self.list_all_gps:

            page_list = [0, 24]
            for page in page_list:
                yield FormRequest(
                    url="https://www.ele.me/restapi/shopping/restaurants",
                    method="GET",
                    meta={'cookiejar': response.meta['cookiejar'], 'jwd': str(jwd[0]) + ", " + str(jwd[1])},
                    formdata={
                        'extras[]': 'activities',
                        'geohash': 'wtw3sjq6n6um',
                        'latitude': str(jwd[1]),
                        'limit': '24',
                        'longitude': str(jwd[0]),
                        'offset': str(page),
                        'terminal': 'web'
                    },
                    headers=self.bang_headers,
                    callback=self.export_data
                )





        # return [
        #     FormRequest(
        #         url="https://www.ele.me/restapi/shopping/restaurants",
        #         method="GET",
        #         meta={'cookiejar': response.meta['cookiejar']},
        #         formdata={
        #             'extras[]': 'activities',
        #             'geohash': 'wtw3sjq6n6um',
        #             'latitude': self.use_lat_lon[0],
        #             'limit': '24',
        #             'longitude': self.use_lat_lon[1],
        #             'offset': '0',
        #             'terminal': 'web'
        #         },
        #         headers=self.bang_headers,
        #         callback=self.export_data
        #     )
        # ]

    def export_data(self, response):
        print("export data" * 20)
        data = json.loads(response.body)

        for v in data:
            item = YataspiderItem()
            print('@@@@@@@@' * 20)
            item['address'] = v['address']
            item['float_delivery_fee'] = v['float_delivery_fee']  # 配送费
            item['float_minimum_order_amount'] = v['float_minimum_order_amount']  # 最低起送
            item['cuisine'] = v['flavors'][0]['name']  # 菜系
            item['latitude'] = v['latitude']  # 纬度
            item['longitude'] = v['longitude']  # 经度

            self.math_distance = []
            self.math_distance.append(self.use_lat_lon)
            self.math_distance.append([v['latitude'], v['longitude']])
            # 计算距离
            item['distance'] = self.get_distance_hav(self.math_distance)

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
                item['phone1'] = v['phone'].split(" ")[0]
                item['phone2'] = ''
            elif 2 == len(v['phone'].split(" ")):
                item['phone1'], item['phone2'] = v['phone'].split(" ", 1)
            else:
                item['phone1'] = ''
                item['phone2'] = ''

            item['rating'] = v['rating']  # 综合评价
            item['order_lead_time'] = v['order_lead_time']  # 平均送达速度
            item['recommend_reasons'] = ''
            if 'recommend_reasons' in v.keys():
                for ii in v['recommend_reasons']:
                    item['recommend_reasons'] = item['recommend_reasons'] + ii['name'] + '|'

            item['ele_distance'] = v['distance']
            item['ele_id'] = v['id']
            item['ele_authentic_id'] = v['authentic_id']
            item['search_jwd'] = response.meta['jwd']
            yield item

    def parse(self, response):
        print('abc')
        return
        pass

### 运行指令
# scrapy crawl EleSpider -o item.json
