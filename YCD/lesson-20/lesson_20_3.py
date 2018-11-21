#! --*--coding:utf-8--*--


# mysql oracle sqlite mongodb pg 
# mysql 安装 windows linux relationship 


# redis 内存数据库 # key - value 

#查看数据库
show databases;

# 切换数据库
use mysql;

# 查看表
show tables;

# 创建数据库
create database pydb

# 创建表
use pydb;
create table table1 (column1 varchar(20),column2 int,column3 float)

# 插入数据
insert into table1 values('jiang',1,1.3)
insert into table1 values('jiang',2,1.3)

# 更改数据
update table1 set column1='jiangTeacher'
update table1 set column1 = "jiangStudent" where column2 = 2

# 查询数据
select * from table1
select column1 from table1
select column1,column2 from table1
select column1,column2 from table1 where column2 = 1

#删除数据
delete from table1 where column2 = 2