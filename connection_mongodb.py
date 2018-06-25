# coding=utf-8

from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pymongo import *
import datetime
import json
import pandas
import celery


# from bson import json_util as jsonb

spark = SparkSession \
    .builder \
    .master('local') \
    .appName("myApp") \
    .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/mytest.mytest") \
    .config("spark.mongodb.output.uri", "mongodb://127.0.0.1/mytest.coll") \
    .getOrCreate()

sc = spark.sparkContext

# sqlc = SQLContext(sc)
# test_collection = sqlc.read.format("com.mongodb.spark.sql").options(uri="mongodb://127.0.0.1:27017",
#                                                                     database="mytest", collection="mytest").load()
# test_collection.printSchema()
# test_collection.first()

# people = spark.createDataFrame([("Bilbo Baggins",  50), ("Gandalf", 1000), ("Thorin", 195), ("Balin", 178),
#                                 ("Kili", 77), ("Dwalin", 169), ("Oin", 167), ("Gloin", 158), ("Fili", 82),
#                                 ("Bombur", None)], ["name", "age"])


# client = MongoClient('example.com',
#                       username='user',
#                       password='password')  #have usename and passwd

client = MongoClient('mongodb://127.0.0.1:27017/')  # not usename and passwd
db = client.mytest
collection = db.mytest
print collection.count()

# 删除
# collection.remove({'name':'mytest'})
# collection.remove({'author':'mike'})

# 插入数据
# post = {'author':'mike',
#         'text':'my first blog post!',
#         'tags':['mongodb','python','pymongo'],
#         'date': datetime.datetime.now()
#         }
# post_id = collection.insert_one(post).inserted_id
# data = [
#         {"name":"zhao","rank":"1"},
#         {"name":"qian","rank":"2"},
#         {"name":"sun","rank":"3"},
#         {"name":"li","rank":"4"},
#         ]
# collection.insert(data)

l = list(collection.find({}, {'_id': 0}))
df = spark.createDataFrame(l)
df.printSchema()
df.write.format("com.mongodb.spark.sql.DefaultSource").mode("append").save()

# collection.insert(l2)
# print collection.count()


# print(jsonb.dumps(list(db.user.find({"name": "wu"}))))
