#-*- coding:utf-8 -*-

import requests
import re

def get_jdcm(pid):
    page = 0
    while (1):
        print "Page %i ..." % (page + 1)
        url = "https://club.jd.com/comment/skuProductPageComments.action?productId=" + pid + "&score=0&sortType=3&page="+ str(page) + "&pageSize=10&isShadowSku=0&callback=fetchJSON_comment98vv7193"
        #https: // club.jd.com / comment / skuProductPageComments.action?productId = 11867803 & score = 0 & sortType = 3 & page = 2 & pageSize = 10 & isShadowSku = 0 & callback = fetchJSON_comment98vv7193
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        html = r.text
        comments = re.findall("\"content\":\"(.*?)\",\"creationTime\"", html)
        if not comments:
            print "over~!"
            break
        for comment in comments:
            print comment
        page += 1