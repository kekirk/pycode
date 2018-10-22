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
	

# 测试
#"list8" = list();
# cmd ----- command
def deepCopy(listname):
	cmd = listname + "= list()";    "list8 = list()"
	exec(cmd)    # execute
	for a in mylist:
		#mylist4.append(a)
		cmd1 = listname + ".append(a)"
		exec(cmd1)
	#print(list8)



deepCopy("list8")


# 为什么一个变量已经在函数内部的执行过程中被定义过了，但是在函数的外部去使用的时候，确实不存在的？
#print(list8)
# 在python当中，所有的变量都是有”作用域“的，----- 作用域，指的是一个变量它起作用的范围(区域)，
# 那么，函数中的变量只在函数内部起作用；
# 那么，我们就要让函数的结果返回回来； ------- return 

def deepCopy(listname):
	cmd = listname + "= list()";    "list8 = list()"
	exec(cmd)    # execute
	for a in mylist:
		#mylist4.append(a)
		cmd1 = listname + ".append(a)"
		exec(cmd1)
	#print(list8)
	#exec("return listname")
	#cmd2 = "listres = "+listname
	#print(cmd2)
	#print(listres)
	#exec(cmd2）     "listres = list8"
	#return listres
	return eval(listname)


list8 = deepCopy("list8")
print("------------------------------")
print(list8)



# exec ------  execute 
# 可以将一个字符串的python代码，执行；
code = "a = 'hello world'"
exec(code)
print(a)


# eval ------  转义
# 将一个变量的名字----->变成变量自身

list10 = list()
print(list10)
print(eval("list10"))

# return ---- 返回 ----- 返回函数 
# 将函数的结果返回到函数的作用域以外, 同时要进行接收；


def rt():
	b = 100
	return b

c = rt()
print(c)

# 返回函数，也就是说，一个函数可以不返回任何值，如果有返回值，就叫返回函数；

# 普通函数(不返回值的函数)，

list11 = list()
print("----------------------------")
print(list11)
def addValue(lt):
	lt.append(1)
	lt.append(2)

addValue(list11)
print(list11)

# 在python的作用域中，函数内部的变量(不返回)，在外部是无法访问，
# 但是，函数外部的变量，在函数内部却可以访问


# 函数的说明
# help -------- python当中，help可以帮助开发人员，看到一个功能的使用说明书
list12 = list()
#help(list)


def explainBook():
	'''
		this is a function ,it can help you to get a number
		这是一个函数，它能帮你得到你个数字

	'''
	return 8;

print(explainBook())
help(explainBook)



# 函数的参数
# 参数类型 ---- 不同种类的参数

# 必备参数

def needArg(arg):
	a=1
needArg("33")

def needArgs(arg1,arg2):
	a = 1

needArgs("33",12)


# 缺省参数
#--------
def canNullArg(arg=2):   # 缺省 ----- 默认
	a = 1

canNullArg()

#-------
def canNullArg(arg=2):   # 缺省 ----- 默认
	print(arg)

canNullArg()

#------
def canNullArg(arg=2):   # 缺省 ----- 默认
	print(arg)


canNullArg(arg=3)
canNullArg(3)

# ((((传参的方式

def giveArgs(arg1,arg2,arg3):
	print(arg1)
	print(arg2)
	print(arg3)

print('-----------------------')
giveArgs(1,2,3)
print('-----------------------')
giveArgs(arg1=1,arg3=2,arg2=3)

###   传参的方式有两种： 一种：顺序传参，二种：参数名传参)))) 


# 不定长参数   # 不定长参数分为两种

def LengthArgs(arg1,arg2,arg3):
	a = 1


#LengthArgs(1,2,3,4)


def unlimitLengthArgs(*args):
	a = 1

unlimitLengthArgs(1,2,3,4)


# 函数的参数的作用，通过参数来实现函数的代码逻辑的通用性；
# 函数的参数的不定长，能够更加增进函数的通用性；

def unlimitLengthSum(*args):     #Sum ---- 求和
    print(args)


print('-----------------------')
unlimitLengthSum(1,2,3,4)

def unlimitLengthSum(*args):     #Sum ---- 求和
    print(args)
    res = 0
    for s in args:
    	res += s
    return res

num = unlimitLengthSum(1,2,3,4,5,6,7,8,9,10)
print(num)

num = unlimitLengthSum(1,2,3,4,5,6,7,8,9,10,11)
print(num)


# 不定长参数2
def unlimitLength(**args):
	print(args)

unlimitLength(a=1,b=2,c=4)

d1 = dict()

def unlimitLength(**kvargs):
	a = kvargs['dividend']
	b = kvargs['divisor']
	print(a/b)

unlimitLength(divisor=2,dividend=4)


# 字典参数-----例子

# 终端操作电脑时，传参用；






