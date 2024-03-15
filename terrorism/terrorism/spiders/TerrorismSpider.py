import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import time
from datetime import datetime as dt

# for errors handling 
import sys
import logging as l

class TerrorismSpider(scrapy.Spider):
    name = 'terrorism'
    start_urls = ['https://rewardsforjustice.net']
    url = 'https://rewardsforjustice.net/index/?jsf=jet-engine:rewards-grid&tax=crime-category:1070%2C1071%2C1073%2C1072%2C1074'
    terrorismurls = []
    def __init__(self, name=None, **kwargs):
        super(TerrorismSpider, self).__init__(name, **kwargs)
        options = Options()
        # options.add_argument("--headless")
        service = Service(executable_path='C:\\Users\\Mukesh\\Downloads\\chromedriver.exe')
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()

    def page_init(self, url):
        """Initilize the url in browser"""
        try:
            self.driver.get(url)
            time.sleep(2)
        except Exception as e:
            # this will print the error on consol with error generating line no.
            print("___________________ ERROR ____________________")
            print(e)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            message = str(exc_type) + str(exc_obj) + ' At line no : ' + str(exc_tb.tb_lineno)
            l.error(message)
            self.driver.quit()

    def terrorurls(self):
        self.driver.execute_script("window.scrollBy(0,1600)","") 
        time.sleep(5)
        response = scrapy.Selector(text=self.driver.page_source)
        time.sleep(2)
        urls = self.driver.find_elements(by=By.XPATH, value='//div[@class="jet-engine-listing-overlay-wrap"]//a')
        for link in urls:
            self.terrorismurls.append(link.get_attribute("href"))
        
    def paginationurls(self):
        try:
            while self.driver.find_element(by=By.XPATH, value='//div[@class="jet-filters-pagination"]//div[@data-value="next"]'):
                self.terrorurls()
                self.driver.find_element(by=By.XPATH, value='//div[@class="jet-filters-pagination"]//div[@data-value="next"]').click()
                break    #remove it when complete
        except:
                pass
        time.sleep(5)
        self.terrorurls()
    
    def parse(self, response):
        try:
            self.page_init(self.url)
            self.paginationurls()

            for terrorurl in self.terrorismurls[0:2]:   #remove it when complete
                self.page_init(terrorurl)

                pageurl = terrorurl 
                category = 'null'
                try:
                    title =  self.driver.find_element(by=By.XPATH, value='//div[@id="hero-col"]//h2').text
                except:
                    title = 'null'
                try:
                    reward_amount = self.driver.find_element(by=By.XPATH, value='//div[@id="reward-box"]//div[@class="elementor-widget-wrap elementor-element-populated"]/div[2]//h2').text
                except:
                    reward_amount = 'null'
                try:
                    reward_amount = reward_amount.replace("Up to ", "")
                except:
                    reward_amount = 'null'
                
                try:
                    about = self.driver.find_element(by=By.XPATH, value='//div[@id="reward-about"]').text
                except:
                    about = 'null'
                
                lenrewads= len(self.driver.find_elements(by=By.XPATH, value='//*[@id="reward-fields"]/div/div'))
                
                for num in range(1,lenrewads+1):
                    print(f"$$$$$$$$$$$$${num}$$$$$$$$$$$$$$")
                    # image heading
                    try:
                        heading = self.driver.find_element(by=By.XPATH, value=f'//*[@id="reward-fields"]/div/div[{num}]/div/h2').text
                    except:
                        pass
                    # image url
                    if 'images' in heading.lower(): 
                        value = self.driver.find_element(by=By.XPATH, value='//*[@id="gallery-1"]/figure/div/a')
                        value = value.get_attribute("href")
                    else:
                        value = "null"

                    if 'date of birth' in heading.lower():
                        try:
                            dob = self.driver.find_element(by=By.XPATH, value=f'//*[@id="reward-fields"]/div/div[{num+1}]/div').text
                        except:
                            pass
                        break
                    else:
                        dob = "null"
                
                reqdata= {
                    "pageUrl": pageurl,
                    "title": title,
                    "reward_amount": reward_amount,
                    "about" : about
                }
            
                print("--------------------------")
                print(dob)
                print('--------------------------')
            self.driver.quit()

        except Exception as e:
            print("___________________ ERROR ____________________")
            print(e)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            message = str(exc_type) + str(exc_obj) + \
                ' At line no : ' + str(exc_tb.tb_lineno)
            l.error(message)
            self.driver.quit()