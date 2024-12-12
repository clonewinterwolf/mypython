# Test version that use user-agent to avoid 403 forbidden issue by WAF
# works well on website https://www.jinyongwang.net/. hit 403 error when using mechanicalsoup browser. 
# refer to https://docs.python.org/3/howto/unicode.html
from bs4 import BeautifulSoup
import urllib.parse
import re
import io
import os
import random, string
import requests

#def Chapter:

def base_url(url, with_path=False):
    parsed = urllib.parse.urlparse(url)
    path   = '/'.join(parsed.path.split('/')[:-1]) if with_path else ''
    parsed = parsed._replace(path=path)
    parsed = parsed._replace(params='')
    parsed = parsed._replace(query='')
    parsed = parsed._replace(fragment='')
    return parsed.geturl()


#function to browse url and save to a file
def save_chapter_content_tofile(url, chaptertitle,savefilepath):
    request_headers = { #header added to simulate web robot as chrome browser to prvent error 403 by WAF
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding' : 'gzip, deflate, sdch',
        'Accept-Language' : 'en-US,en;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    chapterpage = requests.get(url, headers=request_headers)
    chapterpage_soup = BeautifulSoup(chapterpage.content, 'html.parser')
    #title = chapterpage_soup.find_all("h1")[0].get_text()
    content = chapterpage_soup.find_all("div", {"class":"vcon"}) #change this name based on web.  
    contentstring = content[0].get_text(separator="\r\n", strip=True) # /? match zeor or one of /
    file1 = io.open(savefilepath, mode="a", encoding="utf-8")
    file1.write("\r\n" + " - "*50)
    file1.write("\r\n\r\n## " + chaptertitle + "\r\n") # use char # to be easily convert txt to epub as markdown format
    file1.write(contentstring)
    file1.close()
    return savefilepath

def find_chinese_di(text):
    # Regex pattern for Chinese characters (CJK Unified Ideographs)
    find_chinese_di = re.compile(r'\u7b2c*')
    return find_chinese_di.findall(text)

def find_chinese_number(text):
    # Regex pattern for Chinese characters (CJK Unified Ideographs)
    find_chinese_di = re.compile(r'\u4e00-\u5341')
    return find_chinese_di.findall(text)

# 1
#book_rootpath = "H:\\Ebooks\\Huangshu\\古典\\"
book_rootpath = "H:\\Ebooks\\Huangshu\\武侠\\"



base_url = "https://www.jinyongwang.net"
index_url = "https://www.jinyongwang.net/nshen" #the url of index page containing url of all chapters 
#index_page = browser.get(index_url)
request_headers = {
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding' : 'gzip, deflate, sdch',
    'Accept-Language' : 'en-US,en;q=0.8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(index_url, headers=request_headers)
indexpage_soup = BeautifulSoup(response.content, 'html.parser')
#book_title = index_page.soup.find_all("h3", attrs={"class":"post-title entry-title"})[0].get_text().replace("\n",'') #the first h1 should be the book title
#chapter_list = index_page.soup.find_all("h3", attrs={"class":"post-title entry-title"})[1:]

book_title = indexpage_soup.find_all("h1")[0].get_text() #the first h1 should be the book title
chapter_list = indexpage_soup.find_all("li")

subfolderpath = book_rootpath + book_title
book_filepath = subfolderpath + "\\" + book_title + ".txt"
chinese_num_index = 1 # set to 0 if chapter name start with chinese digit number and 1 if start with 第

#create subfolder under book_rootpath
if os.path.exists(book_rootpath):
    if not os.path.exists (subfolderpath):
        print(f"Book folder path {subfolderpath} does not exist. Create book folder book_title")   
        os.mkdir(subfolderpath)
    else:
        print(f"Book folder path {subfolderpath} exists.")    
else: 
    print(f"Book Root path {book_rootpath} does not exist. Script terminated with error!!")
    quit()

#check whether book file exit. set book file name with random
if os.path.exists(book_filepath):
    char_set = string.ascii_uppercase + string.digits
    rndstring = ''.join(random.sample(char_set*6, 6))
    print (f"Book file path exist. Rename the file")
    book_filepath = subfolderpath + "\\" + book_title + "-" + rndstring + ".txt"

print(f">>> Start book scraping to file path {book_filepath} ...")
for chapter in chapter_list:
    #print(f'{base_url}{chapter.a.get("href")} - {chapter.a.get_text()}')
    #newurl = base_url + chapter.a.get("href")
    #第 \u7b2c 回\u56de
    chinese_numberchar_unicode = ['\u4e00','\u4e8c','\u4e09','\u56db','\u4e94','\u516d','\u4e03','\u516b','\u4e5d','\u5341'] #chinese char,一...十
    #if (chapter.get_text()[0] in chr(ord('\u7b2c'))): #check whether the first chinese char is 第
    if (chapter.get_text()[chinese_num_index] in chinese_numberchar_unicode): #Change index to chapter.get_text()[1] if chapter title is  第一...
        print(f'{base_url}{chapter.a.get("href")} - {chapter.a.get_text()}')
        newurl = base_url + chapter.a.get("href")
        save_chapter_content_tofile(newurl, chapter.a.get_text(), book_filepath)