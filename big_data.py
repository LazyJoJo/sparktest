#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    :2018/6/25 14:06
# @Author  :ZhengChengBin
# @File    :big_data.py

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
print df[0:3]  # out 前三行
# loc[data,columns]
print df.loc[dates[0:4]]  # out columns和前4行数据 通过index获取数据
print df.loc[:, ['A', 'B']]  # out index,A,B的所有数据
df.at[dates[0], 'A']  # 访问特定值
# iloc[list,list] 前面是行，后面是列，0:2，只有0,1两行或两列
df.iloc[2:4, 0:2]  # 第三第四行，index，第一第二列
df.iloc[[1, 2, 4], [0, 2]]  # 2,3,5行，index，1,3列
df.iloc[1, 1]  # 某个值
df.iat[1, 1]  # 和上面一行相同效果
df[df.A > 0]  # 筛选条件
print df[df > 0]
df2 = df.copy()
df2['E'] = ['one', 'two', 'three'] * 2  # add column
print df2
df2[df2['E'].isin(['two', 'three'])]  # 筛选E中为‘two','three'的数据

s1 = pd.Series(range(1, 7), index=pd.date_range('20130102', periods=6))  # 自动对准index，没有就为NaN
print s1
df['F'] = s1
df.iat[0, 0] = 0
df.iat[0, 1] = 0
df.loc[:, 'D'] = np.array([5] * len(df))
print df
df2 = df.copy()
print df2
df2[df2 > 0] = -df2  # 所有值都为负值,这里只改变了>0的值
print df2

df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1], 'E'] = 1
df1.dropna(how='any')  # 删除任何带有Na的数据
df1.dropna(how='all')  # 删除所有字段都是Na的数据
df1.dropna(subset=['E', 'A'])  # 删除子列中带有Na的数据
df1.dropna(thresh=4)  # 只保留至少有4个非NA值的行

df1 = df.copy()
df1.fillna(value=5)  # 将NA值赋值为5
values = {'A': 1, 'B': 2}
df1.fillna(value=values)  # 给每一列的空值设置默认值

print df.mean(1)  # 行的平均值
print df.mean()  # 列的平均值

s = pd.Series([1, 3, 4, np.nan, 6, 8], index=dates).shift(2)  # 沿着index平移2个单元

print s
print df.sub(s, 'index')  # df中的值减去s中的值，如果s中为NA则整行为空，每一列都要减

# 对数据应用函数
df.apply(lambda x: x.max() - x.min())  # 对每一列数据使用相同的操作，reduce操作，将每列或每行的所有元素（多-》1）

s = pd.Series(np.random.randint(0, 7, size=10))  # 10个0~6的随机数
print s.value_counts()  # 按照s的值计算每个值的个数

df = pd.DataFrame(np.random.randn(5, 4), index=range(5), columns=list('1234'))
pieces = [df[:3], df[3:7], df[7:]]
pd.concat(pieces)  # =df  将这些行拼接在一起
left = pd.DataFrame({'key': ['foo', 'dd', 'dd'], 'value': [1, 2, 3]})
right = pd.DataFrame({'key': ['foo', 'dd', 'dd'], 'value': [4, 5, 6]})
print pd.merge(left, right, on='key')  # 全连接

df = pd.DataFrame(np.random.randn(8, 4), columns=list('ABCD'))
s = df.iloc[3]  # 编号为3的
df.append(s, ignore_index=True)  # 添加一条数据

df = pd.DataFrame({
    'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
    'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
    'C': np.random.randn(8),
    'D': np.random.randn(8)
})
print df
df.groupby('A').sum()  # 分组求和
df.groupby(['A', 'B']).sum()

tuples = list(zip(['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
                  ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']))
print tuples  # 相当于把两列表示的数据拆成每行表示[('bar', 'one'), ('bar', 'two'),
# ('baz', 'one'), ('baz', 'two'), ('foo', 'one'), ('foo', 'two'), ('qux', 'one'), ('qux', 'two')]

index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
print df
print df.iloc[0]  # name,A,B,其中name为tuple
stacked = df.stack()  # 表格形式变成花括号形式 stacked类型变成series
stacked.unstack(level=-1)  # 花括号变成表格，层级默认是最里面那层-1，最外层应该是0

pd.pivot_table(df, values=[],index=[],columns=[],fill_value=0 ) #具体看印象笔记例子

