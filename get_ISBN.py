#-*- coding:utf-8 -*-

import requests
import re

def get_ISBN(tag):
    num = 0
    urllist = []
    while (1):
        if (num > 180):
            break
        try:
            url = "https://book.douban.com/tag/" + tag + "?start=" + str(num) + "&type=T"
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            html = r.text
            list = re.findall("<a href=\"(.*?)\" title=\"", html)
            if not list:
                break
            urllist += list
        except:
            print "爬取失败"
        num += 20
    ISBNlist = []

    for bookurl in urllist:
        try:
            r = requests.get(bookurl, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            html = r.text
            ISBN = re.search("<span class=\"pl\">ISBN:</span> (.*?)<br/>", html)
            print ISBN.group(1)
            ISBNlist.append(ISBN.group(1))
        except:
            print "爬取失败"
