from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

website = "https://www.thesun.co.uk/sport/football/"
chromepath = r"C:\Users\clone\Documents\chromedriver\chromedriver.exe"

webservice = Service(executable_path=chromepath)
driver = webdriver.Chrome(service=webservice)
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
df_headlins.to_csv('headline.csv')
driver.quit()