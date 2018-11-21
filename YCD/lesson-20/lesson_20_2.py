#！ --*--coding:utf-8--*--
# SQLite  --- SQL structual query language

# DataBase mysql redis mongodb oracle SQLite

# android file xml sqlite linux

# database ---- table 

# 怎样安装python package
# pypi python package index
# pip install SQLAlchemy
# pip python install package

# Connections / Engines 连接 
# MetaData / Schema 元数据
# SQL Expressions 表达我的检索目的
# ORM Configuration orm 对象关系映射
#          select * from user
# Performance
# Sessions / Queries  回话 


from sqlalchemy import create_engine # 创建一个引擎
from sqlalchemy.pool import QueuePool
engine = create_engine('mysql://scott:tiger@localhost/myisam_database')
# mysql数据库
# mysql 数据库的种类 3306(default port)
# scott:tiger 用户名:密码
# localhost socket(ip+port)
# myisam_database 数据库的名字

# sqlite
eng = create_engine("sqlite://")
conn = eng.connect()
# create 创建表
conn.execute("create table x (a integer, b integer)")
# insert 插入数据
conn.execute("insert into x (a, b) values (1, 1)")
conn.execute("insert into x (a, b) values (2, 2)")
# 检索数据
result = conn.execute("select x.a, x.b from x")
print(result.keys())

# 手动创建一个sqlite数据库
# 在一个指定的路径下面
# sqlite3 databasename.db 回车
# .databases 回车
# .q 回车退出

import sqlite3
conn = sqlite3.connect("lesson20.db")
# 游标 cursor 
cursor = conn.cursor()
# 执行数据库命令
cursor.execute("create table student(id varchar(20),name varchar(20))")
# 关闭游标
cursor.close()
# 关闭连接
conn.close()


from sqlalchemy import create_engine # 创建一个引擎
from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String
# Column 字段(列)，String 文本

engine = create_engine('sqlite:////lesson20demo.db')
print(type(sessionmaker)) # <type 'type'>
DBsession = sessionmaker(bind=engine)
print(type(DBsession)) #<class 'sqlalchemy.orm.session.sessionmaker'>

print(type(declarative_base))  #<type 'function'>
Base = declarative_base()
print(Base) # <class 'sqlalchemy.ext.declarative.api.Base'>


class User(Base):
 	__tablename__="user"

 	id = Column(String(20),primary_key=True) # primary_key 主键
 	name = Column(String(20))


class Score(Base):
	__tablename__="score"

	student = Column(String(20),primary_key=True)
	score = Column(String(20))

class Score_math(Base):
	__tablename__="score_math"

	student = Column(String(20),primary_key=True)
	score = Column(String(20))

class Score_english(Base):
	__tablename__="score_english" # 表明必须小写

	student = Column(String(20),primary_key=True)
	score = Column(String(20))

class Score_chinese(Base):
	__tablename__="score_chinese"

	student = Column(String(20),primary_key=True)
	score = Column(String(20))


# 创建表
Base.metadata.create_all(engine)

# 建立会话
session = DBsession() # <class 'sqlalchemy.orm.session.Session'>
print(type(session))

# 生成数据
xiaoming = User(id="5",name="xiaoming")
xiaoming_score = Score(student='5',score='100')
xiaoming_math_score = Score_math(student='5',score='100')
xiaoming_chinese_score = Score_chinese(student='5',score='99')
xiaoming_english_score = Score_english(student='5',score='88')


# 插入数据
session.add(xiaoming)
session.add(xiaoming_score)
session.add(xiaoming_math_score)
session.add(xiaoming_chinese_score)
session.add(xiaoming_english_score)

# 提交操作
sesion.commit()

# 检索数据
user = session.query(User).filter(User.id=='5').one()
print(user)
print(user.name)

xiaohong = User(id="1",name="xiaohong")
session.add(xiaohong)
session.commit() # 增加数据的时候需要提交，检索数据不需要提交

user = session.query(User).first()
print(user)
print(user.name)

all_user = session.query(User).all()
print(all_user)

for user in all_user:
	exec(str(user.name) + "=user")
	print(user.name)


all_user_two = session.query(User.name, User.id).all()
print(all_user_two)
for user in all_user_two:
	print(user[0])
	print(user[1])

# 关闭会话
session.close()



