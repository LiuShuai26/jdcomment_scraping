#-*- coding:utf-8 -*-

import requests
import re

def get_jdnum(ISBN):
    searchurl = "https://search.jd.com/Search?keyword=9787550274259&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=" + ISBN + "&wtype=1&click=1"

    try:
        r = requests.get(searchurl, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        html = r.text
        jdnum = re.search("<a target=\"_blank\" href=\"//item.jd.com/(.*?).html\?dist=jd\"", html)
        print jdnum.group(1)
    except:
        print "爬取失败"