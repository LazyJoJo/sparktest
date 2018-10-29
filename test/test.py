# -*- coding: utf-8 -*- #设置默认编码格式
from pyspark.sql import SparkSession

# -----根据api编写-----
SPARK_HOME = "C:/spark/spark-2.3.0-bin-hadoop2.6/"
spark = SparkSession \
    .builder \
    .master("local") \
    .appName("myapp") \
    .getOrCreate()
# .enableHiveSupport()\
sc = spark.sparkContext
sc.setLogLevel("error")

# ==========createDataFrame(data, schema=None, samplingRatio=None, verifySchema=True)
l = [('Alice', 1)]
print spark.createDataFrame(l).collect()  # Creates a DataFrame from an RDD, a list or a pandas.DataFrame
print spark.createDataFrame(l, ['name', 'age']).collect()
d = [{'name': 'alice', 'age': 1}]  # out of time
spark.createDataFrame(d).collect()  # collect is order to out to list
rdd = sc.parallelize(l)
print spark.createDataFrame(rdd).collect()
df = spark.createDataFrame(rdd, ['name', 'age'])
print df.collect()

from pyspark.sql import Row

Person = Row('name', 'age')
person = rdd.map(lambda r: Person(*r))  # ‘*’ 可以自动解包， r 为整行数据，自动拆成每个元素给Person
df2 = spark.createDataFrame(person)
print df2.collect()

from pyspark.sql.types import *

schema = StructType([
    StructField('name', StringType(), True),
    StructField('age', IntegerType(), True)
])
df3 = spark.createDataFrame(rdd, schema)
print df3.collect()

# print spark.createDataFrame(df.toPandas()).collect()

# --------range---------------------------
print spark.range(1, 3, 4).collect()

print spark.range(3).collect()

# ----------read------------------as a DataFrame.
df = spark.read.json(SPARK_HOME + "examples/src/main/resources/people.json")
df.show()

# ----------readStream-------------as a streaming DataFrame
# df = spark.readStream

textFile = spark.read.text(SPARK_HOME + "examples/src/main/resources/people.txt")  # RDD
print textFile.count()
print textFile.first()
lines = textFile.filter(textFile.value.contains("Spark"))

# -------------sql-----------------
df.createOrReplaceTempView('table1')
df2 = spark.sql('select age as f1, name as f2 from table1')
print df2.collect()
df2 = spark.table('table1')
print sorted(df.collect()) == sorted(df2.collect())  # 排序后，比较是否相同

# 节选部分dataFrame  join
df2 = sc.parallelize([
    Row(name='Andy', height=178),
    Row(name='Michael', height=198),
    Row(name='Justin', height=188)
]).toDf()
print df.select('age', 'name').collect()
print df2.select('name', 'height').collect()
df4 = df.crossJoin(df2.select('height')).select('name', 'age', 'height')  # join
print df4.collect()

print df.join(df2, df.name == df2.name, 'inner').drop(df.name).collect()

df.describe(['age']).show()  # 会计算 count，mean，min,max等，最好不要放非数字类型的字段
df.distinct().count()  # 去重计数

# ==========

sc.stop()
