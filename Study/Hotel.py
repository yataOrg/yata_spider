#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# http://music.163.com/#/discover/playlist/?order=hot
from selenium import webdriver
import csv,time

url = "http://ebooking.ctrip.com/ebkorder/order/AllOrderList.aspx"
chrome_options = webdriver.chrome.options.Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# 开启主动调用浏览器 方便测试
# driver = webdriver.PhantomJS()
driver = webdriver.Chrome(chrome_options = chrome_options)
csv_file = open("hotellist.csv", "w", newline='')
writer = csv.writer(csv_file)
writer.writerow(['姓名', '预定客房', '价格'])


driver.get(url)
time.sleep(4)

data = driver.find_element_by_css_selector('ul.ordersSyn-list').find_elements_by_css_selector('li')
print(len(data))

# for i in range(len(data)):
#     nb = data[i].find_element_by_class_name('nb').text
#     if '万' in nb or int(nb) > 500:
#         msk = data[i].find_element_by_css_selector('a.msk')
#         writer.writerow([msk.get_attribute('title'), nb, msk.get_attribute('href')])
#
# url = driver.find_element_by_css_selector('a.zbtn.znxt').get_attribute('href')

csv_file.close()

### 卡住了 每次打开浏览器都要重新登录



