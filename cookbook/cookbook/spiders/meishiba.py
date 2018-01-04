# encoding:utf-8
import os
import sys
from os.path import dirname

father_path = dirname(dirname(os.path.abspath(dirname(__file__))))
base_path = dirname(dirname(os.path.abspath(dirname(__file__))))
path = dirname(os.path.abspath(dirname(__file__)))
sys.path.append(path)
sys.path.append(base_path)
sys.path.append(father_path)
import json
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from cookbook.items import SbarItem


class MeishijieSpider(CrawlSpider):
    name = 'sbar'
    allowed_domains = ['sbar.com.cn']
    start_urls = ['http://www.sbar.com.cn']
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'host': "www.sbar.com.cn",
            'connection': "keep-alive",
            'upgrade-insecure-requests': "1",
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            'referer': "http://www.sbar.com.cn/",
            'accept-encoding': "gzip, deflate",
            'accept-language': "zh-CN,zh;q=0.9,en;q=0.8",
            'cache-control': "no-cache",
        },
        'DOWNLOAD_DELAY': 1
    }
    rules = (
        Rule(LinkExtractor(allow=('cate\_list', 'caipu', 'shicai', 'baike', 'search'),
                           deny=('sbar\.com\.cn\/caipu\/\d+$'))),
        Rule(LinkExtractor(allow=('sbar\.com\.cn\/caipu\/\w+$'), deny=('sbar\.com\.cn\/caipu\/[a-z]+$')),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        if '一二三四五，上山打老虎，页面不在家，我找美食吧 404' in response.text:
            return
        s = Selector(text=response.text)
        pic = s.xpath('//img[@class="title_photo"]/@src').extract_first()
        title = s.xpath('//h1[@class="title"]/@title').extract_first()
        f_num = s.xpath('//div[starts-with(@id, "show_fav_count")]/text()').extract_first()
        nd = s.xpath('//li[@class="hr_r"]/a/text()').extract_first()  # 难度
        xgsc = s.xpath('//li[@class="shicai_list_li"]/a/@href').extract()  # 相关食材
        h3 = s.xpath('//div[@class="info_label"]/h3[@class="shicai_title"]/text()').extract()
        if '相关分类：' in h3:
            category = s.xpath('//div[@class="info_label"]/ul[1]/li/a/text()').extract()  # 相关分类
            xgzf = s.xpath('//div[@class="info_label"]/ul[2]/li/a/text()').extract()  # 相关做法
        else:
            category = []
            xgzf = s.xpath('//div[@class="info_label"]/ul[1]/li/a/text()').extract()
        original = s.xpath('//div[@class="infos"]/span[1]/a/@href').extract_first()  # 查看原文
        date = s.xpath('//div[@class="infos"]/span[2]/text()').extract_first()  # 上传时间
        viewclicknum = s.xpath('//div[@class="infos"]/span[3]/em/text()').extract_first()  # 浏览次数

        main_name = s.xpath('//ul[@class="ctim"][1]/li/span[1]/label/text()').extract()
        main_num = s.xpath('//ul[@class="ctim"][1]/li/span[2]/text()').extract()
        zl = dict(zip(main_name, main_num))  # 主料

        access_name = s.xpath('//ul[@class="ctim"][2]/li/span[1]/label/text()').extract()
        access_num = s.xpath('//ul[@class="ctim"][2]/li/span[2]/text()').extract()
        fl = dict(zip(access_name, access_num))  # 辅料
        item = SbarItem()
        item['url'] = response.url
        item['title'] = title if title else ''
        item['f_num'] = f_num if f_num else ''
        item['pic'] = pic if pic else ''
        item['category'] = json.dumps(category, ensure_ascii=False)
        item['nd'] = nd if nd else ''
        item['xgsc'] = json.dumps(xgsc, ensure_ascii=False)
        item['xgzf'] = json.dumps(xgzf, ensure_ascii=False)
        item['original'] = original if original else ''
        item['date'] = date if date else ''
        item['viewclicknum'] = viewclicknum if viewclicknum else ''
        item['zl'] = json.dumps(zl, ensure_ascii=False)
        item['fl'] = json.dumps(fl, ensure_ascii=False)

        yield item
