# Version: 5.0.2 
# added support to onepage website
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

def get_base_url(url, with_path=False):
    parsed = urllib.parse.urlparse(url)
    path   = '/'.join(parsed.path.split('/')[:-1]) if with_path else ''
    parsed = parsed._replace(path=path)
    parsed = parsed._replace(params='')
    parsed = parsed._replace(query='')
    parsed = parsed._replace(fragment='')
    return parsed.geturl()


#function to browse url and save to a file
def save_chapter_content_tofile(url, chaptertitle, find_pattern, savefilepath):
    request_headers = { #header added to simulate web robot as chrome browser to prvent error 403 by WAF
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding' : 'gzip, deflate, sdch',
        'Accept-Language' : 'en-US,en;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    chapterpage = requests.get(url, headers=request_headers)
    chapterpage_soup = BeautifulSoup(chapterpage.content, 'html.parser')
    content = chapterpage_soup.find_all(find_pattern[0],find_pattern[1]) #change this name based on web.  
    contentstring = content[0].get_text(separator="\r\n", strip=True) # /? match zeor or one of /
    file1 = io.open(savefilepath, mode="a", encoding="utf-8")
    file1.write("\r\n" + " - "*50)
    file1.write("\r\n\r\n## " + chaptertitle + "\r\n") # use char # to be easily convert txt to epub as markdown format
    file1.write(contentstring)
    file1.close()
    return savefilepath

def find_chinese_di(text):
    # Regex pattern for Chinese characters (CJK Unified Ideographs)::
    find_chinese_di = re.compile(r'\u7b2c*')
    return find_chinese_di.findall(text)

def find_chinese_number(text):
    # Regex pattern for Chinese characters (CJK Unified Ideographs)
    find_chinese_di = re.compile(r'\u4e00-\u5341')
    return find_chinese_di.findall(text)

# 1 Custom variables for the book website

## ctrl+Shift+i in devopment tool. Idenity pattern of link to book chapters.   
# """
# # For website with no index page:  https://blog.xbookcn.net/2019/06/blog-post_94.html
# book_rootpath = "H:\\Ebooks\\Huangshu\\武侠\\"
# index_url = "https://blog.xbookcn.net/2019/05/blog-post.html" #the url of index page containing url of all chapters
# ## ctrl+Shift+i in devopment tool. Idenity pattern of book title. 
# title_tag = "h3"
# title_tag_attribute ={"class":"post-title entry-title" }

# chapther_tag = "" # set to "" if there is only one page
# chapter_attribute = {}
# chapter_find_pattern = ["div", {"class": "post-body entry-content","itemprop":"description articleBody"}] #set tag attributes of chapter content. div
# chinese_num_index = 1 # set to 0 if chapter name start with chinese digit number and 1 if start with 第
# chapter_link_ordered = True # if link is not ordered, set below variables
# """
#book_rootpath = "H:\\Ebooks\\Huangshu\\古典\\"
book_rootpath = "H:\\Ebooks\\Huangshu\\武侠\\"
index_url = "https://www.jinyongwang.net/ntian/" #the url of index page containing url of all chapters

## ctrl+Shift+i in devopment tool. Idenity pattern of book title. 
title_tag = "h1"
title_tag_attribute ={}

chapther_tag = "li" # set to "" if there is only one page
chapter_attribute = {}
chapter_contentfind_pattern = ["div", {"class":"vcon"}]  #set tag attributes of chapter content. div
chinese_num_index = 0 # set to 0 if chapter name start with chinese digit number and 1 if start with 第

chapter_link_ordered = True # if link is not ordered, set below variables
#--------------------------------------
chapter_startindex = 8 #index of the first　第一章
total_chapter = 39
total_chapter = 39
chapter_endindex = chapter_startindex + total_chapter
totalcol = 3
totalrow = round(total_chapter/totalcol)

#---------------------------------------------------------------------------------------------------------
base_url = get_base_url(index_url) #get base URL from book index url. 
#Use request instead of browser to avoid WAF 403 error. index_page = browser.get(index_url)
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
book_title = indexpage_soup.find_all(title_tag, title_tag_attribute)[0].get_text().replace('\n','') #the first h1 should be the book title
if len(chapther_tag) != 0: #one page no link to chapters.
    chapter_list = indexpage_soup.find_all(chapther_tag)
else:
    chapter_list = None
    
book_subfolderpath = book_rootpath + book_title
book_filepath = book_subfolderpath + "\\" + book_title + ".txt"

#create subfolder under book_rootpath
if os.path.exists(book_rootpath):
    if not os.path.exists (book_subfolderpath):
        print(f"Book folder path {book_subfolderpath} does not exist. Create book folder book_title")   
        os.mkdir(book_subfolderpath)
    else:
        print(f"Book folder path {book_subfolderpath} exists.")    
else: 
    print(f"Book Root path {book_rootpath} does not exist. Script terminated with error!!")
    quit()

#check whether book file exit. set book file name with random chars
if os.path.exists(book_filepath):
    char_set = string.ascii_uppercase + string.digits
    rndstring = ''.join(random.sample(char_set*6, 6))
    print (f"Book file path exist. Rename the file")
    book_filepath = book_subfolderpath + "\\" + book_title + "-" + rndstring + ".txt"

print(f">>> Start book scraping to file path {book_filepath} ...")
print(f">>>>>>> Chapter Link in sequence  order {chapter_link_ordered} ...")
chinese_numberchar_unicode = ['\u4e00','\u4e8c','\u4e09','\u56db','\u4e94','\u516d','\u4e03','\u516b','\u4e5d','\u5341','\u8bb0','\u91ca','\u540e','\u9644'] #chinese char,一...十,后记

if(chapter_link_ordered):
    if chapter_list is not None:
        for chapter in chapter_list:
            #第 \u7b2c 回\u56de
            #if (chapter.get_text()[0] in chr(ord('\u7b2c'))): #check whether the first chinese char is 第
            if (chapter.get_text()[chinese_num_index] in chinese_numberchar_unicode): #Change index to chapter.get_text()[1] if chapter title is  第一...
                if(base_url in chapter.a.get("href")):
                    chapter_url = chapter.a.get("href")
                else:
                    chapter_url = base_url + chapter.a.get("href")
                print(f'{chapter_url} - {chapter.a.get_text()}')
                save_chapter_content_tofile(chapter_url, chapter.a.get_text(), chapter_contentfind_pattern, book_filepath)
            else:
                print(f"No chinese numeric char found in chapter title {chapter.get_text()[chinese_num_index]}. skip.")
    else: #one page content
        chapter_url = index_url
        print(f'{chapter_url} - {book_title}')
        save_chapter_content_tofile(chapter_url,book_title, chapter_contentfind_pattern, book_filepath)
else:
    for index in range(0, totalrow):
        for j in range(0, totalcol):
            chapter_index = index + chapter_startindex + totalrow * j
            print(f"{index}+{chapter_startindex}+{(totalrow*j)}={chapter_index}")
            if ((chapter_index < chapter_endindex) and (chapter_list[chapter_index].get_text()[1] in chinese_numberchar_unicode)): #Change index to chapter.get_text()[1] if chapter title is  第一...
                print(f'{base_url}{chapter_list[chapter_index].a.get("href")} - {chapter_list[chapter_index].a.get_text()}')
                newurl = base_url + chapter_list[chapter_index].a.get("href")
                save_chapter_content_tofile(newurl, chapter_list[chapter_index].a.get_text(), chapter_contentfind_pattern, book_filepath)
            else:
                print("skipped")