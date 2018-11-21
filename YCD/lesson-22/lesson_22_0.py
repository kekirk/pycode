#! --*--coding:utf-8--*--
# string 
# key 
# hash   hset hmset m:multi scan cursor hlen
# List   lpush left push  rpush right push llen
#        lpush 1 2 3 blpop 3 2 1   先进后出 brpop 先进先出
#        queue put 1 2 3 get 1 2 3 先进先出
#        凡是能用数据库解决的问题，千万不要写代码\
#        blpop (nil) lpop (nil) 
# set    spop diff 差 inter 交 union 并 ismember 子 scard
# zset   zcard zcout zlexcount 
# row column
# hash dict {"k1":v1,"k2":v2} 
# 序列化 redis key_value
# mysql = {c1:r1,c2:r2}

# table id k v
# 1 mysql {c1:r1,c2:r2}

# 数据库 集群 oracle 
# java_web session memory
# 分布式的应用 session （分布式缓存击穿）