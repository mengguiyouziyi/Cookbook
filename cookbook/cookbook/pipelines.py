# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import sys
from os.path import dirname

father_path = dirname(dirname(os.path.abspath(dirname(__file__))))
base_path = dirname(dirname(os.path.abspath(dirname(__file__))))
path = dirname(os.path.abspath(dirname(__file__)))
sys.path.append(path)
sys.path.append(base_path)
sys.path.append(father_path)
import logging
from util.info import etl

logging.log(logging.DEBUG, msg=str(etl.get_host_info()))


class MysqlPipeline(object):
    def __init__(self, crawler):
        self.crawler = crawler
        self.spider = self.crawler.spider
        # 如果有其他item和表结构，需要打开这个注释，并更改spider名字和表名
        if self.spider.name == 'meishij':
            self.tab = 'meishij'
        elif self.spider.name == 'sbar':
            self.tab = 'sbar'
        else:
            self.tab = 'test'
        # self.rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
        self.conn = etl
        self.cursor = self.conn.cursor()
        self.col_list = self._get_column(self.tab)[1:-1]
        self.col_str = ','.join(self.col_list)
        self.val_str = self._handle_str(len(self.col_list))

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def _get_column(self, tab):
        """
        获取mysql表 字段字符串
        :param con:
        :param table_in:
        :return:
        """
        sql = """select group_concat(column_name) from information_schema.columns WHERE table_name = '{tab}' and table_schema = 'spider'""".format(
            tab=self.tab)
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print(e)
            print('获取数据表字段错误....')
            exit(1)
        results = self.cursor.fetchall()
        col_str = results[0]['group_concat(column_name)']
        col_list = col_str.split(',')
        return col_list

    def _handle_str(self, num):
        """
        根据插入字段数量来构造sql语句
        :param num: 插入字段数量
        :return: sql的value字符串
        """
        x = "%s"
        y = ", %s"
        for i in range(num - 1):
            x += y
        return x

    def process_item(self, item, spider):
        # print(item)
        sql = """insert into {tab} ({col}) VALUES ({val})""".format(tab=self.tab, col=self.col_str, val=self.val_str)
        args = [item[i] for i in self.col_list]
        try:
            self.cursor.execute(sql, args)
            self.conn.commit()
            print(item['title'])
        except Exception as e:
            # cnipr_comp = str(item['origin_id']) + '~' + str(item['only_id']) + '~' + str(
            # 	item['comp_full_name']) + '~' + str(item['cursorPage'])
            # self.rc.lpush('cnipr_fail', cnipr_comp)
            print(e)
            print('mysql error，链接为：{}'.format(item['url']))
            self.crawler.engine.close_spider(spider, 'mysql error')
