#!/usr/bin/env python
# -*- coding: utf-8 -*-

from io import BytesIO
import os
import re
import sys
from time import sleep
import requests
from DrissionPage import ChromiumPage, ChromiumOptions
import firebase_admin
from firebase_admin import credentials, firestore,storage

# 初始化 Firebase
cred = credentials.Certificate("cs673comparecart-firebase-adminsdk-8la2o-c86686395c.json")

firebase_admin.initialize_app(cred, {
    'storageBucket': 'cs673comparecart.firebasestorage.app'
})
db = firestore.client()
bucket = storage.bucket()

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
        store_name='Amazon'
        divs = page.eles('xpath://div[@data-component-type="s-search-result"]')
        amazon_dir = os.path.join(currentDir, 'amazon')
        print('amazon', amazon_dir)
        if not os.path.exists(amazon_dir):
            os.mkdir(amazon_dir)
        for d in divs:
            try:
                title = d.ele('xpath:.//h2//span').text
                img_url = d.ele('xpath:.//img').attr('src')
                img_name = re.sub(rstr, "_", title)
                img_res = my_requests(img_url)
                image_data = BytesIO(img_res.content)
                blob = bucket.blob("item_image/" + img_name + '.jpg')
                blob.upload_from_file(image_data, content_type="image/jpeg")
                blob.make_public()
                img_blob_url = blob.public_url
            except:
                img_url=''
                img_blob_url=''
            try:
                detail_url = d.ele('xpath:.//h2//a').attr('href')
            except:
                detail_url=''
            try:
                star = d.ele('xpath:.//span[contains(@aria-label,"5 stars")]').attr('aria-label')
                star = float(re.findall(r'^\d\.\d(?= out of 5 stars)', star)[0])

            except:
                star = 0
            try:
                price = d.ele('xpath:.//span[@class="a-price"]/span[1]').text
                price = float(price.replace('$', ''))
            except:
                price = 0

            try:
                comment_num = d.ele('xpath:.//span[contains(@aria-label,"ratings")]').attr('aria-label')
                comment_num = comment_num[:-7]
            except:
                comment_num = 0
            dic = {'star': star, 'comment_num': comment_num, 'price': price, 'title': title,
                   'detail_url': detail_url,
                   'img_url': img_url, 'store': store_name, 'img_ref': img_blob_url}
            try:
                doc_to_add = db.collection("Items").document(title.replace("/", ""))
                doc_to_add.set(dic)
                print(store_name + ':', dic)
            except:
                continue

    elif 'bestbuy' in url:
        store_name='Bestbuy'
        sleep(2)
        page.ele("xpath://button/span[text()='Show more']").click(by_js=True)
        sleep(2)
        page.scroll.to_top()
        sleep(2)
        divs = page.eles('xpath://div[contains(@class, "productsRow")]/div')
        bestbuy_dir = os.path.join(currentDir, 'bestbuy')
        if not os.path.exists(bestbuy_dir):
            os.mkdir(bestbuy_dir)
        for d in range(len(divs)):
            page.actions.move_to(ele_or_loc=divs[d])
            sleep(1)
            try:
                title = divs[d].ele('xpath:.//div[@itemprop="name"]').text
            except:
                title=''
            try:
                price = divs[d].ele('xpath:.//div[contains(@class, "style-module_price")]').text
                price = float(price.replace('$', '').replace(',', ''))
            except:
                price = 0
            try:
                img_url = divs[d].ele('xpath:.//img').attr('src')
                img_name = re.sub(rstr, "_", title)
                img_res = my_requests(img_url)
                image_data = BytesIO(img_res.content)
                blob = bucket.blob("item_image/" + img_name + '.jpg')
                blob.upload_from_file(image_data, content_type="image/jpeg")
                blob.make_public()
                img_blob_url = blob.public_url
            except:
                img_url=''
                img_blob_url = ''
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
                comment_num = divs[d].ele('xpath:.//meta[@itemprop="reviewCount"]').attr('content')
                comment_num = float(comment_num)
            except:
                comment_num = 0
            dic = {'star': star, 'comment_num': comment_num, 'price': price, 'title': title,
                   'detail_url': detail_url,
                   'img_url': img_url, 'store': store_name, 'img_ref': img_blob_url}
            try:
                doc_to_add = db.collection("Items").document(title.replace("/", ""))
                doc_to_add.set(dic)
                print(store_name + ':', dic)
            except:
                continue

    elif 'alibaba' in url:
        store_name='Alibaba'
        divs = page.eles('xpath://div[@data-content="abox-ProductNormalList"]/div')
        alibaba_dir = os.path.join(currentDir, 'alibaba')
        if not os.path.exists(alibaba_dir):
            os.mkdir(alibaba_dir)
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
                img_url = divs[d].ele('xpath:.//img[contains(@class,"search-card-e-slider")]').attr('src')
                img_name = re.sub(rstr, "_", title)
                img_res = my_requests(img_url)
                image_data = BytesIO(img_res.content)
                blob = bucket.blob("item_image/" + img_name + '.jpg')
                blob.upload_from_file(image_data, content_type="image/jpeg")
                blob.make_public()
                img_blob_url = blob.public_url
            except:
                img_url=''
                img_blob_url = ''
            try:
                detail_url = divs[d].ele('xpath:.//h2/preceding-sibling::a').attr('href')
            except:
                continue
            try:
                star = divs[d].ele('xpath:.//span[@class="search-card-e-review"]/strong[1]').text
                star = float(star)
            except:
                star = 0
            try:
                comment_num = divs[d].ele('xpath:.//span[@class="search-card-e-review"]/span[1]').text
                comment_num = float(comment_num)
            except:
                comment_num = 0
            dic = {'star': star, 'comment_num': comment_num, 'price': price, 'title': title,
                   'detail_url': detail_url,
                   'img_url': img_url, 'store': store_name, 'img_ref': img_blob_url}
            try:
                doc_to_add = db.collection("Items").document(title.replace("/", ""))
                doc_to_add.set(dic)
                print(store_name + ':', dic)
            except:
                continue

def my_requests(img_url):
    try:
        img_res = requests.get(url=img_url, proxies={})
    except:
        img_res = ''
    return img_res

def collect_data(keyword):
    return {'amazon': getHTML('https://www.amazon.com/-/zh/s?k=%s&page=2&qid=1727679681&ref=sr_pg_2' % keyword),
            'alibaba': getHTML('https://www.alibaba.com/trade/search?SearchText=%s' % keyword),
            'bestbuy': getHTML('https://www.bestbuy.ca/en-ca/search?search=%s' % keyword)}

if __name__ == '__main__':
    collect_data('phone')
    collect_data('tablet')
    collect_data('laptop')
    collect_data('bottle')
    collect_data('floor+lamp')