#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
FILE_NAME: webSpider ;
DATE: 2024/9/27 ;
"""
from random import random

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
                #commentNum = d.ele('xpath:.//span[contains(@aria-label, "rating")]').attr('aria-label')
                commentNum = d.ele('xpath:.//span[contains(@aria-label,"rating")]').attr('aria-label')
                commentNum = commentNum[:-7]
                #commentNum = d.ele('xpath:.//span[contains(@aria-label, " 评级")]').attr('aria-label')
                #commentNum = d.ele('xpath:.//span[@id="acrCustomerReviewText"]').text()
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
'''
import os
import re
import sys
import time
import pandas
import requests
from DrissionPage import ChromiumPage, ChromiumOptions

currentDir = os.path.abspath(os.path.dirname(sys.argv[0]))


def getHTML(url):
    currentDir = r'D:\pythonProject\SPIDER\seleniumSpider'
    chromeDir = os.path.join(currentDir, 'Chrome')
    userDataPath = os.path.join(chromeDir, 'AutomationProfile')
    browserPath = os.path.join(chromeDir, 'chrome.exe')
    do1 = ChromiumOptions(read_file=False)
    do1.set_paths(local_port=int(9111), user_data_path=userDataPath, browser_path=browserPath, )
    page = ChromiumPage(do1)
    page.get(url)
    page.wait.doc_loaded()
    page.scroll.to_bottom()
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'

    if 'amazon' in url:
        store = 'Amazon'
        divs = page.eles('xpath://div[@data-component-type="s-search-result"]')
        amazonDir = os.path.join(currentDir, 'amazon')
        print('amazon', amazonDir)
        if not os.path.exists(amazonDir):
            os.mkdir(amazonDir)
        for d in divs:
            try:
                title = d.ele('xpath:.//h2//span').text
                imgUrl = d.ele('xpath:.//img').attr('src')
                imgName = re.sub(rstr, "_", title)
                imgPath = os.path.join(amazonDir, imgName + '.jpg')
                imgRes = myRequests(imgUrl)
                if imgRes:
                    with open(imgPath, 'wb') as f:
                        f.write(imgRes.content)
                detail_url = d.ele('xpath:.//h2//a').attr('href')

            except:
                continue
            try:
                star = d.ele('xpath:.//span[contains(@aria-label,"5 stars")]').attr('aria-label')
                # star = d.ele('xpath:.//span[contains(@aria-label,"最多 5 颗星")]').attr('aria-label')
                star = float(re.findall(r'^\d\.\d(?= out of 5 stars)', star)[0])

            except:
                star = 0
            try:
                # price = d.ele('xpath:.//span[@class="a-price"]/span[1]').text
                price = d.ele('xpath:.//span[@class="a-price"]/span[1]').text
                price = float(price.replace('$', ''))
            except:
                price = 0

            try:
                # commentNum = d.ele('xpath:.//span[contains(@aria-label, " 评级")]').attr('aria-label')
                # commentNum = d.ele('xpath:.//span[contains(@aria-label, "rating")]').attr('aria-label')
                commentNum = d.ele('xpath:.//span[contains(@aria-label,"ratings")]').attr('aria-label')
                commentNum = commentNum[:-7]
                # commentNum = d.ele('xpath:.//span[contains(@aria-label, " 评级")]').attr('aria-label')
                # commentNum = d.ele('xpath:.//span[@id="acrCustomerReviewText"]').text()
            except:
                commentNum = 0
            dic = {'star': star, 'comment_num': commentNum, 'price': price, 'store': store, 'title': title,
                   'detail_url': detail_url}
            # tmpDf = pandas.DataFrame(data=dic)
            # df = pandas.concat([tmpDf, df], axis=0)

            print('amazon：', dic)
            print(imgPath)


    elif 'bestbuy' in url:
        store = 'Bestbuy'
        time.sleep(2)
        page.ele("xpath://button/span[text()='Show more']").click(by_js=True)
        time.sleep(2)
        page.scroll.to_top()
        time.sleep(2)
        divs = page.eles('xpath://div[contains(@class, "productsRow")]/div')
        bestbuyDir = os.path.join(currentDir, 'bestbuy')
        if not os.path.exists(bestbuyDir):
            os.mkdir(bestbuyDir)
        # for d in range(6):
        for d in range(len(divs)):
            page.actions.move_to(ele_or_loc=divs[d])
            time.sleep(1)
            try:
                title = divs[d].ele('xpath:.//div[@itemprop="name"]').text
            except:
                title = ''
            try:
                price = divs[d].ele('xpath:.//div[contains(@class, "style-module_price")]').text
                price = float(price.replace('$', '').replace(',', ''))
            except:
                price = 0

            try:
                imgUrl = divs[d].ele('xpath:.//img').attr('src')
                imgName = re.sub(rstr, "_", title)
                imgPath = os.path.join(bestbuyDir, imgName + '.jpg')
                imgRes = myRequests(imgUrl)
                with open(imgPath, 'wb') as f:
                    f.write(imgRes.content)
            except:
                imgUrl = ''
                imgName = ''
            try:
                detail_url = divs[d].ele('xpath:.//a').attr('href')
            except:
                continue
            try:
                star = divs[d].ele('xpath:.//meta[@itemprop="ratingValue"]').attr('content')
                star = float(star)
            except:
                star = 0
            try:
                commentNum = divs[d].ele('xpath:.//meta[@itemprop="reviewCount"]').attr('content')
                commentNum = float(commentNum)
            except:
                commentNum = 0
            dic = {'star': star, 'comment_num': commentNum, 'price': price, 'store': store, 'title': title,
                   'detail_url': detail_url}
            # tmpDf = pandas.DataFrame(data=dic)
            # df = pandas.concat([df, tmpDf], axis=0)
            print('bestbuy：', dic, d)
    elif 'alibaba' in url:
        store = 'Alibaba'
        divs = page.eles('xpath://div[@data-content="abox-ProductNormalList"]/div')
        alibabaDir = os.path.join(currentDir, 'alibaba')
        if not os.path.exists(alibabaDir):
            os.mkdir(alibabaDir)
        # for d in range(8):
        for d in range(len(divs)):

            try:
                title = divs[d].ele('xpath:.//h2//span').text
            except:
                continue
            try:
                price = divs[d].ele('xpath:.//div[@class="search-card-e-price-main"]').text
            except:
                continue
            price = re.findall('(?<=\$)\d+.\d{2}', price.replace(',', ''))[0]
            price = float(price)

            try:
                imgUrl = divs[d].ele('xpath:.//img[contains(@class,"search-card-e-slider")]').attr('src')
                imgName = re.sub(rstr, "_", title)
                imgPath = os.path.join(alibabaDir, imgName + '.jpg')
                imgRes = myRequests(imgUrl)
                with open(imgPath, 'wb') as f:
                    f.write(imgRes.content)
            except:
                imgUrl = ''
                imgName = ''
            try:
                '''
                link_element = divs[d].ele('xpath:.//h2/preceding-sibling::a')
                if link_element:
                    detailUrl=link_element.attr('href')
                    if detailUrl:
                        print(detailUrl)
                    else:
                        detailUrl = None
                        #return detailUrl

                else:
                    detailUrl = None
                '''

                # sleep(5)
                # sleep(random.randint(1,3))
                detail_url = divs[d].ele('xpath:.//h2/preceding-sibling::a').attr('href')
                # detailUrl = divs[d].ele('xpath:.//a').attr('href')
                # detailUrl = divs[d].ele('xpath://a[contains(@class='')]').attr('href')

            except:
                # detailUrl = None
                # raise
                continue

            try:
                star = divs[d].ele('xpath:.//span[@class="search-card-e-review"]/strong[1]').text
                star = float(star)
            except:
                star = 0
            try:
                commentNum = divs[d].ele('xpath:.//span[@class="search-card-e-review"]/span[1]').text
                commentNum = float(commentNum)
            except:
                commentNum = 0
            dic = {'star': star, 'comment_num': commentNum, 'price': price, 'store': store, 'title': title,
                   'detail_url': detail_url}
            # tmpDf = pandas.DataFrame(data=dic)
            # df = pandas.concat([df, tmpDf], axis=0)
            print('alibaba：', dic)
    # starDf = df.sort_values(by='star', ascending=False, inplace=False).head(5)
    # priceDf = df.sort_values(by='price', ascending=False, inplace=False).head(5)
    # print('starDf', starDf)
    # print('priceDf', priceDf)
    # return {'starDf': starDf, 'priceDf': priceDf}


def myRequests(imgUrl):
    try:
        # imgRes = requests.get(url=imgUrl, proxies={'https': '127.0.0.1:7890', 'http': '127.0.0.1:7890'})
        imgRes = requests.get(url=imgUrl, proxies={})

    except:
        imgRes = ''
    return imgRes


if __name__ == '__main__':
    # getHTML('https://www.amazon.com/-/zh/s?k=macbook&page=2&qid=1727679681&ref=sr_pg_2')
    getHTML('https://www.alibaba.com/trade/search?SearchText=tablet')
    # getHTML('https://www.bestbuy.ca/en-ca/search?search=tablet')
    # getHTML('https://www.alibaba.com/trade/search?SearchText=tablet')
