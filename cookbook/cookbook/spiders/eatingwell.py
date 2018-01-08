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
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from cookbook.items import EatingwellItem


class MeishijieSpider(CrawlSpider):
    name = 'eatingwell'
    allowed_domains = ['eatingwell.com']
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'host': "www.eatingwell.com",
            'connection': "keep-alive",
            'cache-control': "no-cache",
            'upgrade-insecure-requests': "1",
            # 'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            'accept-encoding': "gzip, deflate",
            'accept-language': "zh-CN,zh;q=0.9,en;q=0.8",
            # 'cookie': "FirstImpression=False; ARSiteUser=1-b3719b1f-d63b-4eaa-b452-249d85a6fe4d; ARCompressedSession=KgcAAB+LCAAAAAAABAB9VduOokoU/RdfmY5ykUsn84AiigpeAAXeQAooKSiEQi6T+fdD2z1295yTk1RCau3N2mvf4NfIhHHuk7oEo9eRlSlp0cW4Dw4nkGy0SSFLtgRMrtWS9W28bWc5LiIjX+3GJn/hF9C8GkvilV4jozkCGVgtucWaK5l6IfZonzISy5vXVnEE9652IRy3S1T2JqnX5MgUmhqrS3Mr7m/rXllmziwQOrbb1DPaTVkxq+f0tUHTwNHGx9X6zqasJzrC4VTNbhefU6iFzbrHeZEWbDu3tG0X6gKPDJGrknjXMqJmOdhgDYhdVWJKpWChlFTT8b1JKc9CXYf2N8ueLdFWVj1pijNRSJs+SvcTeK3HV7W7JSQul5P67PMzWz8svA4YFKeudd25Os1W8VnWS0B/z1LL0nmH4atOqhUSLrQ+mqc7N4QiRnooHx372tguy+8bY9ZJgcI59HgPmHzaOPQ5d284CShBai/rCSeOlYNkDDXdrQKZrhvESbtTnS3mh74mC8Wm7DzcEKNx/TK7XSLpyhb6GMRXXe7jOCQtnBbqbcy4rs4ctML1NkpPhdViaS9XscftrHGrU5Quwv1Z6CiPzbaJ2K44p9VNYWk6hpsv6NjPnKDp610yv9ZackR9O2m2KWuFuu2x7vR8gcxY3s42nitNDbD35BOvx4ahts1qfZheGo4q2MJs0qTpVpWVhS6/RlrbWMvqrvJTvN4uzEjjBXiHZXrVlFmcixfxLHO2gs2W7nK7XNH+Xt3It7iZRmZ/QD3GmuMLRRIUjtKzYn23YIBbud5u9kogRKeFhpReOorTmRgBrZxWO83Z1EtdJTnVnyo/te61Q0vZXKoazzuV/nnRzA1OcNJasz2p2vCg65N2npzB4cr0HpocdtQ8s9RTN6Nc+eQBiJAi6NTaNOb3VZ4wVnlQo01jLksfew11nCfUYQ+paVQhQvQjkbQ2NbKikDxyMWXGZyabOiq0cbajxTsax5vVdrPaX9U09c+b/XXcnNU8IsqJD9od69jKRmBNIa3owjoW8s+fox+jOcYpBFoe4dHrr4/bsobhsLX0S8AKtBTQ0UvIs8ELB3z/JeCmzAvDSaE49fkIcOEnhzJ6nfwYaZVckwTkBF58AgaeyEcVeMO3OI5BqOVfoMEVDzD8ih2Hfc8CUOrgCdoVKD/oH95WV4DHbQVDsKoDEw3P8um+8qtEGyLnNUK/3yhVWFbEghk4wQoSPHiSsgZPi5YVJagqiPNPwxFcYAFmuNVxWCMg332I/AB9ajIACKt9Ce4QNEcQDQTJd5tZFwUuCcxj/ZGPSYbPYfW36yO1P9WvK4KzZ6oKrArkd4afgfdcfowW2SBDDsM3ud8wFZeZTx6vGaCpECAElDNIzDp7gPsSRxABLfPjJ9nfAqsEFg8Zfn4BCIFQGRr4x/ldm10iC6cgf8bOP5xGk8mEfnkcazJ5fZzRoxMzhOMv3V20BSy/jcUJlDCCIPy3Rb4QeAdfgKeyJzYUtST/I+H3Q4PlVwQMvYpACQaG6r8GawiX47zLcF19mwIc57D/EvGzVu8NHb3SQ5BdlsO3n93HgP2Zvv8wyEHwNjTvuzEa/f4HW1S4OioHAAA=; _ga=GA1.2.720961868.1515377996; _gid=GA1.2.632738190.1515377996; _cb_ls=1; _cb=BRcEjCDIoaWCDLOeFb; mt.v=2.490229108.1515377999027; mt.pc=2.1; mt.g.5c174d97=2.490229108.1515377999027; __ybotu=jc5kxp718e7tjizsdi; __gads=ID=b4ee3b4bcb1d44e1:T=1515378001:S=ALNI_MZcVVBy7uX6J-4GeVDiB3buMi216g; mt.session=t; mt.c-lbx=4; mt.INC_W=(RA_DIR_NTRG_P02_M068_MN_c710eram068bo:1); radius=20; zipCode=98101; ARToken=84XAr4Z2Z57+ieH6qwuIrano3gW7wvq9Wbo8Ssr9qwH8dSbdboTXM1SJDTYR9cNWRUAFWDrcHTQHlzB/wCe1/wGd9FtmBHy0k1REvzouuy4++ISDdcC278vRJtacFIKXHwBux059KKvkqRJbcInGm+6bO4hi7GgJ2mMLQP9sQ2a/go9YoAhYag==; _chartbeat2=.1515377996292.1515381958971.1.DZ4a39B6uIQTBl2sQ-BUK7rnBONg66; _cb_svref=null; session_depth=www.eatingwell.com%3D51%7C846313298%3D51; __ybotb=5076; __ybotv=1515381962913; __ybots=jc5nalyau8t13ta33l.0.jc5naly9ezryo2t0su.1; __ybotc=http%3A//ads-adseast-vpc.yldbt.com/m/; _gali=eatingWellAppId",
        },
        'DOWNLOAD_DELAY': 1
    }

    def start_requests(self):
        url = 'http://www.eatingwell.com/recipes/?page='
        for i in range(1, 345):  # 3063
            yield scrapy.Request(url + str(i))

    def parse(self, response):
        s = Selector(text=response.text)
        urls = s.xpath('//article[@class="gridCol--fixed-tiles"]/a/@href').extract()
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_item)

    def parse_item(self, response):
        s = Selector(text=response.text)
        pic = s.xpath('//img[@class="recipeDetailSummaryImageMain"]/@src').extract_first()
        title = s.xpath('//h3[@itemprop="name"]/text()').extract_first().strip()
        rate = s.xpath('//meta[@itemprop="ratingValue"]/@content').extract_first()
        review = s.xpath('//meta[@itemprop="reviewCount"]/@content').extract_first()
        submitter = s.xpath('//div[@class="recipeSubmitter"]/p/@title').extract_first()
        submitterLogo = s.xpath('//li[@class="submitterLogo"]/img/@src').extract_first()
        submitterTitle = s.xpath('//span[contains(@class, "submitterTitle")]/text()').extract_first()
        submitterRole = s.xpath('//span[contains(@class, "submitterRole")]/text()').extract_first()
        nutrition_profile = s.xpath('//span[@class="nutritionTag"]/a/text()').extract()
        ingredients = s.xpath('//span[@itemprop="ingredients"]/text()').extract()
        active = s.xpath('//time[@itemprop="prepTime"]/@datetime').extract_first()
        totalTime = s.xpath('//time[@itemprop="totalTime"]/@datetime').extract_first()
        step = s.xpath('//span[@class="recipeDirectionsListItem"]/text()').extract()

        item = EatingwellItem()
        item['url'] = response.url
        item['pic'] = pic
        item['title'] = title
        item['rate'] = rate
        item['review'] = review
        item['submitter'] = submitter
        item['submitterLogo'] = submitterLogo
        item['submitterTitle'] = submitterTitle
        item['submitterRole'] = submitterRole
        item['nutrition_profile'] = json.dumps(nutrition_profile, ensure_ascii=False)
        item['ingredients'] = json.dumps(ingredients, ensure_ascii=False)
        item['active'] = active
        item['totalTime'] = totalTime
        item['step'] = json.dumps(step, ensure_ascii=False)
        yield item
