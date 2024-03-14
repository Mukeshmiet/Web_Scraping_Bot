import scrapy
import time
from datetime import datetime as dt

# for errors handling 
import sys
import logging as l

class TerrorismSpider(scrapy.Spider):
    name = 'terrorism'
    start_urls = ['https://www.google.com']
    url = 'https://rewardsforjustice.net/index/?jsf=jet-engine:rewards-grid&tax=crime-category:1070%2C1071%2C1073%2C1072%2C1074'
    product_url = []
    req_info = []

    def parse(self):
        try:
            print("Time")

        except Exception as e:
            print("___________________ ERROR ____________________")
            print(e)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            message = str(exc_type) + str(exc_obj) + \
                ' At line no : ' + str(exc_tb.tb_lineno)
            l.error(message)
