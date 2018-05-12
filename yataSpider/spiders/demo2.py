#!/usr/bin/python3  
# -*- coding: utf-8 -*-

import requests

s = requests.session()
s.verify = True
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

login_url = "https://h5.ele.me/restapi/eus/login/login_by_password"

data = {
        'captcha_hash': "",
        'captcha_value': "",
        'password': "5201314qq",
        'username': '18521568316',
}

result = s.post(login_url, json=data, headers=login_headers)
print(result.text)