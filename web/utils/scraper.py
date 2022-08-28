import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_djangoitem import DjangoItem
from multiprocessing import Process


from dashboard.models import News

class NewsItem(DjangoItem):
    django_model = News

class NewsPipeline(object):
    def process_item(self, item, spider):
        item.save()
        return item

class YandexNewsSpider(CrawlSpider):
    name = "yandex"
    allowed_domains = ['market.yandex.ru']
    start_urls = ['https://market.yandex.ru/partners/news']
    base_url = 'https://market.yandex.ru'

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//a[contains(@class, "news-list__item")]'), callback='parse_item'),
    )

    def parse_item(self, response):
        news_item = NewsItem()
        news_item['title'] = response.xpath('//div[contains(@class, "news-info__title")]/text()').get()
        news_item['text'] = response.xpath('//div[contains(@class, "news-info__post-body")]/p/text()').get()
        news_item['url'] = response.url
        tags = ['#yandex']
        tags += response.xpath('//a[contains(@class, "news-info__tag")]/text()').getall()
        news_item['tags'] = tags
        return news_item

def run_spider():
    process = CrawlerProcess(settings={
        "FEEDS": {
            "items.json": {"format": "json"},
        },
        "ITEM_PIPELINES" : {
            NewsPipeline: 300
        }
    })

    process.crawl(YandexNewsSpider)
    process.start()

def run_scraper():
    p = Process(target=run_spider)
    p.start()
    p.join()
