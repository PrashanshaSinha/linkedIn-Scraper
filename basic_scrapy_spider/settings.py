
BOT_NAME = 'basic_scrapy_spider'

SCRAPEOPS_API_KEY = '8cdd6aa3-850b-4f45-a636-7b194e470668'

  
SCRAPEOPS_PROXY_ENABLED = True


DOWNLOADER_MIDDLEWARES = {
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
}


SPIDER_MODULES = ['basic_scrapy_spider.spiders']
NEWSPIDER_MODULE = 'basic_scrapy_spider.spiders'



# Obey robots.txt rules
ROBOTSTXT_OBEY = False

FEED_FORMAT = 'csv'
FEED_URI = 'linkedin_jobs.csv'  # Choose the name for your output CSV file

