#! --*--coding:utf-8--*--

# virtual machine 8G 3G cpu+memory
# kvm 开源的虚拟化技术 
# 云计算 
# docker 进程


# $type bson

# Double	1	 
# String	2	 
# Object	3	 
# Array	4	        [a1,a2,a3,a4]       pyton:[2,"a",True]  
# Binary data	5	 
# Undefined	6	已废弃。
# Object id	7	 
# Boolean	8	 
# Date	9	 
# Null	10	 
# Regular Expression	11	 
# JavaScript	13	 
# Symbol	14	 
# JavaScript (with scope)	15	 
# 32-bit integer	16	 
# Timestamp	17	 
# 64-bit integer	18	 
# Min key	255	Query with -1.
# Max key	127	 

# https://docs.mongodb.com/manual/reference/bson-types/

# a = NumberInt(10);



# index 索引 (目录)
# index_table 


# table1
# c1 c2 c3 c4
# 
# ......100rows..........
# 
# 1  2  3  4
# 2  3  4  5
# 1  2  3  22
# 2  3  4  17
# 1  2  3  6
# 2  3  4  9
# 1  2  3  8
# 2  3  4  19
# 2  3  4  5

# c1 c4
# c1 1-->2
# select * from table1 where c1=2 and c4 = 5;
# c4 
# index
# 4-->5(rowid,rowid)
# 5-->22
# 17<--22
# 6<--17
# 17-->19
# 6-->9
# 8<--9
# select * from table1 where c4 = 5 and c1=2; (索引靠左);



# select * from table1 where c4 = 5;
# index(c4)
# tree_index

# index利弊
# 利: 快速查找
# 弊：数据更新慢

# redis 
# 表的拆分
# 1  2  3  4
# 2  3  4  5
# 1  2  3  22
# 2  3  4  17

# 1  2  3  6
# 2  3  4  9
# 1  2  3  8
# 2  3  4  19
# 2  3  4  5

# 对唯一值比较多的建立索引，主键索引比较多


# mongodb index : unique,expireAfterSeconds,name,weight

# 聚合操作
# db.ut.aggregate([{$group:{_id:"$f1",count:{$sum:1}}}])
# select f1,count(1) from ut group by f1

# db.ut.aggregate([{$group:{_id:"$f1",count:{$sum:"$f1"}}}])
# select f1,sum(f1) from ut group by f1

#  db.ut.aggregate([{$group:{_id:"$f1",count:{$sum:1},f1_sum:{$sum:"$f1"}}}])
# select f1,count(1),sum(f1) from ut group by f1