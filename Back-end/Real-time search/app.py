"""
FILE_NAME:  ;
DATE: 10/17/2024 ;
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

#/get_data?keyword=