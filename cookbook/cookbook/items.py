# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeishijieItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    f_num = scrapy.Field()

    pic = scrapy.Field()
    news_id = scrapy.Field()
    category = scrapy.Field()
    pinglun = scrapy.Field()
    step = scrapy.Field()

    gx = scrapy.Field()
    gy = scrapy.Field()
    nd = scrapy.Field()
    rsh = scrapy.Field()
    kw = scrapy.Field()
    zbsj = scrapy.Field()
    prsj = scrapy.Field()
    author = scrapy.Field()
    author_url = scrapy.Field()
    v_small = scrapy.Field()
    cp_num = scrapy.Field()
    gz_num = scrapy.Field()
    fs_num = scrapy.Field()
    date = scrapy.Field()
    viewclicknum = scrapy.Field()
    jy = scrapy.Field()
    zl = scrapy.Field()
    fl = scrapy.Field()
    prjq = scrapy.Field()


class SbarItem(scrapy.Item):
    """
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
        item['see_num'] = see_num if see_num else ''
        item['zl'] = json.dumps(zl, ensure_ascii=False)
        item['fl'] = json.dumps(fl, ensure_ascii=False)
    """
    url = scrapy.Field()
    title = scrapy.Field()
    f_num = scrapy.Field()
    pic = scrapy.Field()
    category = scrapy.Field()
    nd = scrapy.Field()
    xgsc = scrapy.Field()
    xgzf = scrapy.Field()
    original = scrapy.Field()
    date = scrapy.Field()
    viewclicknum = scrapy.Field()
    zl = scrapy.Field()
    fl = scrapy.Field()
