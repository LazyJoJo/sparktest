#!/usr/bin/env python
# -*- coding:utf8 -*-
# TIME    :2018/7/5 17:27
# Author  :ZhengChengBin
# File    :user_twice_login.py

"""
用户上线时间统计
"""



import numpy as np
import pandas as pd
import datetime as dt

df = pd.read_excel('C:\Users\zcb\Desktop\\test.xlsx', index_col=0, dtype={'time': str, 'date': str})


def strts(x):
    """
    string to float
    """
    import time
    a = time.strptime(x, '%Y-%m-%d %H:%M:%S')
    return time.mktime(a)


def str2(x):
    """
    :param x:Series （上线和下线时间）
    :return: 用户在线时间
    """
    print x
    sum = 0
    count = 1
    for num in x:
        sum += num * (-1) ** count
        count += 1
    return sum


df2 = df.iloc[:, [0, 1]]
df3 = df2.dropna(how='any')
# print df3.info()

df3['time'] = df3['time'].apply(lambda x: strts(x))
print type(df3['time'])
df3 = df3.sort_values(['id','time'])
df4 = df3.groupby(['id'])['time'].agg([lambda x: str2(x)])
print(type(df4))
# print df3['<lambda>']
# df3 = df3.to_frame()
print df3
df3 = df3.groupby(['id','time'])['time'].agg(lambda x: str2(x)).unstack()
print type(df3)
# df3 = df3.to_frame(name=None)
print df3
# pd.to_datetime(x, format='%Y/%m/%d')

df2 = df.iloc[:, [2,3]]
df2 = df2.groupby(['date', 'status']).size().unstack()
print type(df2)
# print df2
