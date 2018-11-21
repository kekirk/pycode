#!--*--coding:utf8--*-- 

# 2.x python
# 类的方法vs静态方法

class A:
	def fun(self,name):
		print(name)



a = A()
a.fun("name")


#

class A:
	def fun(self,name):   #成员方法
		print(self) #<__main__.A instance at 0x00000000034B8F88>
		print(name)


	@classmethod   #class类 method方法
	def class_fun(cls,name):
		print(cls)    # __main__.A
		print(name)


a = A()
a.fun("name")
#A.fun("name")
A.class_fun("name")
a.class_fun("name")



class A:
	def fun(self,name):   #成员方法
		print(self) #<__main__.A instance at 0x00000000034B8F88>
		print(name)


	@classmethod   #class类 method方法
	def class_fun(cls,name):
		print(cls)    # __main__.A
		print(name)


	@staticmethod
	def static_fun(arg1):  # staticmethod 就是一个普通方法
		print(arg1)


A.static_fun("bb")
a = A()
a.static_fun("aa")


#  成员方法   ------ 对象调用
#  类的方法   ------ 对象 类 都可以调用
#  静态方法   ------ 对象 类 都可以调用


# 
class Annimal:
	@classmethod
	def class_fun(cls,name):
		print(name)

	@classmethod
	def class_cat(cls):
		c = cls()
		c.name="cat"
		c.food="fish"
		c.freetime="sleep"
		return c 

	@classmethod
	def class_dog(cls):
		d = cls()
		d.name="dog"
		d.food="bone"
		d.freetime="run"
		return d


a1 = Annimal.class_dog()
print(a1.name)


a2 = Annimal.class_cat()
print(a2.name)

#工厂模式  --- java学来的


# 静态方法
class Math:
	@staticmethod
	def sum(*args):
		res = 0
		for a in args:
			res += a
		return res

	@staticmethod
	def average(*args):
		print(args)
		s = Math.sum(*args)
		return s/len(args)


#对方法的一些管理的方式
res = Math.sum(1,2,3,4)
print(res)

avg = Math.average(1,2,3,4)
print(avg)



