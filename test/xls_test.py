#!/usr/bin/env python
# -*- coding:utf8 -*-
# TIME    :2018/7/5 9:06
# Author  :ZhengChengBin
# File    :xls_test.py


import pandas as pd
import numpy as np

df = pd.read_excel(u'C:\\Users\zcb\Desktop\RGOS平台资质表.xlsx', encoding='utf8', index_col=None, usecols=(0, 13),
                   header=0, skipfooter=0, na_values='1.0')  #
df.set_axis(['name', 'score'], axis='columns', inplace=True)

# df1 = df.reindex(index = range(134),columns = ['name','score'])
# print df

df1 = df[(df['name'] == 'Na')]
# print df1

df1 = df[:20]

# df1 = df.dropna(subset=['name','score'])
# print df1

df1.to_json(u'C:\\Users\zcb\Desktop\RGOS平台资质表.json', orient='index')
# df = pd.read_json(u'C:\\Users\zcb\Desktop\RGOS平台资质表.zip',orient ='index',compression='zip')
# print df.count()

reader = pd.read_json(u'C:\\Users\zcb\Desktop\\test_records.json', orient='records', lines=True, chunksize=4)
df = pd.concat(reader, ignore_index=True)
print df

df.to_csv(u'C:\\Users\zcb\Desktop\\test_records.csv', header=True, index=True, encoding='utf8')
reader = pd.read_csv(u'C:\\Users\zcb\Desktop\\test_records.csv', header=0, index_col=0, encoding='utf8',
                     chunksize=4)
df = pd.concat(reader, ignore_index=True)
print df

writer = pd.ExcelWriter('C:\\Users\zcb\Desktop\\test_records.xlsx')
df1.to_excel(writer, 'Sheet1', index=False)
writer.save()

# reader = pd.read_csv('data/servicelogs', iterator=True)
# try:
#     df = reader.get_chunk(100000000)
# except StopIteration:
#     print "Iteration is stopped."
df = pd.DataFrame(np.arange(12).reshape(3, 4))
df1 = pd.DataFrame(np.arange(15).reshape(3, 5))
df2 = df[:2].append([df1, ],ignore_index=True)  # ignore_index=True也是重新生成index索引
print df2
