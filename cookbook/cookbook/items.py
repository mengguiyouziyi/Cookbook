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
    url = scrapy.Field()
    title = scrapy.Field()
    f_num = scrapy.Field()
    pic = scrapy.Field()
    category = scrapy.Field()
    zf = scrapy.Field()
    kw = scrapy.Field()
    nd = scrapy.Field()
    xgsc = scrapy.Field()
    xgzf = scrapy.Field()
    original = scrapy.Field()
    date = scrapy.Field()
    viewclicknum = scrapy.Field()
    zl = scrapy.Field()
    fl = scrapy.Field()


class BlueapronItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    sub_title = scrapy.Field()
    time = scrapy.Field()
    servings = scrapy.Field()
    nutrition = scrapy.Field()
    descriptions = scrapy.Field()
    likes = scrapy.Field()
    save = scrapy.Field()
    ingredients = scrapy.Field()
    tools = scrapy.Field()


class Allrecipes(scrapy.Item):
    """
    item['url'] = response.url
    item['title'] = title
    item['star_num'] = str(star_num)
    item['made_it'] = made_it
    item['review_count'] = str(review_count)
    item['picture_count'] = str(picture_count)
    item['author'] = author
    item['descriptions'] = descriptions
    item['pics'] = json.dumps(pics, ensure_ascii=False)
    item['time'] = time
    item['servings'] = servings
    item['nutrition'] = nutrition
    item['ingredients'] = json.dumps(ingredients, ensure_ascii=False)
    item['pretime'] = pretime
    item['cooktime'] = cooktime
    item['totaltime'] = totaltime
    item['directions'] = json.dumps(directions, ensure_ascii=False)
    """
    url = scrapy.Field()
    title = scrapy.Field()
    star_num = scrapy.Field()
    made_it = scrapy.Field()
    review_count = scrapy.Field()
    picture_count = scrapy.Field()
    author = scrapy.Field()
    descriptions = scrapy.Field()
    pics = scrapy.Field()
    time = scrapy.Field()
    servings = scrapy.Field()
    nutrition = scrapy.Field()
    ingredients = scrapy.Field()
    pretime = scrapy.Field()
    cooktime = scrapy.Field()
    totaltime = scrapy.Field()
    directions = scrapy.Field()