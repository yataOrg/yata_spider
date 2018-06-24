#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import scrapy, json, math, random,time
from scrapy.http import FormRequest, HtmlResponse
from scrapy import Request
from decimal import *


# from yataSpider.items import NelmItem


class HotelSpider(scrapy.Spider):
    name = 'HotelSpider'
    allowed_domains = ['ebooking.ctrip.com']

    # http://ebooking.ctrip.com/ebkorder//Ajax/OrderAjax.ashx?v=0.9404447668229456
    # http://ebooking.ctrip.com/ebkorder//Ajax/OrderAjax.ashx?v=0.6270874592399025
    start_headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '486',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Host': 'ebooking.ctrip.com',
        'Origin': 'http://ebooking.ctrip.com',
        'Pragma': 'no-cache',
        'Referer': 'http://ebooking.ctrip.com/ebkorder/order/AllOrderList.aspx',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    start_cookies = {
        '_RGUID': '1602ab31-5c24-491f-a572-e09684abaebc',
        '_RSG': 'Va49S5pg2O1ywwg4Q9uoLA',
        '_RDG': '2879421ee4a8e1233a350e00219d4c609b',
        'ASP.NET_SessionId': 'd5vmzw2bdm5gqmjxopnhhft0',
        '_RF1': '183.240.33.167',
        'randomkey': '64dbc700-b028-4f92-8e03-4dfe3fce9c53',
        'clinetIp': '222.44.101.87',
        'MipHuName': '89C051D699FD9F0591D40CFA629A8CD0',
        'MipHuid': 'CDA4505E0969EE61',
        'ebk_basedata_Huid': 'CDA4505E0969EE61',
        'ishotelcompany': 'E29E0B9F05243659',
        'hotelcompany': '94823F71B32CC683',
        'hotelcompanyname': '05204165EA582B34D7145D188AEFF935E1AFDCEE88D8B824AC42BD892986EFEDBCC82BF5C7688188E3C1A6E6BA2B3FDB20F4DF7DC4FF7804A1BB2159F4552190',
        'hotelcompanyename': 'DBF2F766E9A0527D',
        'huid': 'CDA4505E0969EE61',
        'huname': '629DD31A4C802ABCF6276A2723018E9934ABE93F7FF032C1B76A84330D770FB1',
        'hotel_user_token': '8CA15E5C896D54D27ED65F9D5225B89773F3B5750210F2FA09F8ACE9D4C00605CDD494DA882A07A7',
        'ebk_login': 'IsNewVersion=T',
        'autoLogin': 'T',
        'usenewversion': 'yes',
        'CurrentLanguage': 'SimpChinese',
        'ASP.NET_SessionSvc': 'MTAuMTQuMy4xNzl8OTA5MHxvdXlhbmd8fDE1MjU4MzI1NjEyMDQ',
        '_fpacid': '09031132210365483632',
        'GUID': '09031132210365483632',
        'cticket': '0462CC643BCDAFDC1FFA47891B2A07A416F1B72CCA0230637F0BBE86E9A8E7CC',
        'DUID': 'u=6CB30ADCD4A4A86010CF0E13B3F5A1ABF71F3B9C37186641CF0E12A395AFFBFA&v=0',
        'IsNonUser': 'F',
        'imislogin': '1474092^1',
        'imuid': '_IMEBK2689071772',
        'basedatats': '1529802206',
        'EbookingHotelPreCookieIdentityhotel': '-1',
        'EbookingHotelPreCookieBookable': '',
        'ebk_basedata': 'Huid=CDA4505E0969EE61&IsSpecialSupplier=1103A49E7A8E7883&isDivCloseNotice=0&Hotel=B59080915E9B8BC1',
        'hotel': 'B59080915E9B8BC1',
        'hotelname': '05204165EA582B34D7145D188AEFF935E1AFDCEE88D8B824AC42BD892986EFEDBCC82BF5C7688188E3C1A6E6BA2B3FDB20F4DF7DC4FF7804A1BB2159F4552190',
        'hotelename': '00A9B72C2149987A26CFBCFBDE618B8E857C937ADBE8FE8013A1E5FFBCC85B0FFE2A375106578094',
        'ebooking': 'hotel=-1',
        'ebookinghotel': '-1',
        'timeszone': '-28800000',
        'EpushOrderCount': '0',
        'DonotShowNotice': 'T',
        'ebkneworder': 'Y',
        '_bfa': '1.1529802174150.adnkx.1.1529802174150.1529802177929.1.7.0',
        '_bfs': '1.6',
        '_bfi': 'p1%3D0%26p2%3D0%26v1%3D7%26v2%3D5',
        'pageSeqID': 'f5b43c7c-4bf8-4cb3-aa73-97e4cc9ef302',
        'lus': '2018-06-24 09:07:28',
        'extradatats': '1529802448',
        'RandomToken': 'ecb29a3a-0b6f-4e23-9681-425aaceeac3a'
    }

    form_data = {
        'DateType': 'ALL',
        'DateStart': '2018-05-24',
        'DateEnd': '2018-06-24',
        'OrderType': 'ALL',
        'OrderStatus': '0',
        'ReceiveType': '',
        'OrderID': '',
        'RoomName': '',
        'ClientName': '',
        'BookingNo': '',
        'IsGuarantee': 'false',
        'IsPP': 'false',
        'IsUrgent': 'false',
        'IsHoldRoom': 'false',
        'IsFreeSale': 'false',
        'IsCreditOrder': 'false',
        'IsBookingInvoice': 'false',
        'ConfirmName': '',
        'OrderBy': 'FormDate',
        'UnCheckInChecked': 'false',
        'TodayCheckInChecked': 'false',
        'TodayOrderChecked': 'false',
        'SourceType': 'Ebooking',
        'UnBookingInvoice': 'false',
        'PageIndex': '1',
        'FlagID': '0',
        'Method': 'QueryOrderList'
    }

    url_one = 'http://ebooking.ctrip.com/ebkorder//Ajax/OrderAjax.ashx?v=0.4494990724138175'

    def start_requests(self):
        print('open')
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        now_timestamp = time.time()
        self.start_cookies['extradatats'] = now_timestamp
        self.start_cookies['lus'] = now_time
        return [
            FormRequest(self.url_one, method='POST', headers=self.start_headers, cookies=self.start_cookies,
                        formdata=self.form_data, callback=self.get_list)
        ]

    def get_list(self, response):
        print(response.body)
