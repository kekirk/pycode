#! --*--coding:utf8--*--

# 面向对象

# 对象是内存中存储变量和代码区的一块区域


# 变量 ---- 数据
# 数据结构 --- 变量
# 函数 ----- 代码逻辑
# 对象 ----- 函数+变量+数据结构


# 面向对象 ------ 面向过程 C --- C++ --- Java python


# 定义一个类(对象)

class firstClass():                  # --------- 类
	pass

firstObject = firstClass()          # ----- Object ---- 对象 --- （客体) --- 物体

# 一切的物体，都有自己的种类；
# 把种类抽象出来，如果之后需要用到种类当中的某个物体，按照我定义的种类自动生成出来；

# 小狗 dog
# 种类 annimal

print(globals())

class FourLegAnimmal():
	leg = 4
	head = 1
	product = "buru"
	legs = ["left1","left2","right1","right2"]
	def eat():
		print("It has eated")

dog1 = FourLegAnimmal()

print(globals())

# 内存当中 ---->  1,增加了一个类  2,当生成对象的时候，增加了一个对象

#   ---- 实例  

# isinstance
print(isinstance(dog1,FourLegAnimmal))

# 种类 ----》 共性   实例 ----》 个性

# 初始化
class FourLegAnimmal():
	leg = 4
	head = 1
	product = "buru"
	def __init__(self,col):
		color = col

dog2 = FourLegAnimmal("red")

#print(dog2.color)    ----- error
# AttributeError: FourLegAnimmal instance has no attribute 'color'

# attribute ---- 属性  ？？？ --- 特点  ---- 个性

# self   ----- 自身
class FourLegAnimmal():
	leg = 4
	head = 1
	product = "buru"
	def __init__(self,col):
		self.color = col

dog2 = FourLegAnimmal("red")

print(dog2.color)

# self.color  #
mylist = list()
mylist.append(1)
mylist.append(5)
mylist.append(5)

print(max(mylist))
print(mylist.count(5))

# mylist = list()  ------------  dog1 = FourLegAnimmal()
# .点 ---- 产看或者调用对象内部的(变量，数据结构，函数)



# __init__():
# init --- 初始化

class FourLegAnimmal():
	leg = 4
	head = 1
	product = "buru"
	legs = ["left1","left2","right1","right2"]
	def __init__(self,col):
		print("my color is "+col)
		self.color = col

	def run():
		print("running")

dog3 = FourLegAnimmal("black")

# __init__() 是Python面向对象中的默认的函数，当去生成一个实例(对象)时，会执行这个函数

# self 到底是个啥
class FourLegAnimmal():
	leg = 4
	head = 1
	product = "buru"
	legs = ["left1","left2","right1","right2"]
	def __init__(self,col):
		print("my color is "+col)
		self.color = col

	def run(self):
		print("running")

dog4 = FourLegAnimmal("black")

# self --- 自身
# self -- 实例(object)  代表的是同一个内存id, 所以object有的东西，self也都有

class FourLegAnimmal():
	leg = 4
	head = 1
	product = "buru"
	legs = ["left1","left2","right1","right2"]
	def __init__(self,col):
		print("my color is "+col)
		self.color = col

	def run(self):
		print(self.leg)
		print("running") 

dog5 = FourLegAnimmal("black")
#print(dog5.leg)
dog5.run()

# 属性(变量，数据结构)   +  方法(自定义函数，默认函数) = 类
# 函数 + 参数  --->  结果
# 方法 + 属性  --->  结果


class FourLegAnimmal():
	leg = 4
	head = 1
	product = "buru"
	legs = ["left1","left2","right1","right2"]
	def __init__(self,col):
		print("my color is "+col)
		self.color = col

	def run(leg1,leg2,leg3,leg4):
		print(leg1)
		print(leg2)
		print(leg3)
		print(leg4)

dog5 = FourLegAnimmal("black")
dog5.run(dog5.legs[0],dog5.legs[1],dog5.legs[2])

# 1

class FourLegAnimmal():
	leg = 4
	head = 1
	product = "buru"
	legs = ["left1","left2","right1","right2"]
	def __init__(self,col):
		print(self)
		print("my color is "+col)
		self.color = col

	def run(self,leg1,leg2,leg3,leg4):
		print(leg1)
		print(leg2)
		print(leg3)
		print(leg4)

dog5 = FourLegAnimmal("black")
dog5.run(dog5.legs[0],dog5.legs[1],dog5.legs[2],dog5.legs[3])

# self: 这个单词，不是必须这么写，也就是说，写什么都行，但是Python会默认认为函数的第一个参数就是self参数,但是一般情况下，我们会写self

# 为什么给了四个参数，Python认为我给了五个？？



class FourLegAnimmal():
	leg = 4
	head = 1
	product = "buru"
	legs = ["left1","left2","right1","right2"]
	def __init__(self,col):
		print(self)
		print("my color is "+col)
		self.color = col

	def run(self):
		print(self.legs[0])
		print(self.legs[1])
		print(self.legs[2])
		print(self.legs[3])

dog6 = FourLegAnimmal("black")
dog6.run()


