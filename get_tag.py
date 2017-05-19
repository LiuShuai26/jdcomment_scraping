#-*- coding:utf-8 -*-

import requests
import re

def get_tag():
    url = "https://book.douban.com/tag/?view=cloud"

    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        html = r.text
        tags = re.findall("<td><a href=\"/tag/(.*?)\">", html)
        for tag in tags:
            print  tag
    except:
        print "爬取失败"

get_tag()