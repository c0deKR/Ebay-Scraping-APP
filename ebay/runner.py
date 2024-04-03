import scrapy  
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.ItemScraper import ItemscraperSpider

process = CrawlerProcess(settings=get_project_settings())
process.crawl(ItemscraperSpider)
process.start()