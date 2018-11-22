#db.ut1.aggregate([{$group:{_id:"$f1",f31:{$addToSet:"$f3"}}}])
# select f1,distinct(f3) from ut1 group by f1;db.ut1.aggregate([{$group:{_id:"$f1",f31:{$push:"$f3"}}}])

#db.ut1.aggregate([{$group:{_id:"$f1",f31:{$push:"$f3"}}}])
#select f1,f3 from ut1 order by f1;


# 管道操作

# ls | cat 

# $project

# db.ut1.aggregate([
# {$project:{f1:1,f3:1}},
# {$group:{_id:"$f1",max:{$max:"$f3"}}}
# ])

# db.ut1.aggregate([{$project:{f1:1,f3:1}},{$group:{_id:"$f1",max:{$max:"$f2"}}}])

# aggregate([{},{},{},{}])
# data stream
# hadoop(data stream)  sql:structual

# nosql 
# data type
# 增删改查
# index
# 高级查询 aggregate


# 监测工具
# mongostat operation
# mongotop I/O

# 监测命令
# db.currentOp()
# db.serverstatus()

# locks锁 (read lock+write lock)

# oracle 默认没有读锁；
# money = 1000
# select money from table1; 
# update table1 set money = 100;

# create index --> create index table
# read write

# 1000 documents
# insert({}) 100
# mongodb index 强制加锁
# backgroud:true 不长时间占用锁 vs backgroud:false 长时间占用锁
# db.finance.createIndex({"f3":1},{background:true})

# relationship 关系
# mysql oracle sqlite 关系型数据库

# table:student(student_id)
# table:score(math,chinese,english,science)
# table:address(family_address)

# 一对一:班级与班长之间的联系：
# 一个班级只有一个正班长
# 一个班长只在一个班中任职
# 一对多：班级与学生之间的联系：
# 一个班级中有若干名学生，
# 每个学生只在一个班级中学习
# 多对多：课程与学生之间的联系：
# 一门课程同时有若干个学生选修
# 一个学生可以同时选修多门课程

# 1:N
# 1:1
# N:1
# N:N

# 
# 有var就是局部变量，如果没有就是全局变量

# st1 = {name:1,students:1,id:Objectid()} json
# 在json当中，对象就是一种数据结构，函数就是一种数据类型;

# pickle.dumps() pickle.loads()
# json.dumps()   json.loads() <script>$.get(){
# loads(data)
# 
# } </script>


# mongodb集群 redis集群 mysql更详细
# python脚本操作数据库
# hbase hive python操作 （odbc+orm）

# 前端