### 
class FourLegAnimmal():
	leg = 4
	head = 1
	product = "buru"
	legs = ["left1","left2","right1","right2"]
	def __init__(self,col):
		print(self)
		print("my color is "+col)
		self.color = col

	def run(self,tail):
		print(self.legs[0])
		print(self.legs[1])
		print(self.legs[2])
		print(self.legs[3])
		if tail:
			print("tail")
		else:
			pass

dog6 = FourLegAnimmal("black")
dog6.run(True)


##  object 不止属于一个种类，dog 既是动物 又生物 还是物体


class Animal():
	do = True
	eat = True


dog7 = Animal()

dog7 = FourLegAnimmal("black")

# 继承
class FourLegAnimmal(Animal):
	leg = 4
	head = 1
	product = "buru"
	legs = ["left1","left2","right1","right2"]
	def __init__(self,col):
		print(self)
		print("my color is "+col)
		self.color = col

	def run(self,tail):
		print(self.legs[0])
		print(self.legs[1])
		print(self.legs[2])
		print(self.legs[3])
		if tail:
			print("tail")
		else:
			pass

	def let_eat(self):    ## 
		print("let it eat")

dog7 = FourLegAnimmal("black")
print(dog7.eat)

# 
if(dog7.eat):
	dog7.let_eat()

# 更改对象的属性
dog7.eat=False;
if(dog7.eat):
	dog7.let_eat()
else:
	print("it can not eat")

# 
class FourLegAnimmal(Animal):
	leg = 4
	head = 1
	product = "buru"
	legs = ["left1","left2","right1","right2"]
	def __init__(self,col):
		print(self)
		print("my color is "+col)
		self.color = col

	def run(self,tail):
		print(self.legs[0])
		print(self.legs[1])
		print(self.legs[2])
		print(self.legs[3])
		if tail:
			print("tail")
		else:
			pass

	def let_eat(self):    ## 
		print("let it eat")

dog8 = FourLegAnimmal("black")
dog8.let_eat()       ###  只要是类里面定义的函数，当我使用这个函数的时候，Python会默认赋值给函数一个参数----就是self参数


# 
# let_eat -- 可以吃，也可以不吃，也就是 这个属性是可以更改
# 但是有一些属性是不能更改的，color

class FourLegAnimmal(Animal):
	leg = 4
	head = 1
	product = "buru"
	legs = ["left1","left2","right1","right2"]
	def __init__(self,col):
		print(self)
		print("my color is "+col)
		self.__color = col
		print(self.__color)

	def run(self,tail):
		print(self.legs[0])
		print(self.legs[1])
		print(self.legs[2])
		print(self.legs[3])
		if tail:
			print("tail")
		else:
			pass

	def let_eat(self):    ## 
		print("let it eat")

dog9 = FourLegAnimmal("black")
#print(dog9.__color)
### 在Python当中，object的属性，如果是以__(两根下划线开头)，就代表这个属性不能从外部访问(不能通过.点访问)

#
class FourLegAnimmal(Animal):
	leg = 4
	head = 1
	product = "buru"
	legs = ["left1","left2","right1","right2"]
	def __init__(self,col):
		print(self)
		print("my color is "+col)
		self.__color = col
		print(self.__color)

	def run(self,tail):
		print(self.legs[0])
		print(self.legs[1])
		print(self.legs[2])
		print(self.legs[3])
		if tail:
			print("tail")
		else:
			pass

	def __let_eat(self):    ## 
		print("let it eat")

dog10 = FourLegAnimmal("black")
#dog10.__let_eat()   # 说明 __两根下划线打头的函数(方法)也是不能访问的；


# dog ---   FourLegAnimmal  ---  Animal  --- FourLeg (桌子)

# python的多继承      ------ 多继承这种继承方式(面向对象)，有一些语言支持，有一些不支持  # java 单继承， c++ 多继承
class FourLeg():
	leg = 4


dog11 = FourLeg()
dog11 = FourLegAnimmal("black")

class FourLegAnimmal(Animal,FourLeg):
	head = 1
	product = "buru"
	legs = ["left1","left2","right1","right2"]
	def __init__(self,col):
		print(self)
		print("my color is "+col)
		self.__color = col
		print(self.__color)

	def run(self,tail):
		print(self.legs[0])
		print(self.legs[1])
		print(self.legs[2])
		print(self.legs[3])
		if tail:
			print("tail")
		else:
			pass

	def __let_eat(self):    ## 
		print("let it eat")

dog11 = FourLegAnimmal("black")
print(dog11.leg)



## 

# 多重继承

class LivingBeings():
	living = True


dog12 = LivingBeings()
dog11 = FourLegAnimmal("black")


class Animal(LivingBeings):
	do = True
	eat = True

class FourLegAnimmal(Animal,FourLeg):
	head = 1
	product = "buru"
	legs = ["left1","left2","right1","right2"]
	def __init__(self,col):
		print(self)
		print("my color is "+col)
		self.__color = col
		print(self.__color)

	def run(self,tail):
		print(self.legs[0])
		print(self.legs[1])
		print(self.legs[2])
		print(self.legs[3])
		if tail:
			print("tail")
		else:
			pass

	def __let_eat(self):    ## 
		print("let it eat")

dog13 = FourLegAnimmal("black")
print(dog13.living)


