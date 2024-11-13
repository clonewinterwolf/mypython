# beauty_soup.py

from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
#print(soup.get_text())
print(soup.find_all("img"))
image1,image2 = soup.find_all("img")
print(image1.name)

base_url = "http://olympus.realpython.org"
url = base_url + "/profiles"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

for link in soup.find_all("a"):
    link_url = base_url + link["href"]
    print(link_url)