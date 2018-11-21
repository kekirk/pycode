#!--*--coding:utf8--*--
# GC --- 引用计数法

# 垃圾回收   GC算法

# GC算法  ------    复制压缩算法（java) ，但是java虚拟机不采用引用计数算法
# 引用计数

#a = list()
a = [1,2,3,4]
b = a
c = b
d = c

d = 9
c = 10
b = 11
a = 14

# del
b = list()

print(globals())
del b
print(globals())   # GC算法不会立马起效，del会立马起效



class gc():
	def __init__(self):
		print("it is inited")

	def __del__(self):
		print("it is deleted")

g = gc()

del g

while True:
	pass