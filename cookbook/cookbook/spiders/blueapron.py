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
from cookbook.items import BlueapronItem


class MeishijieSpider(CrawlSpider):
    name = 'blueapron'
    allowed_domains = ['blueapron.com']
    start_urls = ['https://www.blueapron.com/cookbook']
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "zh-CN,zh;q=0.9,en;q=0.8",
            'cache-control': "no-cache",
            # 'cookie': "isMobileWeb=false; _sp_id.ce9f=5e8a91b56b880148.1515070049.1.1515070227.1515070049; site_tests=2906770709&2720250403&5017750724&5263410768&5288820639&5593050559&5654114109&NEW_MODAL_RANKING&pmc_delivery_schedule&live_chat&7662912568&cancellation_link_removal&7489351338&recipe_quickview_coming_soon&reactivation_copy&meal_reschedule&clickable_delivery_schedule_graphic&freshness_banner&expiring_credits_modal&miss_upcoming_order&pmc_account_experience&upcoming-second-box-email&8285656708&9739250177&hide-manage-link&9922611301&activationButtonExperiment&recipe-quick-tag&ratings-v2-zendesk&default-2p2&upcomingToggleLayoutExperiment&9834291889&8353667113&pmc-user-signup&limited-quantity-badge-test&9865259431&pmc-eight-choose-three-user-signup&user-login-landing-location&recipe-main-dish-photo&tips-from-users-button&inviteContactIntegrationExperiment&googleAutofillSignupExperiment&8608270290&specialty-tomatoes-badge-test&customer-favorite-badge-test&trending-badge-test&8605367479&eds-to-new-users&launchTabExperiment&cust-fave-campaign-badge-test&30-minute-meal-badge-test&android_reportIssue&streamlinedOnboardingExperiment&inviteGoogleContactIntegrationExperiment&2p2-invite-value&guestLaunchTabExperiment&one-pan-meal-badge-test&one-pot-meal-badge-test&sheet-pan-supper-badge-test&easy-clean-up-badge-test&hands-off-cooking-badge-test&thanksgiving-dish-badge-test&invitePromptExperiment&9424150238&ratings-v2&pushNotificationsPermissionExperiment&reportIssueExperiment&whole-30-badge-test&whole-thirty&9866333104&9873428064&price-raise-012018; _session_id=3369fc486948e9bef8d53b576a728576; optimizelyEndUserId=oeu1515070046961r0.5076603183317214; optimizelySegments=%7B%22214532990%22%3A%22direct%22%2C%22215107286%22%3A%22false%22%2C%22215334127%22%3A%22gc%22%2C%222078370004%22%3A%22true%22%2C%222144860797%22%3A%22true%22%7D; optimizelyBuckets=%7B%7D; isMobileWeb=false; _ga=GA1.2.675325512.1515070047; _gid=GA1.2.1523146944.1515070047; market_cart=0; recipe_newsletter_modal_seen=true; __qca=P0-1265567359-1515070049377; _iveuid=29b8e14b-2064-4946-91b8-b3749a0d08d9; show_donate_banner=true; site_test_participated=9870761125%2C9863749865%2C8630140967%2C9727880617; __zlcmid=kJh1MhEgqejCBG; _sp_ses.ce9f=*; _ivesct=2; __insp_wid=198116051; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cuYmx1ZWFwcm9uLmNvbS9jb29rYm9vaw%3D%3D; __insp_targlpt=UmVjaXBlcyAtIEJsdWUgQXByb24%3D; __insp_norec_sess=true; amplitude_idblueapron.com=eyJkZXZpY2VJZCI6IjEzZjFhYjFkLTI2Y2YtNDI1NS1hNGRjLTNhYzkzYWM3MjVlNVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTUxNTEyMDc5MDUwMywibGFzdEV2ZW50VGltZSI6MTUxNTEyMDk1Mjg2NiwiZXZlbnRJZCI6MjYsImlkZW50aWZ5SWQiOjI0LCJzZXF1ZW5jZU51bWJlciI6NTB9; traffic_source={\"utm_medium\":\"(none)\",\"utm_source\":\"direct\"}; _sp_id.ce9f=5e8a91b56b880148.1515070049.1.1515120953.1515070049; _uetsid=_uetb4685317; _iveses=!142,6NFZn28SSHOvjbd7TnGWjA,1515120953,$; __insp_slim=1515120953496",
            'upgrade-insecure-requests': "1",
        },
        'DOWNLOAD_DELAY': 1
    }

    def start_requests(self):
        url = 'https://www.blueapron.com/cookbook?page='
        for i in range(1, 72):
            yield scrapy.Request(url + str(i))

    def parse(self, response):
        s = Selector(text=response.text)
        urls = s.xpath('//div[@class="recipe-thumb col-md-4"]/a/@href').extract()
        for url in urls:
            yield scrapy.Request(urljoin(response.url, url), callback=self.parse_item)

    def parse_item(self, response):
        s = Selector(text=response.text)
        title = s.xpath('//h1[@class="ba-recipe-title__main"]/text()').extract_first().strip()
        sub_title = s.xpath('//h2[@class="ba-recipe-title__sub mt-10"]/text()').extract_first().strip()
        item_name = s.xpath('//div[@class="ba-info-list__item-name"]/text()').extract()
        if '\nTime\n' in item_name:
            time = s.xpath('//div[@class="ba-info-list__item-value"][1]/span/text()').extract_first()
        else:
            time = ''
        servings = s.xpath('//span[@itemprop="recipeYield"]/text()').extract_first()
        nutrition = s.xpath('//span[@itemprop="calories"]/text()').extract_first()
        descriptions = s.xpath('//p[@itemprop="description"]/text()').extract_first()
        likes = s.xpath('//span[@class="_5n6h _2pih"]/text()').extract_first()
        save = s.xpath('//span[@data-pin-log="button_pinit"]/text()').extract_first()
        li_tags = s.xpath('//li[@itemprop="ingredients"]')
        ingredients = []
        for li in li_tags:
            ingredient = li.xpath('.//text()').extract()
            ingredient = [ing.strip().replace('\n', ' ') for ing in ingredient if ing and ing != '\n']
            ingredient = ' '.join(ingredient)
            ingredients.append(ingredient)
        # ingredients = s.xpath('//li[@itemprop="ingredients"]/div[@class="non-story"]/span/text()').extract()
        # ingredients = [ing.replace('\n', ' ').replace('"', '') for ing in ingredients if ing]
        tools = s.xpath('//li[@itemprop="tools"]/a/text()').extract()
        tools = [to.strip() for to in tools if to]

        item = BlueapronItem()
        item['url'] = response.url
        item['title'] = title
        item['sub_title'] = sub_title
        item['time'] = time
        item['servings'] = servings
        item['nutrition'] = nutrition
        item['descriptions'] = descriptions
        item['likes'] = likes if likes else ''
        item['save'] = save if save else ''
        item['ingredients'] = json.dumps(ingredients, ensure_ascii=False)
        item['tools'] = json.dumps(tools, ensure_ascii=False)

        yield item
