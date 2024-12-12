import mechanicalsoup
import urllib.parse
import re
import io

#def Chapter:


def mybase_url(url, with_path=False):
    parsed = urllib.parse.urlparse(url)
    path   = '/'.join(parsed.path.split('/')[:-1]) if with_path else ''
    parsed = parsed._replace(path=path)
    parsed = parsed._replace(params='')
    parsed = parsed._replace(query='')
    parsed = parsed._replace(fragment='')
    return parsed.geturl()

#function to browse url and save to a file
def save_chapter_content(url, chaptertitle,savefilepath):
    chapterpage = browser.get(url)
    title = chapterpage.soup.find_all("h1")[0].get_text()
    content = chapterpage.soup.find_all("div", {"class":"tjc-cot"})    
    contentstring = content[0].get_text(separator="\n", strip=True) # /? match zeor or one of /
    savefile = extractpath + "\\" + fname + ".txt" 
    file1 = io.open(savefilepath, mode="a", encoding="utf-8")
    file1.write("\r\n" + " - "*50)
    file1.write("\r\n\r\n## " + chaptertitle + "\r\n") # use char # to be easily convert txt to epub as markdown format
    file1.write(contentstring)
    file1.close()
    return savefile

# 1
browser = mechanicalsoup.Browser()
base_url = "https://www.jinshuzhijia.com"
index_url = "https://www.jinshuzhijia.com/index.php/book/info/daoyutai"
index_page = browser.get(index_url)
chapter_list = index_page.soup.find_all("li",{"itemprop":"name"})

for chapter in chapter_list:
    print(f'{base_url}{chapter.a.get("href")} - {chapter.a.get_text()}')
    newurl = base_url + chapter.a.get("href")
    save_chapter_content(newurl, chapter.a.get_text())