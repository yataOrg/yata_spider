#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from twisted.enterprise import adbapi
class YataspiderPipeline(object):

    # 140.143.32.44
    def __init__(self):
        dbparms = dict(
            host = 'localhost',
            db = 'yata_data_01',
            user = 'root',
            passwd = '',
            charset = 'utf8',
            cursorclass = pymysql.cursors.DictCursor,
            use_unicode = True
        )
        self.dbpool = adbapi.ConnectionPool("pymysql", **dbparms)


    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error, item, spider)


    def handle_error(self, failure, item, spider):
        print('this has errors')
        insert_sql, params = item.get_insert_sql()
        print(insert_sql % params)
        print(failure)

    def do_insert(self, cursor, item):
        insert_sql, params = item.get_insert_sql()
        print("target going up up" + "@@"*10)
        # print(insert_sql % params)
        cursor.execute(insert_sql % params)