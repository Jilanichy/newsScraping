# Yahoo News Scraping

## Tools Used

<b>Tools:</b> Python, Scrapy, Pandas <br>

# Project Overview

* Scrape Yahoo finance News by going into each url.
* Utilize Pandas to process the data and output them in CSV / JSON format.
* Provide logs of crawled links, errors with timestamps.


# To Run the Project
First, create a virtual environment and activate it
```
python3 -m venv env && source env/bin/activate
```
Clone the project
```
git clone https://github.com/Jilanichy/newsScraping.git
```
cd into the directory
```
cd newsScraping
```
Then, install the requirements file
```
pip install -r requirements.txt
```
Then, run the "yahoo_news" spider to crawl and scrap the news
```
scrapy crawl yahoo_news
```
After that run the "news_log" to output the logs
```
scrapy crawl yahoo_news --logfile log.text
```
To find the full log
```
scrapy crawl yahoo_news --logfile log.text
```
