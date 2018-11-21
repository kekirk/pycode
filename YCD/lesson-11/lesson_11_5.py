#!--*--coding:utf8--*--

# super() 超越 超级  superman  -----super() 父类

class father(object):
	def __init__(self,age,gender,hometown,country,sports):
		self.age = age
		self.gender = gender
		self.hometown = hometown
		self.country = country
		self.sports = sports


class son(father):
	def __init__(self,age,gender,hometown,country,sports,name):
		self.age = age
		self.gender = gender
		self.hometown = hometown
		self.country = country
		self.sports = sports
		self.name = name


s = son(1,1,1,1,1,1)

# 3.x
# class son(father):
# 	def __init__(self,age,gender,hometown,country,sports,name):
# 		super().__init__(age,gender,hometown,country,sports)
# 		self.name=name


s = son(1,1,1,1,1,1)

# 2.x
class son(father):
	def __init__(self,age,gender,hometown,country,sports,name):
		super(son,self).__init__(age,gender,hometown,country,sports)
		self.name=name

s = son(1,1,1,1,1,1)




# 方法重写
class A(object):
	def eat(self):
		print("it is eatting");


class B(A):
	def eat(self,food):
		print("it eats %s" % food)


a = A()
a.eat()

b = B();
b.eat("noodels")



print("---------------------------------------")
class C(A):
	def eat(self,food):
		super(C,self).eat()
		print("it eats %s" % food)

c = C()
c.eat("apple")