from urllib.request import urlopen
url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)

import re
string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*?>", "ELEPHANTS", string)
string