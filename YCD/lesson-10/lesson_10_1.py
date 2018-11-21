#! --*--coding:utf-8--*--




mylist = [1,2,3,4,5]

mylist4 = list()
for a in mylist:
	mylist4.append(a)


# 但是有一个问题，每次完成这样一个相同的功能都要把相同的代码重新写一边；

mylist5 = list()
for a in mylist:
	mylist5.append(a)



# 避免重复敲代码，使用函数来解决；
#函数的作用： 保存代码

# step1
# 函数的定义

#  def ------ defind 的缩写，defind --- 定义
#  以fun为例，fun是自定义的函数的名字
#  在函数名之后，跟一个小括号  （—————— 它的作用是传递参数）
#  在括号后面加一个冒号：
def fun():       
	## 再另起一行去写我们要保存的代码,    ---- 但是一定要空一个tab键，或者四个空格键，建议大家使用tab键
	print("this is code ")

fun()
fun()
fun()
fun()
# step2
# 把上面的代码保存进去

def deepCopy():
	mylist5 = list()
	for a in mylist:
		mylist5.append(a)
	print(mylist5)


deepCopy()


# 但是，不能扩大应用范围  ， 虽然保存原有代码，但是代码逻辑不能通用

# 函数的参数，通过参数来实现函数的代码逻辑的通用性；


def deepCopy(l):
	l = list()
	for a in mylist:
		l.append(a)
	print(l)


mylist7 = "a"
deepCopy(mylist7)   # argument -- 参数
mylist8 = "a"
deepCopy(mylist8)
# 还不够完全的通用，如果想更加通用，怎么实现，？？？  ------ 这样可以实现的，但是这由于python的语言特点决定的，换句话说，就是这种功能在有一些语言中是实现不了的；----Java
# deepCopy("mylist8") ?? 这是因为 python是一种解释型的语言，但是java却是一种编译型的语言；

# 解释型语言：python ----- python在运行的时候，需要python解释器，对python代码进行逐行翻译，成为二进制码，然后让计算机执行；
# 编译型语言：java  ----- java在程序执行之前，就已经进行了(预)编译，所以导致，程序不能根据代码场景动态地去执行一些操作； Java和C是不一样的，C是一次编译成二进制码；
"list8 = list()"  
# eval 转义，将字符串转义成为了python代码命令  "mylist10 = list() " ---- mylist10 = list()

def deepCopy(listname):
	cs = listname + " = list()"
	eval(cs)
	

# deepCopy("mylist10")


# #函数的调用

# help()
# print()



# #函数的说明
# def fun():
# 	'''
# 	函数的说明
# 	函数的参数

# 	'''



# #函数的参数

# # def fun(a:int,b:bool,c:str):
# # 	print(1);


