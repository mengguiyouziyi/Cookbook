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


class AllrecipesItem(scrapy.Item):
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


class EatingwellItem(scrapy.Item):
    url = scrapy.Field()
    pic = scrapy.Field()
    title = scrapy.Field()
    rate = scrapy.Field()
    review = scrapy.Field()
    submitter = scrapy.Field()
    submitterLogo = scrapy.Field()
    submitterTitle = scrapy.Field()
    submitterRole = scrapy.Field()
    nutrition_profile = scrapy.Field()
    ingredients = scrapy.Field()
    active = scrapy.Field()
    totalTime = scrapy.Field()
    step = scrapy.Field()


class CookpadItem(scrapy.Item):
    """
        item['url'] = response.url
        item['title'] = title
        item['pic'] = pic
        item['likes'] = likes
        item['camera'] = camera
        item['desc'] = desc
        item['author_url'] = author_url
        item['author'] = author
        item['ingredients'] = json.dumps(Ingredients, ensure_ascii=False)
        item['servings'] = servings
        item['cook_time'] = cook_time
        item['instructions'] = json.dumps(instructions, ensure_ascii=False)
    """
    url = scrapy.Field()
    title = scrapy.Field()
    pic = scrapy.Field()
    likes = scrapy.Field()
    camera = scrapy.Field()
    description = scrapy.Field()
    author_url = scrapy.Field()
    author = scrapy.Field()
    ingredients = scrapy.Field()
    servings = scrapy.Field()
    cook_time = scrapy.Field()
    instructions = scrapy.Field()
