# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeishijieItem(scrapy.Item):
    # define the fields for your item here like:
    """
    item['url'] = response.url
    item['url'] = title  # 菜谱名称
    item['url'] = f_num  # 收藏人数

    item['pic'] = pic  # 菜谱图片链接
    item['news_id'] = n  # 菜谱id
    item['category'] = json.dumps(category, ensure_ascii=False)  # 分类
    item['pinglun'] = pinglun  # 评论数
    item['step'] = step  # 步骤数目

    item['url'] = gx  # 功效
    item['url'] = gy  # 工艺
    item['url'] = nd  # 难度
    item['url'] = rsh  # 人数
    item['url'] = kw  # 口味
    item['url'] = zbsj  # 准备时间
    item['url'] = prsj  # 烹饪时间
    item['url'] = author  # 作者
    item['url'] = author_url  # 作者主页url
    item['url'] = v_small  # 是否大V
    item['url'] = cp_num  # 作者菜谱数
    item['url'] = gz_num  # 作者被关注数
    item['url'] = fs_num  # 作者粉丝数
    item['url'] = date  # 菜谱上传时间
    item['url'] = viewclicknum  # 菜谱浏览量
    item['url'] = jy  # 作者寄语
    item['url'] = zl  # 主料
    item['url'] = fl  # 辅料
    item['url'] = prjq  # 烹饪技巧
    """
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

