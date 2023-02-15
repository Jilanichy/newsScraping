import scrapy
import pandas as pd
import csv
from scrapy.spiders import CrawlSpider, Spider


# global list to store all the news title and text
news_text = []


class YahooNewsSpider(scrapy.Spider):
    name = 'yahoo_news'
    start_urls = ['https://finance.yahoo.com/news/']


    def parse(self, response):

        # go to each link of yahoo finance news
        for link in response.css('li.js-stream-content h3 a::attr(href)'):
            yield response.follow(link, self.parse_news)


    def parse_news(self, response):
        
        # grabbing actual news title and text and appending on the global list
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