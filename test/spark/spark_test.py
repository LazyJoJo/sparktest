#!/usr/bin/env python
# -*- coding:utf8 -*-
# TIME    :2018/6/29 15:34
# Author  :ZhengChengBin
# File    :spark_test.py


#失败
from pyspark.sql import *
spark = SparkSession \
    .builder \
    .master('local') \
    .appName("myApp") \
    .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/mytest.mytest") \
    .getOrCreate()

