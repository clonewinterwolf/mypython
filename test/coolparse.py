from lib2to3.pgen2.token import OP
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import pandas as pd
import os
import sys
from datetime import datetime

application_path = os.path.dirname(sys.executable)

website = "https://www.cool18.com/bbs4/index.php?app=forum&act=threadview&tid=14277626"
chromepath = r"C:\Users\clone\Documents\chromedriver\chromedriver.exe"

#headless-mode
weboptions = Options()
weboptions.headless = True

webservice = Service(executable_path=chromepath)
driver = webdriver.Chrome(service=webservice, options=weboptions)
driver.get(website)
containers = driver.find_elements(by="xpath", value='Pre')
containers
