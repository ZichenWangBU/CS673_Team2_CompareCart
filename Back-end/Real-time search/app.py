"""
FILE_NAME:  ;
DATE: 10/17/2024 ;
"""
"""
# run.py
# 导入Flask
import os
import sys

from flask import Flask
from flask import request
from webSpider import getHTML

# 创建Flask应用对象
app = Flask(__name__)


# 路由route + 视图函数
# 使用route()装饰器告诉Flask什么样的URL能触发执行被装饰的函数
# index()函数就是被装饰的视图函数，它返回显示在用户浏览器中的信息
@app.route('/get_data')
def index():
    keyword = request.args.get("keyword", default='')
    return {'amazon': getHTML('https://www.amazon.com/-/zh/s?k=%s&page=2&qid=1727679681&ref=sr_pg_2' % keyword),
            'alibaba': getHTML('https://www.alibaba.com/trade/search?SearchText=%s' % keyword),
            'bestbuy': getHTML('https://www.bestbuy.ca/en-ca/search?search=%s' % keyword)}


if __name__ == '__main__':
    app.run(port=8000, debug=True, host='0.0.0.0')
"""

'''
#/get_data?keyword=
# run.py
# 导入Flask
import os
import sys

from flask import Flask
from flask import request
from webSpider import getHTML

# 创建Flask应用对象
app = Flask(__name__)


# 路由route + 视图函数
# 使用route()装饰器告诉Flask什么样的URL能触发执行被装饰的函数
# index()函数就是被装饰的视图函数，它返回显示在用户浏览器中的信息
@app.route('/get_data')
def index():
    keyword = request.args.get("keyword", default='')
    return {'amazon': getHTML('https://www.amazon.com/-/zh/s?k=%s&page=2&qid=1727679681&ref=sr_pg_2' % keyword),
            'bestbuy': getHTML('https://www.bestbuy.ca/en-ca/search?search=%s' % keyword),
            'alibaba': getHTML('https://www.alibaba.com/trade/search?SearchText=%s' % keyword)}


if __name__ == '__main__':
    app.run(port=8000, debug=True, host='0.0.0.0')
'''

# /get_data?keyword=

import os
import sys

from flask import Flask
from flask import request
from webSpider import getHTML

# 创建Flask应用对象
app = Flask(__name__)


# 路由route + 视图函数
# 使用route()装饰器告诉Flask什么样的URL能触发执行被装饰的函数
# index()函数就是被装饰的视图函数，它返回显示在用户浏览器中的信息
@app.route('/get_data')
def index():
    keyword = request.args.get("keyword", default='')

    return {
            #'amazon': getHTML('https://www.amazon.com/-/zh/s?k=%s&page=2&qid=1727679681&ref=sr_pg_2' % keyword),
            'bestbuy': getHTML('https://www.bestbuy.ca/en-ca/search?search=%s' % keyword),
            'alibaba': getHTML('https://www.alibaba.com/trade/search?SearchText=%s' % keyword),
            #'bestbuy': getHTML('https://www.bestbuy.ca/en-ca/search?search=%s' % keyword)
            }
    # alibabaDf = getHTML('https://www.alibaba.com/trade/search?SearchText=%s' % keyword)
    # bestbuyDf = getHTML('https://www.bestbuy.ca/en-ca/search?search=%s' % keyword)
    # amazonDf = getHTML('https://www.amazon.com/-/zh/s?k=%s&page=2&qid=1727679681&ref=sr_pg_2' % keyword)
    # amazonPriceDf = amazonDf['priceDf']
    # amazonStarDf = amazonDf['starDf']
    # amazonPriceRank = dfToList(amazonPriceDf)
    # amazonStarRank = dfToList(amazonStarDf)

    # alibabaPriceDf = alibabaDf['priceDf']
    # alibabaStarDf = alibabaDf['starDf']
    # alibabaPriceRank = dfToList(alibabaPriceDf)
    # alibabaStarRank = dfToList(alibabaStarDf)

    # bestbuyPriceDf = bestbuyDf['priceDf']
    # bestbuyStarDf = bestbuyDf['starDf']
    # bestbuyPriceRank = dfToList(bestbuyPriceDf)
    # bestbuyStarRank = dfToList(bestbuyStarDf)


"""
    return {
        #'amazonPriceRank' : amazonPriceRank,
        #'amazonStarRank': amazonStarRank,
        #'alibabaPriceRank': alibabaPriceRank,
        #'alibabaStarRank':  alibabaStarRank,
        #'bestbuyPriceRank': bestbuyPriceRank,
        #'bestbuyStarRank':  bestbuyStarRank,
        bestbuyDf,
        amazonDf,
        alibabaDf

            }

"""


def dfToList(df):
    rankList = []
    for i in range(df.shape[0]):
        dic = {
            'star': str(df.iloc[i, 0]),
            'commentNum': str(df.iloc[i, 1]),
            'price': str(df.iloc[i, 2]),
            'title': df.iloc[i, 3],
            'detailUrl': df.iloc[i, 4]
        }
        rankList.append(dic)
    return rankList


if __name__ == '__main__':
    app.run(port=8000, debug=True, host='0.0.0.0')
