#! --*--coding:utf-8--*--

# 生产者 消费者 queue  put message get message lpush rpop
# consumer1 ---> element1 
# consumer2 ---> element2
# lpush --- rpop

# 发布者 订阅者 redis subscribe publish
# subscriber1 ---> element1
# subscreber2 ---> element1
# subscribe --- publish

# Mongodb(nosql)    ---- mysql(sql)
# not only sql       # structual query language
# bson(binary json)(key:value)  # talbe (row column)


# database            database
# collection          talbe
# document            row
# field(域)           column(列/字段)
# index               index
# primary key(主键)   primary key
#                     table joins

# createCollection("collection1")    # create table table1 (c1 varchar(10));
# document1 vs document2 不同的field  # row1 vs row2 相同column
# _id 必须有 自动生成                  # id 可有可无

# ues database1
# db.dropdatabase()
# createCollection("table1")
# insert({})
# find().pretty()
# table1.drop()
# find({}) 
# table1.update({},{}) 
# table1.save({"_id"})
# db.table1.save({"filed0":8})

# remove:
# {"field0":9}  default :{justOne:false}
# {"field0":{$lt:10}} defualt:{justOne:true}

# find() find({"field0":value})
# and or
# db.table1.find({"f1":1,"f3":4}) and
# db.table1.find({$or:[{"f3":2},{"f3":4}]}) $or
# 
# 限定被检索的field(域)
# db.table1.find({"f1":1},{"f1":0,"f2":0}) 0：false 1:true
# db.table1.find({"f1":1},{"f1":1,"f2":1})

# db.table1.find({"f1":1},{"f1":1,"f2":0}) 错误的语法
#  "Projection cannot have a mix of inclusion and exclusion.",
# inclusion模式 1
# exclusion模式 0

# $type
# db.table1.find({"f1":{$type:2}})
# db.table1.find({"f1":{$type:"string"}})
# 非结构化的数据 filed 不同 type 不同
# 离散矩阵(mongodb)  mysql(非离散矩阵)
# hbase-hadoop:database:离散矩阵
# 离散矩阵:NLP:自然语言处理:自然语言本质上就是一种离散矩阵



# redis  memory harddisk
# mongodb harddisk map(memory)
# mongod.exe --dbpath "E:\Program Files\MongoDB\Server\4.0\data"               
# mysql  harddisk 