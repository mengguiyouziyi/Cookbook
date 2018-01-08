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
import scrapy
import re
from urllib.parse import urljoin
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from cookbook.items import AllrecipesItem


class MeishijieSpider(CrawlSpider):
    name = 'allrecipes'
    allowed_domains = ['allrecipes.com']
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'host': "allrecipes.com",
            'connection': "keep-alive",
            'cache-control': "no-cache",
            'upgrade-insecure-requests': "1",
            # 'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            'accept-encoding': "gzip, deflate",
            'accept-language': "zh-CN,zh;q=0.9,en;q=0.8",
            # 'cookie': "FirstImpression=False; ARSiteUser=1-6f50b6b3-90cc-472a-b81f-49103c2d2ee5; ARCompressedSession=PgcAAB+LCAAAAAAABAB9VV2TojoQ/S++ulMCKsJU3QdQQfwC+VTfIgSIQoIkCLi1//0yzqwzs3frVlEFOd2cPp0+gZ89ByUYsKqEvddeu67nx7jIEQISphyqQYUtVTq7Dm9yhF/PVDDnJvJU8+9Xc5+nk7XYP+ALOOeVzFv3MI2ExXKEm9mO+aPxMqiGJ7UfOvxuHGl7s82u7Uaen0v5mOiBxsuKeM1va10m5uA4LlouCXB/cjeF49UwYLrD/M099zmu1o+JTBjpi740YqLs7DYevOPWlLKiFmaj2zkBeGkeXDkrU5WjhmgHce3PrJmet32RcdMLPxGl7GKodswAHVkrGh39drc+tzPkkDCpOF7JzP0W1fYi9Sa3YGmlfak5xFdXFWoLrqwyMLtn1MTemUWcup4doRLGQn+fJpWOqcd27DwrUvUAk2S3lMejiYEvyAv2WKlYqtfXNBSijWdNyPC6WG80ENj7xJwPhRomFQFwvxwkS42KbGvaRL4d5XzMycSBEp+XAnSz4cC2sRfsPE44uT6wByNXnh0GUibHywUw56Dd21EAls1ESfK+Uzgbzpd2cqFPRmITHHbjbLKy6GU5btZBIc535lSqJxpFHlxPV+FIu/Lj/MpmxwM/TQKbp7gtqap2VLI+slz1mqLc8vlVLFXHJBkCTfGTcOCJtXo9NhOBJwchvsrt8mxCMrIiXcthcwyX8UxMh4eVC/J0ZqxKmOG11xAQstN4E+MgFZl4UujlakJBvrYhIL58XW2G9CAGyvl8GsVu0jiJYrh6oWzvq0tqq/a+jNAgHJc8n/m+I2QsTYHeH25Tfa/Zir+gk60WJSq33p78DKh3xWaCXIO1va9vU3hONHsKGnkNRevYX+QQBR0/kfRzvthEk8vQMbwlW5OkVcb926Chg6k8x0WjWrYhS4ku2Uch0qdzyQ+qMJQtFC2iUaAddnPn3nhmQedqDlBgGN62LKmtcv0MXtz4zm6lfFkLR0vMmsQcW3QQqR5xDhTbmarg7FIuYLNRa3tLijkfVZJ/DDTXxSXbDndB20pWm2xG15BIbLdb9uX5P70fvSkhFwQNHJPe68+PlV6hqDvJ/IsYj7mTeBq+yFwYvowmAng5SXz8MpJ5btiZUYBw/Mkx671yP3oGfXMrxAyFgMGOJwYZhW94tyMJjAz8BepSSQejr5gNc5ifYLmBT9CjsPygf2S7bQEfqwWK4KI6OVl3L5/pC0BTo6uMqyz79UapoZIyF+XQRxQx0mWysoLPiJEXJaQUEfwZsGGICqiSZkOiKoPKDaAMnLJPTVsII2qV8IZgbcO4I0i/x5yqKEjJEE42j34c1n0i6Z+pj9Z+735FGcmfrc4QLTLQbkEO33v50Zt3xsiUKHqT+w3TSJkD9nhtC2uaQcZgqSLmVPkDtEoSowwaOUieZH8KpCkqHjIADmGWwWjWDfB38rs2r8xccoH4WRt/JPU4juNfHpfLca+Pq/eYhJqR5Mt0502Bym+28GGJYgSj/0aUkKEb/AI8lT2xblNL9j8Sfj00uIAy2M0qhiXsGOjfjNWVwwS3OanoNxeQBKP7l4qfe/U+0N4r3xUxc4zefoAfBvvtvr8ElNPpzTTvZ6PX+/Uvtjoqcz4HAAA=; bounceClientVisit2602v=N4IgNgDiBcIBYBcEQKQGYCCKBMAxHuAhmGAE4CmAxgJYTkDOAdJQPYC2BFNd9BIANCFIwQIAL5A; s_fid=1051CFAE2DC7838B-0FC8FF526BE4032F; s_cc=true; telemetryUserId=ee439fed-3902-4629-97de-68a1f2d5a6e3; s_vi=[CS]v1|2D279B17051D3897-6000190E0000366B[CE]; __gads=ID=7441c10be167a84a:T=1515140657:S=ALNI_MYOHbsnuwB4BkoYZCNLA8liPGNQUw; __ybotb=a6b9; __ybotu=jc1np4tcamukesvuah; __ybotc=http%3A//ads-adseast-vpc.yldbt.com/m/; fsr.r=%7B%22d%22%3A90%2C%22i%22%3A%22d464cf8-84660044-129d-72f1-f9c0f%22%2C%22e%22%3A1515745833731%7D; s_sq=%5B%5BB%5D%5D; telemetryPageviewId=4d362116-4042-43d5-b910-9bb8d1a60aea; __ybotv=1515141093331; __ybots=jc1np4td4lgaenynbv.1.jc1nvxsj3zety5ub98.33; ARToken=84XAr4Z2Z57+ieH6qwuIrfn/QfNJNX2LPKYVV7oOQ5BdzCBQZvZrqU8ETzynz0Yehdu4ajIeuM2Zp3D0wzr1pG0Em6jejp3leOwxPdMKFWgdPsADCgS2r1xEVt0XYmW+MU8aN2expvC16ejlfHUMcWfycyP3VT6M0z5nJH0GfSa2nkr1iaR8lg==; fsr.s=%7B%22cp%22%3A%7B%22ovid%22%3A%222D279B17051D3897-6000190E0000366B%22%2C%22vstat%22%3A%22visitor%22%2C%22variant%22%3A%22Control%22%2C%22country%22%3A%22USA%22%2C%22evar13%22%3A%22Control%22%7D%2C%22v2%22%3A1%2C%22v1%22%3A1%2C%22rid%22%3A%22d464cf8-84660044-129d-72f1-f9c0f%22%2C%22to%22%3A4.7%2C%22mid%22%3A%22d464cf8-84660194-61b1-0598-09be9%22%2C%22rt%22%3Afalse%2C%22rc%22%3Atrue%2C%22c%22%3A%22http%3A%2F%2Fallrecipes.com%2Frecipes%2F%22%2C%22pv%22%3A23%2C%22lc%22%3A%7B%22d2%22%3A%7B%22v%22%3A23%2C%22s%22%3Atrue%7D%7D%2C%22cd%22%3A2%2C%22f%22%3A1515141092373%2C%22sd%22%3A2%2C%22meta%22%3A%7B%22rtp%22%3A%22c%22%2C%22rta%22%3A1%2C%22rts%22%3A1%7D%2C%22l%22%3A%22en%22%2C%22i%22%3A-1%7D",
        },
        'DOWNLOAD_DELAY': 1
    }

    def start_requests(self):
        url = 'http://allrecipes.com/recipes/?page='
        for i in range(1, 3063):  # 3063
            yield scrapy.Request(url + str(i))

    def parse(self, response):
        s = Selector(text=response.text)
        urls = s.xpath('//section[@id="fixedGridSection"]/article[@class="fixed-recipe-card"]/a/@href').extract()
        for url in urls:
            list_url = urljoin(response.url, url)
            yield scrapy.Request(list_url, callback=self.parse_item)

    def parse_item(self, response):
        s = Selector(text=response.text)
        title = s.xpath('//h1[@class="recipe-summary__h1"]/text()').extract_first().strip()
        stars = s.xpath('//div[@class="recipe-summary__stars"]/div[@class="rating-stars"]/img/@src').extract()
        star_num = 0
        for star in stars:
            if 'full' in star:
                star_num += 1
            elif 'half' in star:
                star_num += 0.5
            else:
                continue
        made_it = re.search(r'init\((\d+),null\)', response.text).group(1)
        review_count = s.xpath('//span[@class="review-count"]/text()').re_first(r'\d+')
        picture_count = s.xpath('//span[@class="picture-count-link"]/format-large-number/@number').re_first(r'\d+')
        author = s.xpath('//span[@class="submitter__name"]/text()').extract_first()
        desc = s.xpath('//div[@class="submitter__description"]/text()').extract()
        descriptions = ''.join([d.strip() for d in desc if d]) if desc else ''
        pics = s.xpath('//ul[@class="photo-strip__items"]/li//img/@src').extract()
        pics = ['http'+p for p in pics if p] if pics else ''
        time = s.xpath('//span[@class="ready-in-time"]/text()').extract_first()
        servings = s.xpath('//div[@class="subtext"]/text()').re_first(r'\d+')
        nutrition = s.xpath('//li[@itemprop="calories"]/span/text()').extract_first()
        ingredients = s.xpath('//span[@class="recipe-ingred_txt added"]/text()').extract()
        pretime = s.xpath('//time[@itemprop="prepTime"]/span/text()').extract_first()
        cooktime = s.xpath('//time[@itemprop="cookTime"]/span/text()').extract_first()
        totaltime = s.xpath('//time[@itemprop="totalTime"]/span/text()').extract_first()
        directions = s.xpath('//span[@class="recipe-directions__list--item"]/text()').extract()

        item = AllrecipesItem()
        item['url'] = response.url
        item['title'] = title
        item['star_num'] = str(star_num)
        item['made_it'] = str(made_it)
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
        yield item
