#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import scrapy
class DemoSpider(scrapy.Spider):

	name = 'demo'
	allowed_domains = ['duitang.com']
	start_urls = [
		"https://www.duitang.com/search/?kw=%E8%82%96%E6%88%98&type=feed",
		"https://www.duitang.com/search/?kw=%E5%A4%8F%E5%A4%A9&type=feed"
	]

	def parse(self, response):
		print('ssssssssssssssssssss'*12)
		print('@@@@@@@@@'*12)