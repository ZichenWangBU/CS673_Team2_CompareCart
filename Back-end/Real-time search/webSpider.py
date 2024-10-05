#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
FILE_NAME: webSpider ;
DATE: 2024/9/27 ;
"""

import os
import re
import sys
import time

from DrissionPage import ChromiumPage, ChromiumOptions

currentDir = os.path.abspath(os.path.dirname(sys.argv[0]))
def getHTML(url):
    currentDir = r'address'
    chromeDir = os.path.join(currentDir, 'Chrome')
    userDataPath = os.path.join(chromeDir, 'AutomationProfile')
    configFile = os.path.join(currentDir, 'config.txt')
    browserPath = os.path.join(chromeDir, 'chrome.exe')
    do1 = ChromiumOptions(read_file = False)
    do1.set_paths(local_port = int(9111), user_data_path = userDataPath, browser_path = browserPath, )
    page = ChromiumPage(do1)
    page.get(url)
    page.wait.doc_loaded()
    time.sleep(5)
    page.scroll.to_bottom()
    dataList = []
    if 'amazon' in url:
        divs = page.eles('xpath://div[@data-component-type="s-search-result"]')

        for d in divs:
            dic = {}
            try:
                star = d.ele('xpath:.//span[contains(@aria-label,"5 stars")]').attr('aria-label')
            except:
                star = ''
            try:
                price = d.ele('xpath:.//span[@class="a-price"]/span[1]').text
            except:
                price = ''
                
            try:
                commentNum = d.ele('xpath:.//span[contains(@aria-label, " level")]').attr('aria-label')
            except:
                commentNum = ''
            dic['star'] = star
            dic['commentNum'] = commentNum
            dic['price'] = price
            dataList.append(dic)
            print('amazon_data：', dic)


    return dataList


    
if __name__ == '__main__':
    getHTML('https://www.amazon.com/-/zh/s?k=macbook&page=2&qid=1727679681&ref=sr_pg_2')
    #getHTML('https://www.amazon.com/s?k=ipone&crid=W1WVENW7PUJ3&sprefix=ipone%2Caps%2C89&ref=nb_sb_noss_2')
    # time.sleep(10)
    # getHTML('https://www.walmart.com/')
    # getHTML('https://www.target.com/s?searchTerm=iphone')
    # woerma('https://www.walmart.com/')






