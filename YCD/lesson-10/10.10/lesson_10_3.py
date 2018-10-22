#! --*--coding:utf-8--*--


#变量作用域


# 作用域  = 命名空间  ---- 就是一个字典{name:value}

# 两种命名空间：   
# 1.全局命名空间   ----- 全局作用域   ---  全局变量   --- global
# 2.局部命名空间   ------局部作用域   ---  局部变量   --- local
   

a = 4

def localArg(a):
	print(a)

localArg(8)


print(globals())


def localNameSpace(a,b,c):
	print(locals())

localNameSpace(1,2,3)

# 

a = 4

# 当局部变量和全局变量重名时，以局部变量为准
def requestGlobal(a):
	print(a)
requestGlobal(8)


# 当局部变量和全局变量不重名时，以全局变量为准
def requestGlobal(b):
	print(a)
requestGlobal(8)

# 当局部变量和全局变量重名时，又想访问全局变量
def requestGlobal(a):
	globalArgs = globals()
	globalA = globalArgs["a"]
	print(globalA)

requestGlobal(8)

# 当局部变量和全局变量不重名时，又想访问全局变量
a = 4

def requestGlobal(b):
	print(a)
requestGlobal(8)

def requestGlobal(b):    # SyntaxError: name 'a' is local and global
	global a
	print(a)

requestGlobal(8)

# ？？？？？ 为什么要多写一个global,这样不是浪费代码码？？？？

def requestGlobal(b): 
	global a
	a = a+1
	print(a)

requestGlobal(8)

print(a)


