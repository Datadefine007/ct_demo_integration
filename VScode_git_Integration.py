# Databricks notebook source
from pyspark.sql.types import StructType,StructField, StringType, IntegerType
data2 = [("James","","Smith","36636","M",3000),    ("Michael","Rose","","40288","M",4000),    ("Robert","","Williams","42114","M",4000),    ("Maria","Anne","Jones","39192","F",4000),    ("Jen","Mary","Brown","","F",-1)  ]
schema = StructType([ \
    StructField("firstname",StringType(),True), \
    StructField("middlename",StringType(),True), \
    StructField("lastname",StringType(),True), \
    StructField("id", StringType(), True), \
    StructField("gender", StringType(), True), \
    StructField("salary", IntegerType(), True) \
  ]) 
df = spark.createDataFrame(data=data2,schema=schema)
# df.printSchema()
df.display()


a=[i for i in range(1,11)]
d1=0
for i in range(len(a)):
    d1+=a[i]
print(d1)



d2="aeiou"
d1=list(d2)
d4=" ajay singh jadoun"
for i in d1:
  if i in d1:
    print(i,end="")