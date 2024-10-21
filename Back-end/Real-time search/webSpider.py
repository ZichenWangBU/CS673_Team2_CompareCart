#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
FILE_NAME: webSpider ;
DATE: 2024/9/27 ;
"""
'''
import os
import re
import sys
import time

from DrissionPage import ChromiumPage, ChromiumOptions

currentDir = os.path.abspath(os.path.dirname(sys.argv[0]))
def getHTML(url):
    currentDir = r'D:\BU-2024fall\metcs-673-software engineer-20\backend-code\10.5Beta'
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
            print('amazon_data：', 'macbook',dic)

    elif 'walmart' in url:
        divs = page.eles('xpath://div[@data-testid="item-stack"]/div')
        for d in divs:
            dic = {}
            try:
                price = d.ele('xpath:.//div[@data-automation-id="product-price"]').text
            except:
                price = ''
            try:
                commentNum = d.ele('xpath:.//span[@data-testid="product-reviews"]').attr('data-value')
            except:
                commentNum = ''
    
            try:
                star = d.ele('xpath:.//span[@data-testid="product-ratings"]').attr('data-value')
            except:
                star = ''
            dic['star'] = star
            dic['commentNum'] = commentNum
            dic['price'] = price
            dataList.append(dic)
            print('沃尔玛的数据：', dic)
    elif 'target.com' in url:
        divs = page.eles('xpath://section/div/div')
        
        for d in divs:
            dic = {}
            try:
                star = d.ele('xpath:.//span[@data-test="ratings"]/div[@data-ref="rating-mask"]').attr('style')
                
                if star:
                    star = re.findall(r'\d+', star)[0]*0.01*5
                    
            except:
                star = ''
                
            try:
                price = d.ele('xpath:.//span[@data-test="current-price"]').text
                if price:
                    price = re.findall(r'\d+\.\d{1,2}', price)[0]
            except:
                price = ''
            
            try:
                commentNum = d.ele('xpath:.//span[@data-test="rating-count"]').text.replace(' reviews', '')
            except:
                commentNum = ''
            dic['star'] = star
            dic['commentNum'] = commentNum
            dic['price'] = price
            dataList.append(dic)
            print('target的数据：', dic)
    return dataList

def woerma(url):
    currentDir = r'F:\PersonalBankUIAutomaticTest\testCode\SPIDER\seleniumSpider'
    chromeDir = os.path.join(currentDir, 'Chrome')
    userDataPath = os.path.join(chromeDir, 'AutomationProfile')
    configFile = os.path.join(currentDir, 'config.txt')
    browserPath = os.path.join(chromeDir, 'chrome.exe')
    do1 = ChromiumOptions(read_file = False)
    do1.set_paths(local_port = int(9111), user_data_path = userDataPath, browser_path = browserPath, )
    page = ChromiumPage(do1)
    page.get(url)
    page.wait.doc_loaded()
    page.ele('xpath://input[@name="q"]').input('iphone')
    time.sleep(2)
    page.ele('xpath://button[@aria-label="Search icon"]').click(by_js = True)
    
if __name__ == '__main__':
    getHTML('https://www.amazon.com/-/zh/s?k=macbook&page=2&qid=1727679681&ref=sr_pg_2')
    # time.sleep(10)
    # getHTML('https://www.walmart.com/')
    # getHTML('https://www.target.com/s?searchTerm=iphone')
    # woerma('https://www.walmart.com/')

# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
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
    currentDir = r'D:\BU-2024fall\metcs-673-software engineer-20\backend-code\10.5Beta'
    chromeDir = os.path.join(currentDir, 'Chrome')
    userDataPath = os.path.join(chromeDir, 'AutomationProfile')
    configFile = os.path.join(currentDir, 'config.txt')
    browserPath = os.path.join(chromeDir, 'chrome.exe')
    do1 = ChromiumOptions(read_file=False)
    do1.set_paths(local_port=int(9111), user_data_path=userDataPath, browser_path=browserPath, )
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
                title = d.ele('xpath:.//h2//span').text
            except:
                continue
            try:
                star = d.ele('xpath:.//span[contains(@aria-label,"5 stars")]').attr('aria-label')
            except:
                star = ''
            try:
                price = d.ele('xpath:.//span[@class="a-price"]/span[1]').text
            except:
                price = ''

            try:
                commentNum = d.ele('xpath:.//span[contains(@aria-label, " 评级")]').attr('aria-label')
            except:
                commentNum = ''
            dic['star'] = star
            dic['commentNum'] = commentNum
            dic['price'] = price
            dic['title'] = title
            dataList.append(dic)
            print('amazon：', dic)

    elif 'bestbuy' in url:
        time.sleep(3)
        page.ele("xpath://button/span[text()='Show more']").click(by_js=True)
        divs = page.eles('xpath://div[contains(@class, "productsRow")]/div')
        for d in range(len(divs)):

            title = divs[d].ele('xpath:.//div[@itemprop="name"]').text
            price = divs[d].ele('xpath:.//div[contains(@class, "style-module_price")]').text
            try:
                star = divs[d].ele('xpath:.//meta[@itemprop="ratingValue"]').attr('content')
            except:
                star = ''
            try:
                commentNum = divs[d].ele('xpath:.//meta[@itemprop="reviewCount"]').attr('content')
            except:
                commentNum = ''
            dic = {}
            dic['star'] = star
            dic['commentNum'] = commentNum
            dic['price'] = price
            dic['title'] = title
            dataList.append(dic)
            print('bestbuy：', dic)
    elif 'alibaba' in url:
        divs = page.eles('xpath://div[@data-content="abox-ProductNormalList"]/div')
        for d in range(len(divs)):

            title = divs[d].ele('xpath:.//h2//span').text
            price = divs[d].ele('xpath:.//div[@class="search-card-e-price-main"]').text
            try:
                star = divs[d].ele('xpath:.//span[@class="search-card-e-review"]/strong[1]').text
            except:
                star = ''
            try:
                commentNum = divs[d].ele('xpath:.//span[@class="search-card-e-review"]/span[1]').text
            except:
                commentNum = ''
            dic = {}
            dic['star'] = star
            dic['commentNum'] = commentNum
            dic['price'] = price
            dic['title'] = title
            dataList.append(dic)
            print('alibaba：', dic)
    return dataList


def woerma(url):
    currentDir = r'd:\pythonProject\SPIDER\seleniumSpider'
    chromeDir = os.path.join(currentDir, 'Chrome')
    userDataPath = os.path.join(chromeDir, 'AutomationProfile')
    configFile = os.path.join(currentDir, 'config.txt')
    browserPath = os.path.join(chromeDir, 'chrome.exe')
    do1 = ChromiumOptions(read_file=False)
    do1.set_paths(local_port=int(9111), user_data_path=userDataPath, browser_path=browserPath, )
    page = ChromiumPage(do1)
    page.get(url)
    page.wait.doc_loaded()
    divs = page.eles('xpath://div[@data-content="abox-ProductNormalList"]/div')
    for d in range(len(divs)):

        title = divs[d].ele('xpath:.//h2//span').text
        price = divs[d].ele('xpath:.//div[@class="search-card-e-price-main"]').text
        try:
            score = divs[d].ele('xpath:.//span[@class="search-card-e-review"]/strong[1]').text
        except:
            score = ''
        try:
            commentNum = divs[d].ele('xpath:.//span[@class="search-card-e-review"]/span[1]').text
        except:
            commentNum = ''
        print('title:%s,price:%s,score:%s,comment:%s' % (title, price, score, commentNum))


def woerma2(url):
    currentDir = r'd:\pythonProject\SPIDER\seleniumSpider'
    chromeDir = os.path.join(currentDir, 'Chrome')
    userDataPath = os.path.join(chromeDir, 'AutomationProfile')
    configFile = os.path.join(currentDir, 'config.txt')
    browserPath = os.path.join(chromeDir, 'chrome.exe')
    do1 = ChromiumOptions(read_file=False)
    do1.set_paths(local_port=int(9111), user_data_path=userDataPath, browser_path=browserPath, )
    page = ChromiumPage(do1)
    page.get(url)
    page.wait.doc_loaded()
    time.sleep(3)
    page.ele("xpath://button/span[text()='Show more']").click(by_js=True)
    divs = page.eles('xpath://div[contains(@class, "productsRow")]/div')
    for d in range(len(divs)):

        title = divs[d].ele('xpath:.//div[@itemprop="name"]').text
        price = divs[d].ele('xpath:.//div[contains(@class, "style-module_price")]').text
        try:
            score = divs[d].ele('xpath:.//meta[@itemprop="ratingValue"]').attr('content')
        except:
            score = ''
        try:
            commentNum = divs[d].ele('xpath:.//meta[@itemprop="reviewCount"]').attr('content')
        except:
            commentNum = ''
        print('title:%s,price:%s,score:%s,comment:%s' % (title, price, score, commentNum))


def bestpay(url):
    currentDir = r'd:\pythonProject\SPIDER\seleniumSpider'
    chromeDir = os.path.join(currentDir, 'Chrome')
    userDataPath = os.path.join(chromeDir, 'AutomationProfile')
    configFile = os.path.join(currentDir, 'config.txt')
    browserPath = os.path.join(chromeDir, 'chrome.exe')
    do1 = ChromiumOptions(read_file=False)
    do1.set_paths(local_port=int(9111), user_data_path=userDataPath, browser_path=browserPath, )
    page = ChromiumPage(do1)
    page.get(url)
    page.wait.doc_loaded()
    time.sleep(3)
    page.ele("xpath://button/span[text()='Show more']").click(by_js=True)
    divs = page.eles('xpath://div[contains(@class, "productsRow")]/div')
    for d in range(len(divs)):

        title = divs[d].ele('xpath:.//div[@itemprop="name"]').text
        price = divs[d].ele('xpath:.//div[contains(@class, "style-module_price")]').text
        try:
            score = divs[d].ele('xpath:.//meta[@itemprop="ratingValue"]').attr('content')
        except:
            score = ''
        try:
            commentNum = divs[d].ele('xpath:.//meta[@itemprop="reviewCount"]').attr('content')
        except:
            commentNum = ''
        print('title:%s,price:%s,score:%s,comment:%s' % (title, price, score, commentNum))


if __name__ == '__main__':
    getHTML('https://www.amazon.com/-/zh/s?k=macbook&page=2&qid=1727679681&ref=sr_pg_2')
    # # time.sleep(10)
    # # getHTML('https://www.walmart.com/')
    # # getHTML('https://www.target.com/s?searchTerm=iphone')
    woerma('https://www.alibaba.com/trade/search?SearchText=iphone')
    # url = 'https://www.bestbuy.ca/en-ca/search?search=iphone'
    # woerma2(url)


