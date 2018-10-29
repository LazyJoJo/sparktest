#!/usr/bin/env python
# -*- coding:utf8 -*-
# TIME    :2018/6/29 11:02
# Author  :ZhengChengBin
# File    :mongodb_test.py


from pymongo import MongoClient
import json, pandas as pd, time

# 带密码的格式
# client = MongoClient('example.com',
#                       username='user',
#                       password='password')  #have usename and passwd
client = MongoClient('127.0.0.1', 27017)  # 正常是不带密码的
client2 = MongoClient('mongodb://127.0.0.1:27017/')
# db = client['mytest']
db = client.mytest  # 数据库
collection = db.mytest  # 表（集合）
d = dict(name='dfd', age=20, score=80)
js = json.dumps(d)  # 转成json类型

# 删除
collection.remove({'name': 'zhao'})
# collection.remove({'author':'mike'})

# 插入数据
# post = {'author':'mike',
#         'text':'my first blog post!',
#         'tags':['mongodb','python','pymongo'],
#         'date': datetime.datetime.now()
#         }
# post_id = collection.insert_one(post).inserted_id
data = [
    {"name": "zhao", "rank": "1"}
    # ,
    #     {"name":"qian","rank":"2"},
    #     {"name":"sun","rank":"3"},
    #     {"name":"li","rank":"4"},
]
t1 = time.time()
for i in range(100000):  # 数据越大时间越多，成线性增长  写入4.48S/10000条
    for date in data:
        date['_id'] = i
    collection.insert(data)
t2 = time.time()  # 取出数据 0.11s /10000条
# collection.insert(js)
cursor = collection.find({}, {'_id': 0})
a = list(cursor)  # 不知道为何cursor使用完一次后就丢失，所以最好转成list

# for item in a:
#     print item  # IO处理很占用时间
#
# print len(a)
t3 = time.time()  # 转成dateframe也是成线性增长，0.016s/10000条
ng = pd.date_range('1/1/2018', periods=len(a), freq='D')
df = pd.DataFrame(a, index=ng)
t4 = time.time()
# print df

print (t4 - t3), (t3 - t2), (t2 - t1)
client.close()
client2.close()
