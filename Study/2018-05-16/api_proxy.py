#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import hashlib
import requests
class ip_proxy(object):

    # http://ip.feiyiproxy.com:88/open?user_name=lt_test_1&timestamp=15889653664&md5=00112233445566778899AABBCCDDEEFF&pattern=json&number=2&province=510000&city=510100
    # 帐号：hyszscs518919_test
    # 密码：12345678
    def make_url(self):
        int_time = int(time.time())
        user_name = 'hyszscs518919_test'
        password = '12345678'
        str_md5 = hashlib.md5(bytes(user_name + password + str(int_time), encoding='utf-8')).hexdigest()

        url = 'http://ip.feiyiproxy.com:88/open?user_name=' + user_name + '&timestamp=' + \
            str(int_time) + '&md5=' + str_md5 + '&pattern=json&number=5'
        print(url)
        data = requests.get(url, verify=True, timeout=3).json()
        print(data)


if __name__ == '__main__':
    app = ip_proxy()
    app.make_url()