#! --*--coding:utf-8--*--


# setbit

# 用户登录统计

# 255 = 11111111

# login1 setbit 2 0 10111111
# login2 
# login3

# set user1_week1_login true
# set user1_week2_login true


# 持久化

# rdb 内存快照 

# save 900 1
# save 300 10
# save 60 60

# 弊端
# 60 >60  ---> saving 
# next saving (inner 60) set key value
# 上一次saving --- 下一次saving,中间的操作，如果server挂掉，中间操作的数据丢失


# aof 操作日志 append only file

# rdb aof

# rdb aof 弊端：中间操作的数据丢失
# aof rdb 弊端：rdb的io消耗比aof小,重启服务器，rdb加载内存的速度快，aof加载内存慢
# aof rdb 重启服务器，默认aof作为加载数据首选

# buffer set set set set 
# appendonly no #是否仅要日志
# appendfsync no # 系统缓冲,统一写,速度快
# appendfsync always # 系统不缓冲,直接写,慢,丢失数据少¶
# appendfsync everysec #折衷,每秒写1次

# appendfilename "masterappendonly.aof"


# set key7 10
# incr key7 ---- 执行1000次
# key7 1010

# rewrite aof文件重写

# set key7 1010 

# no-appendfsync-on-rewrite  yes: # aof重写时,要不要停止同步aof
# auto-aof-rewrite-percentage 100 #aof文件大小比起上次重写时的大小,增长率100%时,重写
# auto-aof-rewrite-min-size 64mb #aof文件,至少超过64M时,重写


# aof 上一次触发rewrite的时候，aof文件大小是3M,
# percentage 100 指的是当aof再次增加到6M的时候，再次触发重写

# 主从复合模式
# 星型
# 线型
# 图型 

# 星型   
# master---slave1
# master---slave2

# 线型
# master---slave1---slave2

# port 6379 mysql 3306



# 配置

# redis6380.conf
# redis6381.conf
# pid
# port
# dbfilename appendfilename
# slaveof master_ip master_port
# slave-read-only yes


# slaveof no one 快速切换master

# requirepass masterpasswd master
# masterauth masterpasswd slave


# auth passwd

# 一般情况，主从复合模式中，master不开启rdb,slave1开启rdb
# master开启aof,slave不开启aof

# master注释掉sava 时间 操作数量
# slave appendonly no

#