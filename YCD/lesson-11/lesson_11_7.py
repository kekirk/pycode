#!--*--coding:utf8--*-- 
from abc import abstractmethod,ABCMeta

# 抽象方法，----抽象类


class A:   #

	@abstractmethod
	def abfun(self):   # abstract 抽象
		pass


class B(A):
	def abfun(self):
		print("this is a instance of abstractmethod")

	def run(self,times):
		print("run"*times)


b = B()
b.run(10)
b.abfun()

# 接口 -- 实现类

# 定义了一个编程的规范，默认去继承这个类的时候，要遵守这个规范，这个规范就是去具体实现这些抽象方法

class Collection:   # 收集 -- 集合  --- 数据结构 --- list map set tuple
	# def __init__(self,list):
	# 	self.__list = list

	@abstractmethod
	def select(self,n):       # 查找
		pass
		#return self.__list[n]

	@abstractmethod
	def update(self,n,v):     #更改
		pass

	@abstractmethod
	def delete(self,n):     #删除
		pass

	@abstractmethod
	def insert(self,v):   #插入
		pass

class myList(Collection):
	def __init__(self,list):
		self.__list=list

	def select(self,n):       # 查找
		return self.__list[n]

	def update(self,n,v):     #更改
		self.__list[n]=v
		return True

	def delete(self,n):     #删除
		del self.__list[n]
		return True

	def insert(self,v):   #插入
		self.__list.append(v)
		return True



l = [1,2,3,4]
ml = myList(l)

print(ml.select(0))

ml.insert(9)

print(ml.select(4))


print(ml.delete(4))



# 好处？
# Ifind Choice Wind
# document 

# dailyOpen() ：返回今天的开盘价

# fivedailysAverageOpen()  :返回5天平均价
# 1+2+1+4+3

# 1*0.3+2*0.25+3*0.2+4*0.15+5+0.1 加权平均



class Foo():  
	__metaclass__ = ABCMeta
	def f1(self):
		print(123)
 
	def f2(self):
		print(456)
 
	@abstractmethod  
	def f3(self):
		pass
 
class Bar(Foo):
	def f3(self):
		print(33333)

bar = Bar()

print(Foo.__metaclass__)

