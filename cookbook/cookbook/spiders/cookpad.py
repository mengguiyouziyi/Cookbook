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
from urllib.parse import urljoin
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from cookbook.items import CookpadItem


class MeishijieSpider(CrawlSpider):
    name = 'cookpad'
    allowed_domains = ['cookpad.com']
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "zh-CN,zh;q=0.9,en;q=0.8",
            'cache-control': "no-cache",
            # 'cookie': "cpb=00ts682p03834c65ddbcbfcf31d4e65491431c77423c5f8570; bid=00ts682p03834c65ddbcbfcf31d4e65491431c77423c5f8570; v=342-8138978-5098751; FVD=%7Bts+%272018-01-08+16%3A14%3A53%27%7D; country_code=US; ab_session=0.944272257034789; f_unique_id=436ab9c0-1717-4e95-b513-22b8d7190e37; country_suggestion_shown=1; _ga=GA1.2.1753732062.1515395695; _gid=GA1.2.2029256273.1515395695; payload_D=15326; _global_web_session=SllJNC96Q2xLbDN0Q2tNYll2Wk1uaVIrekpzbi9NTGhPLzgrMlFLU2RZQ0kwdVhlQ0hQdkk5UDlWY1d0ZURmanR3aHRqVVpRNEdObzZMdWlBakxpWGE2VXcreXpaM0NGdlRRRjFzSmdzZnI1UWNFdWllT2MxMVI3eGxRUU9GSWZJdUxjRWl0Q3hKRlo2SjRaTjFDUFN3PT0tLVNGcW1UNFlFTkQ0RVlxY2hJTzF2Tnc9PQ%3D%3D--46d06265aadfa0c59c7353abbbf457f9c4004c84",
            'if-none-match': "W/\"c2014b1d64c3a1133a503a67ba71c525\"",
            'upgrade-insecure-requests': "1",
        },
        'DOWNLOAD_DELAY': 1
    }

    def start_requests(self):
        url = 'https://cookpad.com/us?page='
        for i in range(1, 557):  # 3063
            yield scrapy.Request(url + str(i))

    def parse(self, response):
        s = Selector(text=response.text)
        urls = s.xpath('//div[@class="card feed__card"]/a[@class="link-unstyled"]/@href').extract()
        for url in urls:
            list_url = urljoin(response.url, url)
            yield scrapy.Request(list_url, callback=self.parse_item)

    def parse_item(self, response):
        s = Selector(text=response.text)
        title = s.xpath('//h1/text()').extract_first().strip()
        pic = s.xpath('//div[@class="tofu_image"]/img/@src').extract_first()
        likes = s.xpath('//span[starts-with(@id, "likes_count_recipe")]/text()').re_first(r'\d+')
        camera = s.xpath('//a[@class="link-unstyled field-group__hide"]/text()').re_first(r'\d+')
        description = s.xpath('//meta[@name="description"]/@content').extract_first()
        author_url = s.xpath('//a[@class="media__img link-unstyled"]/@href').extract_first()
        author_url = urljoin(response.url, author_url)
        author = s.xpath('//span[@itemprop="name"]/text()').extract_first()
        ing_tags = s.xpath('//div[@class="ingredient__details"]')
        ingredients = [''.join([t.strip() for t in tag.xpath('.//text()').extract() if t]) for tag in ing_tags if tag] if ing_tags else []
        # ingredients = s.xpath('//div[@class="ingredient__details"]//text()').extract()
        # ingredients = [ing.strip() for ing in ingredients if ing] if ingredients else []
        servings = s.xpath('//div[starts-with(@id, "serving_recipe")]/div/text()').extract_first()
        cook_time = s.xpath('//div[starts-with(@id, "cooking_time_recipe")]/div/text()').extract_first()
        instructions = s.xpath('//div[@itemprop="recipeInstructions"]/p/text()').extract()

        item = CookpadItem()
        item['url'] = response.url
        item['title'] = title
        item['pic'] = pic
        item['likes'] = likes
        item['camera'] = camera
        item['description'] = description
        item['author_url'] = author_url
        item['author'] = author
        item['ingredients'] = json.dumps(ingredients, ensure_ascii=False)
        item['servings'] = servings.strip() if servings else ''
        item['cook_time'] = cook_time.strip() if cook_time else ''
        item['instructions'] = json.dumps(instructions, ensure_ascii=False)
        yield item
