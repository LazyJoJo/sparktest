# -*- coding: utf-8 -*- #设置默认编码格式
from pyspark.sql import SparkSession
SPARK_HOME = "C:/spark/spark-2.3.0-bin-hadoop2.6/"
spark = SparkSession \
    .builder \
    .master("local") \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
