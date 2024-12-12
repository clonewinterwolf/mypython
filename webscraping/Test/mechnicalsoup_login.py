import mechanicalsoup
import urllib.parse

url = "https://www.cool18.com/bbs3/index.php?app=forum&act=threadview&tid=14357382"
browser = mechanicalsoup.StatefulBrowser()
browser.open(url)
print("before login")
print(browser.get_url())

browser.select_form('form[action="/pub_page/home_login.php"]')
browser["username"] = "kkkwolf"
browser["password"] = "hiHello123!@#"
print("after login:")
print(browser.get_url())


