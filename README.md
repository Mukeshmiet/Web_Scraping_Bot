# Web_Scraping_Bot
penguin international Data Engineer assessment test

This scraping bot created using python scrapy and selenium.

This bot scrape data from the website "rewardsforjustice.net"

This bot scrape Terrorism page url, category, title, rewards amount, associated organization(s), 
associated location(s), about, image url(s), and date of birth (in ISO date format).

this bot generated an json output file with file name as combination of spider name, date and time.
Ex: terrorism_20240402_135900.json (SpiderName_SpiderDate_SpiderTime.json)

## Instructions:

1. Clone the repo.
2. open TerrorismSpider.py file
3. At line no. 38 change executable_path with your chrome driver path
4. open terminal from terrorism folder
5. Run spider by typing "scrapy crawl terrorism" in terminal
6. after finishing crawling, it will generate a json file in terrorism folder