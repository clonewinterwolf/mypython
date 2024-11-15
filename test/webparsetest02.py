from lib2to3.pgen2.token import OP
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import pandas as pd
import os
import sys
from datetime import datetime

application_path = os.path.dirname(sys.executable)

website = "https://www.thesun.co.uk/sport/football/"
chromepath = r"C:\Users\clone\Documents\chromedriver\chromedriver.exe"

#headless-mode
weboptions = Options()
weboptions.headless = True

webservice = Service(executable_path=chromepath)
driver = webdriver.Chrome(service=webservice, options=weboptions)
driver.get(website)
containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')
titles = []
subtitles = []
links = []

for container in containers:
    title = container.find_element(by="xpath", value='./a/h2').text
    subtitle = container.find_element(by="xpath", value='./a/p').text
    link = container.find_element(by="xpath", value='./a').get_attribute("href")
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

my_dict = {'title':titles, 'subtitle':subtitles, 'link':links}
df_headlins = pd.DataFrame(my_dict)
df_headlins.to_csv('headline-headless.csv')
driver.quit()