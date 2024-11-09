import os
import re
import sys
import time
import pandas
import requests
from DrissionPage import ChromiumPage, ChromiumOptions
import firebase_admin
from firebase_admin import credentials, firestore

# 初始化 Firebase
cred = credentials.Certificate("C:/Users/wyf20/CS673_Team2_CompareCart/Back-end/Real-time search/cs673comparecart-firebase-adminsdk-8la2o-84029a7194.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

currentDir = os.path.abspath(os.path.dirname(sys.argv[0]))


def getHTML(url):
    currentDir = r'C:/Users/wyf20/CS673_Team2_CompareCart'
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

    df = pandas.DataFrame()
    if 'amazon' in url:
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
                detailUrl = d.ele('xpath:.//h2//a').attr('href')

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
            dic = {}
            dic['star'] = [star]
            dic['commentNum'] = [commentNum]
            dic['price'] = [price]
            dic['title'] = [title]
            dic['detailUrl'] = [detailUrl]
            # tmpDf = pandas.DataFrame(data=dic)
            # df = pandas.concat([tmpDf, df], axis=0)
            dic['store']=['amazon']
            db.collection("Items").add(dic)
            print('amazon：', dic)
            print(imgPath)


    elif 'bestbuy' in url:
        time.sleep(2)
        page.ele("xpath://button/span[text()='Show more']").click(by_js=True)
        time.sleep(2)
        page.scroll.to_top()
        time.sleep(2)
        divs = page.eles('xpath://div[contains(@class, "productsRow")]/div')
        bestbuyDir = os.path.join(currentDir, 'bestbuy')
        if not os.path.exists(bestbuyDir):
            os.mkdir(bestbuyDir)
        for d in range(len(divs)):
            page.actions.move_to(ele_or_loc=divs[d])
            time.sleep(1)
            title = divs[d].ele('xpath:.//div[@itemprop="name"]').text
            price = divs[d].ele('xpath:.//div[contains(@class, "style-module_price")]').text
            price = float(price.replace('$', '').replace(',', ''))
            imgUrl = divs[d].ele('xpath:.//img').attr('src')
            imgName = re.sub(rstr, "_", title)
            imgPath = os.path.join(bestbuyDir, imgName + '.jpg')
            imgRes = myRequests(imgUrl)
            if imgRes:
                with open(imgPath, 'wb') as f:
                    f.write(imgRes.content)
            detailUrl = divs[d].ele('xpath:.//a').attr('href')
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
            dic = {}
            dic['star'] = [star]
            dic['commentNum'] = [commentNum]
            dic['price'] = [price]
            dic['title'] = [title]
            dic['detailUrl'] = [detailUrl]
            dic['store']=['bestbuy']
            # tmpDf = pandas.DataFrame(data=dic)
            # df = pandas.concat([df, tmpDf], axis=0)
            db.collection("Items").add(dic)
            print('bestbuy：', dic, d)
    elif 'alibaba' in url:
        divs = page.eles('xpath://div[@data-content="abox-ProductNormalList"]/div')
        alibabaDir = os.path.join(currentDir, 'alibaba')
        if not os.path.exists(alibabaDir):
            os.mkdir(alibabaDir)
        for d in range(len(divs)):

            title = divs[d].ele('xpath:.//h2//span').text
            price = divs[d].ele('xpath:.//div[@class="search-card-e-price-main"]').text
            price = re.findall('(?<=\$)\d+.\d{2}', price.replace(',', ''))[0]
            price = float(price)
            imgUrl = divs[d].ele('xpath:.//img[contains(@class,"search-card-e-slider")]').attr('src')
            imgName = re.sub(rstr, "_", title)
            imgPath = os.path.join(alibabaDir, imgName + '.jpg')
            imgRes = myRequests(imgUrl)
            if imgRes:
                with open(imgPath, 'wb') as f:
                    f.write(imgRes.content)
            detailUrl = divs[d].ele('xpath:.//h2/preceding-sibling::a').attr('href')

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
            dic = {}
            dic['star'] = [star]
            dic['commentNum'] = [commentNum]
            dic['price'] = [price]
            dic['title'] = [title]
            dic['detailUrl'] = [detailUrl]
            dic['store']=['alibaba']
            # tmpDf = pandas.DataFrame(data=dic)
            # df = pandas.concat([df, tmpDf], axis=0)
            db.collection("Items").add(dic)
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
    getHTML('https://www.amazon.com/-/zh/s?k=macbook&page=2&qid=1727679681&ref=sr_pg_2')
    getHTML('https://www.alibaba.com/trade/search?SearchText=iphone')
    getHTML('https://www.bestbuy.ca/en-ca/search?search=iphone')