#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
FILE_NAME: startOBS ;
DATE: 2024/07/17 ;
"""

# run.py
import os
import sys

from flask import Flask
from flask import request
from webSpider import getHTML

app = Flask(__name__)


@app.route('/get_data')
def index():
    keyword = request.args.get("keyword", default = '')
    url = 'https://www.amazon.com/-/zh/s?k=%s&page=2&qid=1727679681&ref=sr_pg_2'%keyword
    return getHTML(url)
    

if __name__ == '__main__':
    app.run(port = 8000, debug = True, host = '0.0.0.0')



