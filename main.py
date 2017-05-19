#-*- coding:utf-8 -*-

import requests
import re
from get_ISBN import get_ISBN
from get_jdnum import get_jdnum
from get_jdcm import get_jdcm


def main():
    tags = ['科普']
    ISBNlist = []
    jdnums = []
    for tag in tags:
        ISBNlist = get_ISBN(tag=tag)
        for ISBN in ISBNlist:
            jdnums = get_jdnum(ISBN=ISBN)
            for jdnum in jdnums:
                get_jdcm(pid=jdnum)


if __name__ == "__main__":
    main()