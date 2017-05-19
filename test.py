#-*- coding:utf-8 -*-

import requests
import re


ISBNlist = []
bookurl = "https://book.douban.com/subject/1291204/"
try:
    r = requests.get(bookurl, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    html = r.text
    ISBN = re.search("<span class=\"pl\">ISBN:</span> (.*?)<br/>", html)
    print ISBN.group(1)
    ISBNlist.append(ISBN)
except:
    print "爬取失败"