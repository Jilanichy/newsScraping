import scrapy
import pandas as pd
import csv
import datetime
import logging

# global list to store all the news title and text
news_text = []


class YahooNewsSpider(scrapy.Spider):
    name = 'news_log'
    start_urls = ['https://finance.yahoo.com/news/']

    custom_settings = {
        'LOG_LEVEL': 'INFO'
    }

    def parse(self, response):
        for link in response.css('li.js-stream-content h3 a::attr(href)'):
            yield response.follow(link, self.parse_news)

    def parse_news(self, response):
        news = {
            'title': response.css('article.caas-container div.caas-title-wrapper h1::text').getall(),
            'text': ' '.join(response.css('p').xpath('.//text()').getall())
        }
        news_text.append(news)

    def closed(self, reason):
        # dataframe from the global news_text list
        df = pd.DataFrame(news_text, columns=['title', 'text'])

        #outputting csv
        df.to_csv('news.csv', index=False)

current_time = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
log_file = "scrapy_log_{}.txt".format(current_time)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(log_file)
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

process = scrapy.crawler.CrawlerProcess()
process.crawl(YahooNewsSpider)
process.start()
