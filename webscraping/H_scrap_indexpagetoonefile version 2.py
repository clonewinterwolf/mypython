import mechanicalsoup
import urllib.parse
import re
import io
import os
import random, string

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
def save_chapter_content(url, fname, extractpath = 'C:\\Users\\clone\\Documents\\github\\mypython\\webscraping\\捣玉台test'):
    chapterpage = browser.get(url)
    title = chapterpage.soup.find_all("h1")[0].get_text()
    content = chapterpage.soup.find_all("div", {"class":"tjc-cot"})    
    contentstring = content[0].get_text(separator="\r\n", strip=True) # /? match zeor or one of /
    savefile = extractpath + "\\" + fname + ".txt" 
    file1 = io.open(savefile, mode="a", encoding="utf-8")
    file1.write(contentstring)
    file1.close()
    return savefile

#function to browse url and save to a file
def save_chapter_content_tofile(url, chaptertitle,savefilepath):
    chapterpage = browser.get(url)
    title = chapterpage.soup.find_all("h1")[0].get_text()
    content = chapterpage.soup.find_all("div", {"class":"grap"}) #change this name based on web.  
    contentstring = content[0].get_text(separator="\r\n", strip=True) # /? match zeor or one of /
    file1 = io.open(savefilepath, mode="a", encoding="utf-8")
    file1.write("\r\n" + " - "*50)
    file1.write("\r\n\r\n## " + chaptertitle + "\r\n") # use char # to be easily convert txt to epub as markdown format
    file1.write(contentstring)
    file1.close()
    return savefilepath

# 1
#book_rootpath = "H:\\Ebooks\\Huangshu\\古典\\"
book_rootpath = "H:\\Ebooks\\Huangshu\\武侠\\"
browser = mechanicalsoup.Browser()
#base_url = "https://www.jinshuzhijia.com"
#index_url = "https://www.jinshuzhijia.com/index.php/book/info/wodetianxia" #the url of index page containing url of all chapters 
base_url = "https://shendiao.5000yan.com/"
index_url = "https://shendiao.5000yan.com" #the url of index page containing url of all chapters 


index_page = browser.get(index_url)
#book_title = index_page.soup.find_all("h3", attrs={"class":"post-title entry-title"})[0].get_text().replace("\n",'') #the first h1 should be the book title
#chapter_list = index_page.soup.find_all("h3", attrs={"class":"post-title entry-title"})[1:]

book_title = index_page.soup.find_all("h1")[0].get_text() #the first h1 should be the book title
chapter_list = index_page.soup.find_all("li",{"class":"p-2"})

subfolderpath = book_rootpath + book_title
book_filepath = subfolderpath + "\\" + book_title + ".txt"

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
    print(f'{chapter.a.get("href")} - {chapter.a.get_text()}')
    newurl = chapter.a.get("href")
    save_chapter_content_tofile(newurl, chapter.a.get_text(), book_filepath)