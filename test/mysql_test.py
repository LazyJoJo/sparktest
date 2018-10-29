#!/usr/bin/env python
# -*- coding:utf8 -*-
# TIME    :2018/6/29 9:59
# Author  :ZhengChengBin
# File    :mysql_test.py

import mysql.connector

import MySQLdb

db = MySQLdb.connect('localhost', 'root', '123456', 'test', charset='utf8')
cursor = db.cursor()

sql = """
        select * from users
"""
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
    id = row[0]
    name = row[1]
    name2 = row[2]

    print id, name, name2

# 表头信息
for field in cursor.description:
    print field[0]
db.close()
