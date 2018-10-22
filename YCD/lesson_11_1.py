#! --*--coding:utf8--*--
# 装饰器 setter getter 封装 多态



class A:
	def give_name(self,n):
		self.__name=n

	def ask_name(self):
		return self.__name

a = A();
a.give_name("aa")
print(a.ask_name())


# a.__name = "bb"
# print(a.__name)
# print(a.ask_name())

#print(a.__name)
a.__name="bb"
print(a.__name)


# attribute ---- 1,外部访问  2,外部不能访问
class Chinese:
	def __init__(self,scores):
		self.__scores = scores

	def set_scores(self,scores):
		if isinstance(scores,int) or isinstance(scores,float):
			if scores>0 and scores<=100:
				self.__scores= scores

	def get_scores(self):
		return self.__scores

c = Chinese(60)
#c.scores = 100;
c.set_scores(100)
print(c.get_scores())
c.set_scores("hello")
print(c.get_scores())



#使用装饰器 ----- 类似注解 (仅仅是类似，本质上是完全不同)
# 高阶函数  ----- 对于函数的一种高级使用方法

#闭包   ----- 动态生成函数  vs   静态函数

# 静态函数
def fun1():
	return 3;


# 动态函数 ------- exec eval , 动态语言
def createFun():
	def fun():
		return 3;
	return fun;

f1 = createFun()
print(f1())

def createFun(n):
	if n == 0:
		def fun():
			print("this is a fun created by code")
	if n == 1:
		def fun():
			return 8;
	return fun;	

f2 = createFun(0)
f2()
f3 = createFun(1)
print(f3())

# 装饰器

# def fun3():
# 	print("====start")
# 	# --------pass
# 	print("====end")
# 	return 3;

# print(fun3())

# # 调试我的程序
# def fun3():
# 	print("====start")
# 	# --------pass
# 	print("====end")
# 	return 3;

# # 调试结束

# def fun3():
# 	#print("====start")
# 	# --------pass
# 	#print("====end")
# 	return 3;

# print("=============================================")
# def log(aa):
# 	print("========start",aa)
# 	def run(n):
# 		return n;
# 	print("=========end")
# 	return run;

# #l = log(7)
# #print(l(0))


# print("***************************************************")
# #@log(1)


# @log("2018/10/15")
# def aaa(n):
# 	return n;

# print(aaa(8))


# @log("2018/10/15")
# def bbb(n):
# 	return n+8;

# print(bbb(9))



###

import time

def log(fun):    # flask
	print(time.time())
	def createFun(a,b):
		return fun(a,b)
	return createFun;

@log
def now(a,b):
	print("2018/10/15")

now(1,2);

class Chinese:
	def __init__(self,scores):
		self.__scores = scores

	def set_scores(self,scores):
		if isinstance(scores,int) or isinstance(scores,float):
			if scores>0 and scores<=100:
				self.__scores= scores

	def get_scores(self):
		return self.__scores


#   方法的重载在python当中是不支持的；

#   方法的重载是java当中，一种常用的方式 ： 同一个函数名，由于参数的不同，可以根据传参的不同，来决定我到底调用的是哪个函数

#   python勉强支持方法重载


class Chinese:
	def __init__(self,scores):
		self.__scores = scores

	@property
	def scores(self):
		return self.__scores

	@scores.setter
	def scores(self,scores):
		self.__scores=scores


c = Chinese(78)
c.scores = 99
print(c.scores)