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
import re
import time
import scrapy
import json
from ast import literal_eval
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from cookbook.items import MeishijieItem


class MeishijieSpider(CrawlSpider):
    name = 'meishij'
    allowed_domains = ['meishij.net', 'meishi.cc']
    start_urls = ['http://www.meishij.net/']
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            'accept-encoding': "gzip, deflate",
            'accept-language': "zh-CN,zh;q=0.9,en;q=0.8",
            'cache-control': "no-cache",
            'connection': "keep-alive",
            # 'cookie': "Hm_lvt_01dd6a7c493607e115255b7e72de5f40=1514363631; UM_distinctid=160971b358c588-02afce166b44a-3c60460e-1fa400-160971b358da45; AJSTAT_ok_times=1; __51cke__=; MSCookieKey=06aaa042ebfa1def83c2f9deaec51e6a.; tma=162999840.12096840.1514364632242.1514364632242.1514364632242.1; fingerprint=c525ece222b3b3635a3206cea96569ef; bfd_s=126376916.463106886695317.1514364632332; bfd_g=826702420a014e1a00004c70000075495a435ed7; CNZZDATA1259001544=611834762-1514358835-http%253A%252F%252Fi.meishi.cc%252F%7C1514364235; AJSTAT_ok_pages=2; __tins__2139665=%7B%22sid%22%3A%201514364625767%2C%20%22vd%22%3A%202%2C%20%22expires%22%3A%201514368195557%7D; __51laig__=2; CNZZDATA5955072=cnzz_eid%3D1492890349-1514360097-null%26ntime%3D1514365498; tmc=10.162999840.12096840.1514364632242.1514366431417.1514366578411; tmd=10.162999840.12096840.1514364632242.; amvid=66fdd61abb6f81a1ade43b4a4de2b496; Hm_lpvt_01dd6a7c493607e115255b7e72de5f40=1514367173",
            'host': "www.meishij.net",
            'referer': "http://www.meishij.net/jiankang/yangsheng/",
            'upgrade-insecure-requests': "1",
            # 'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
            'postman-token': "cb89c719-651e-7a84-dddc-1ecc127ab3a6"
        },
    }
    rules = (
        Rule(LinkExtractor(allow=('\/chufang\/diy\/', 'recipe\_list', 'huodong'))),
        Rule(LinkExtractor(allow=('zuofa\/\w+.html',)), callback='parse_item', follow=True),
    )

    # def __init__(self, *args, **kwargs):
    #     super(MeishijieSpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        if 'error_404' in response.text:
            return
        s = Selector(text=response.text)
        item = MeishijieItem()
        title = s.xpath('//*[@id="tongji_title"]/@title').extract_first()
        # f_num = s.xpath('//*[@id="f_num"]/text()').extract_first().replace('(', '').replace(')', '')
        # gx = s.xpath('//dl[@class="yj_tags clearfix"]/dt/a/text()').extract()
        # gx = ','.join(gx)
        # gy = s.xpath('//*[@id="tongji_gy"]/text()').extract()
        # gy = ''.join(gy)
        # nd = s.xpath('//*[@id="tongji_nd"]/text()').extract()
        # nd = ''.join(nd)
        # rsh = s.xpath('//*[@id="tongji_rsh"]/text()').extract()
        # rsh = ''.join(rsh)
        # kw = s.xpath('//*[@id="tongji_kw"]/text()').extract()
        # kw = ''.join(kw)
        # zbsj = s.xpath('//*[@id="tongji_zbsj"]/text()').extract()
        # zbsj = ''.join(zbsj)
        # prsj = s.xpath('//*[@id="tongji_prsj"]/text()').extract()
        # prsj = ''.join(prsj)
        pic = re.search(r'"pic" :"(.*?)",', response.text).group(1)
        n = s.xpath('//*[@id="news_id"]/@value').extract_first()
        category = re.search(r'"category" :(.*),', response.text).group(1)
        category = literal_eval(category)
        pinglun = re.search(r'"pinglun":"(.*)",', response.text).group(1)
        step = re.search(r'"step":"(.*)",', response.text).group(1)

        gx = re.search(r'"tag" :(.*),', response.text).group(1)
        gx = literal_eval(gx)
        gy = re.search(r'"gongyi":"(.*)"', response.text).group(1)
        nd = re.search(r'"nandu":"(.*)"', response.text).group(1)
        rsh = re.search(r'"renshu":"(.*)"', response.text).group(1)
        kw = re.search(r'"kouwei":"(.*)"', response.text).group(1)
        zbsj = re.search(r'"zbshijian":"(.*)"', response.text).group(1)
        prsj = re.search(r'"prshijian":"(.*)"', response.text).group(1)
        author = s.xpath('//*[@id="tongji_author"]/text()').extract_first().strip()
        author_url = s.xpath('//*[@id="tongji_author"]/@href').extract_first()
        v_small = s.xpath('//a[@class="v_small"]/@title').extract_first()
        v_small = v_small if v_small else ''
        info = s.xpath('//div[@class="info"]')
        span = info.xpath('./span/text()').extract_first()
        cp_num = re.search(r'菜谱：(\d+)', span)
        cp_num = cp_num.group(1) if cp_num else ''
        gz_num = re.search(r'关注：(\d+)', span)
        gz_num = gz_num.group(1) if gz_num else ''
        fs_num = re.search(r'粉丝：(\d+)', span)
        fs_num = fs_num.group(1) if fs_num else ''
        strong = info.xpath('./strong/text()').extract_first()
        date = re.search(r'\d\d\d\d\-\d\d\-\d\d', strong)
        date = date.group() if date else ''
        # viewclicknum = s.xpath('//*[@id="viewclicknum"]/text()').extract_first()
        jy = s.xpath('//div[@class="materials"]/p/text()').extract()
        jy = ''.join(jy)
        zl_ul = s.xpath('//div[@class="yl zl clearfix"]/ul')
        zl_mc = zl_ul.xpath('./li/div/h4/a/text()').extract()
        zl_yl = zl_ul.xpath('./li/div/h4/span/text()').extract()
        zl = dict(zip(zl_mc, zl_yl))
        fl_ul = s.xpath('//div[@class="yl fuliao clearfix"]/ul')
        fl_mc = fl_ul.xpath('./li/h4/a/text()').extract()
        fl_yl = fl_ul.xpath('./li/span/text()').extract()
        fl = dict(zip(fl_mc, fl_yl))
        prjq = s.xpath('//div[@class="editnew edit"]/input/@value').extract_first()
        item['url'] = response.url
        item['title'] = title  # 菜谱名称

        item['pic'] = pic  # 菜谱图片链接
        item['news_id'] = n  # 菜谱id
        item['category'] = json.dumps(category, ensure_ascii=False)  # 分类
        item['pinglun'] = pinglun  # 评论数
        item['step'] = step  # 步骤数目
        # print(item['pic'], item['news_id'], item['category'], item['pinglun'], item['step'])
        # print(pic, n, json.dumps(category, ensure_ascii=False), pinglun, step)

        item['gx'] = json.dumps(gx, ensure_ascii=False)  # 功效
        item['gy'] = gy  # 工艺
        item['nd'] = nd  # 难度
        item['rsh'] = rsh  # 人数
        item['kw'] = kw  # 口味
        item['zbsj'] = zbsj  # 准备时间
        item['prsj'] = prsj  # 烹饪时间
        item['author'] = author  # 作者
        item['author_url'] = author_url  # 作者主页url
        item['v_small'] = v_small  # 是否大V
        item['cp_num'] = cp_num  # 作者菜谱数
        item['gz_num'] = gz_num  # 作者被关注数
        item['fs_num'] = fs_num  # 作者粉丝数
        item['date'] = date  # 菜谱上传时间
        item['jy'] = jy  # 作者寄语
        item['zl'] = json.dumps(zl, ensure_ascii=False)  # 主料
        item['fl'] = json.dumps(fl, ensure_ascii=False)  # 辅料
        item['prjq'] = prjq  # 烹饪技巧
        click = "http://click.meishij.net/pl/click.php?from_search={f}&classid=1&id={n}&addclick=1&_{t}"
        f = s.xpath('//*[@id="from_search"]/@value').extract_first()
        t = int(time.time() * 1000)
        c_url = click.format(n=n, f=f, t=t)
        yield scrapy.Request(c_url, meta={'item': item}, callback=self.parse_click)

    def parse_click(self, response):
        viewclicknum = re.search(r"\('viewclicknum'\)\.innerHTML=(\d+);", response.text)
        viewclicknum = viewclicknum.group(1) if viewclicknum else ''
        f_num = re.search(r"\('f_num'\)\.innerHTML='\((\d+)\)';", response.text)
        f_num = f_num.group(1) if f_num else ''
        item = response.meta.get('item', {})
        item['f_num'] = f_num  # 收藏人数
        item['viewclicknum'] = viewclicknum  # 菜谱浏览量
        # print(item)
        yield item
