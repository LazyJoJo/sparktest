#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    :2018/6/25 14:06
# @Author  :ZhengChengBin
# @File    :test3.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1, 3, 4, np.nan, 6, 8])  # NaN -> null
# Series can accept dist
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))  # 返回6*4的矩阵
# randn正态分布随机数

dist1 = {'A': 1.,
         'B': pd.Timestamp('20130102'),
         'C': pd.Series(1, index=list(range(5)), dtype='float32'),
         'D': np.array([3] * 5, dtype='int32'),
         'E': pd.Categorical(["test", "train", "test", "train", 'zcb']),
         'F': 'foo'}
# categorical 类别，取值必须是类别中的值，否则为NaN
# a,b,f列会自动补齐，其他必须定义相同的行数
df2 = pd.DataFrame(dist1)
df3 = pd.DataFrame({'a': [1, 2], 'b': [2, 3], 'd': (2, 3)})
print df2.dtypes
# DataFrame 好像是按列赋值的
# DataFrame(data, index,columns) data 不包含索引列，index 索引列 ，columns 其他列名称

df.index
df.columns
df.values
df.describe()  # 基本数据统计值描述
df.T  # 转置矩阵

df.sort_index(axis=1, ascending=False)  # axis开启对columns进行排序，ascending表示逆序
df.sort_values(by='B', ascending=False)  # 对b列进行排序，逆序
df['A']  # out index,A
df[0:3]  # out index,A,B,C,D
# loc[data,columns]
print df.loc[dates[0:4]]  # out columns和前4行数据
print df.loc[:, ['A', 'B']]  # out index,A,B的所有数据
df.at[dates[0], 'A']  # 访问特定值
# iloc[list,list] 前面是行，后面是列，0:2，只有0,1两行或两列
df.iloc[2:4, 0:2]  # 第三第四行，index，第一第二列
df.iloc[[1, 2, 4], [0, 2]]  # 2,3,5行，index，1,3列
df.iloc[1, 1]  # 某个值
df[df.A > 0]  # 筛选条件
print df[df > 0]
df2 = df.copy()
print df2.index.size
df2['E'] = ['one', 'two', 'three'] * 2  # add column
print df2
df2[df2['E'].isin(['two', 'three'])] # 筛选E中为‘two','three'的数据


