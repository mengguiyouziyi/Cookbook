# encoding:utf-8
import re
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
        Rule(LinkExtractor(allow=('\/chufang\/diy\/', 'recipe\_list'), )),
        Rule(LinkExtractor(allow=('zuofa\/\w+.html',)), callback='parse_item', follow=True),
    )

    # def __init__(self, *args, **kwargs):
    #     super(MeishijieSpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        s = Selector(text=response.text)
        item = MeishijieItem()
        title = s.xpath('//*[@id="tongji_title"]/@title').extract_first()
        f_num = s.xpath('//*[@id="f_num"]/text()').extract_first().replace('(', '').replace(')', '')
        gx = s.xpath('//dl[@class="yj_tags clearfix"]/dt/a/text()').extract()
        gx = ','.join(gx)
        gy = s.xpath('//*[@id="tongji_gy"]/text()').extract_first()
        nd = s.xpath('//*[@id="tongji_nd"]/text()').extract_first()
        rsh = s.xpath('//*[@id="tongji_rsh"]/text()').extract_first()
        kw = s.xpath('//*[@id="tongji_kw"]/text()').extract_first()
        zbsj = s.xpath('//*[@id="tongji_zbsj"]/text()').extract_first()
        prsj = s.xpath('//*[@id="tongji_prsj"]/text()').extract_first()
        author = s.xpath('//*[@id="tongji_author"]/text()').extract_first()
        author_url = s.xpath('//*[@id="tongji_author"]/@href').extract_first()
        v_small = s.xpath('//a[@class="v_small"]/@title').extract_first()
        v_small = v_small if v_small else ''
        info = s.xpath('//div[@class="info"]')
        span = info.xpath('./span/text()').extract_first()
        cp_num = re.search(r'菜谱：(\d+)', span).group(1)
        gz_num = re.search(r'关注：(\d+)', span).group(1)
        fs_num = re.search(r'粉丝：(\d+)', span).group(1)
        strong = info.xpath('./strong/text()').extract_first()
        date = re.search(r'\d\d\d\d\-\d\d\-\d\d', strong).group()
        viewclicknum = s.xpath('//*[@id="viewclicknum"]/text()').extract_first()
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
        item['f_num'] = f_num  # 收藏人数
        item['gx'] = gx  # 功效
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
        item['viewclicknum'] = viewclicknum  # 菜谱浏览量
        item['jy'] = jy  # 作者寄语
        item['zl'] = zl  # 主料
        item['fl'] = fl  # 辅料
        item['prjq'] = prjq  # 烹饪技巧














