#! --*--coding:utf-8--*--
# pip install sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

import warnings
warnings.filterwarnings("ignore")


engine = create_engine("mysql://root:12345@localhost:3306/sqlalchemy")
conn=engine.connect()

# conn.execute("create table table2 (column1 int,column2 varchar(200))")
# conn.execute("insert into table2 values(12,'value1')")
result = conn.execute("select * from table2")
print(result.keys())
for res in result:
	print(res)
# cursor = conn.cursor() 游标在sqlalchemy当中不支持
# print(cursor)
conn.close()

# orm框架 mybatis sqlalchemy
# object relationship mapping 对象关系映射
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import Column,String,and_,or_,text,ForeignKey,Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base() # DeclarativeMeta 声明的元数据

class User(Base):
	__tablename__="user"
	id = Column(String(20),primary_key=True)
	name = Column(String(20))
	book = relationship("Book")

# CREATE TABLE `user` (
#   `id` varchar(20) NOT NULL,
#   `name` varchar(20) DEFAULT NULL,
#   PRIMARY KEY (`id`)
# )

# alter table book add constraint `fk` foreign key (`user_id`) 
# references user(`id`);

class Book(Base):
	__tablename__="book"
	id = Column(String(20),primary_key=True)
	name = Column(String(20))
	user_id=Column(String(20),ForeignKey("user.id"))

# CREATE TABLE `book` (
#   `id` varchar(20) NOT NULL,
#   `name` varchar(20) DEFAULT NULL,
#   `user_id` varchar(20) DEFAULT NULL,
#   PRIMARY KEY (`id`),
#   KEY `user_id` (`user_id`),
#   CONSTRAINT `book_ibfk_1` FOREIGN KEY (`user_id`) 
#	REFERENCES `user` (`id`)
# ) 

class Score(Base):
	__tablename__="score"
	id = Column(String(20),primary_key=True)
	student = Column(String(20))
	score = Column(String(20))

class Student(Base):
	__tablename__="student"
	id=Column(Integer,primary_key=True)
	book = Column(String(20))
	score = Column(String(20),ForeignKey("score.id"))

#print(Base.metadata.__dict__) #元数据
# https://sqlalchemy-migrate.readthedocs.io/en/latest/
# sqlalchemy-migrate
# sqlalchemy web框架 flask-sqlalchemy dictory(version_info)

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

Base.metadata.create_all(engine)


# 增删改查
DBSession = sessionmaker(bind=engine) # 建立会话
session = DBSession()

# 类---表
# 对象---数据
# xiaoming = User(id="1",name="xiaoming")
# session.add(xiaoming)
# session.commit()

# book_record = Book(id="1",name="book1",user_id="1")
# session.add(book_record)
# session.commit()


# 检索数据
# 简单查询

users = session.query(User)
print(type(users))  # <class 'sqlalchemy.orm.query.Query'>
# select * from user;
users = session.query(User).all()
print(type(users))  # <type 'list'>
for user in users:
	print(user.id)
	print(user.name)

# select * from user limit 1;
#user = session.query(User).one()
print(user.name)
user = session.query(User).first()
print(user.name)
# select * from user limit 10;
users = session.query(User).limit(5).all()
print(users)


# 条件查询
# select * from user where id=1;
user = session.query(User).filter(User.id=="1").one()
#print(type(user))
print(user.name)
users = session.query(User).filter(User.name.like("xiao%")).all()
print(users)

# 字段过滤
# select id,name from user;
users = session.query(User.id,User.name).all()
print(users) # [('1', 'xiaoming')]

# select name from user;
users = session.query(User.name).all()
print(users) # [('xiaoming',)]
for user in users:
	#print(user.id)
	print(user.name)

# 如果进行了字段过滤，就无法得到一个对象了;
users = session.query(User,User.name).all()
print(users)

#多条件查询 and，or

users = session.query(User).filter(and_(User.name.like("xiao%"),
	User.id=="1")).all()
print(users)

users = session.query(User).filter(or_(User.name.like("xiao%"),
	User.id=="1")).all()
print(users)

# 逻辑查询 < > >= <=
users = session.query(User).filter(User.id>="0").all()
print(users)

users=session.query(User).filter(text("id>:params")).params(params=0).all()
print(users)

#关联查询 
# =
user_book = session.query(User,Book).filter(Book.user_id==User.id).all()
print(user_book)
print(user_book[0][0].id)
print(user_book[0][1].user_id)
# inner join
user_book = session.query(User).join(User.book).all()
print(user_book)
# left outer join
user_book = session.query(User,Book).outerjoin(User.book).all()
print(user_book)
# SELECT user.id AS user_id, user.name AS user_name, book.id AS book_id, book.name AS book_name, book.user_id AS book_user_id 
# FROM user LEFT OUTER JOIN book ON user.id = book.user_id

# 关闭会话
session.close()