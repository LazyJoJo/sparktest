#!/usr/bin/env python
# -*- coding:utf8 -*-
# TIME    :2018/7/6 15:45
# Author  :ZhengChengBin
# File    :stock_test.py

import pandas as pd
import pandas_datareader.data as web
from pandas_datareader import wb

import pandas_datareader.fred
import datetime

# We will look at stock prices over the past year, starting at January 1, 2016
start = datetime.datetime(2010, 1, 1)
end = datetime.date.today()

# apple = web.DataReader('AAPL', 'morningstar', start, end)  # 苹果公司股价
# print(apple)
# msft = web.DataReader('MSFT', 'morningstar', start, end)  # 微软公司股价
# print msft
google = web.DataReader('GOOG', 'morningstar', start, end)  # google公司股价
print google

