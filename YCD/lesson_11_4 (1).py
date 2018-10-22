#! --*--coding:utf8--*--


# __init__


# __del__


# __str__
class test():
	def __str__(self):
		return "this is a class"

t = test()
print(t)


class test():
	pass

t = test()
print(t)


class students():

	def __init__(self,name,age):
		self.name=name
		self.age=age


	def __str__(self):
		a = "i am a students , my name is "+self.name+" and my age is "+str(self.age)
		return "i am a students , my name is %s and my age is %d" % (self.name,self.age)

#t = students("xiaoming",17)
#print(t)

t = students("xiaohong",16)
print(t)


# 运算符重载
# __gt__            # greater than >

class students():

	def __init__(self,name,age):
		self.name=name
		self.age=age

	def __gt__(self,other):
		return self.age>other.age

t1 = students("xiaoming",17)
t2 = students("xiaohong",16)

print(t1<t2)


class students():

	def __init__(self,name,age):
		self.name=name
		self.age=age

t1 = students("xiaoming",17)
t2 = students("xiaohong",16)

print(t1<t2)


# __ge__    greater equal >=


# __lt__     <


# __le__    <=


# __eq__    ==


# __ne__    !=


#@log(1,"a")


# 继续讲面向对象

# __repr__



# 当当  零基础入门学python python从入门到精通

# 利用python做机器学习  利用python做数据分析 利用python做自然语言处理  利用python做web开发 利用python做爬虫
