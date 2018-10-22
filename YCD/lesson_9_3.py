#! --*--coding:utf-8--*--


# 判断数据结构是否相等
#     is    ==  ？ 他们的区别是什么


mylist=[1,2,3]
mylist2 = [1,2,3]

print(mylist==mylist2)

print(mylist is mylist2)

# == 是真的，is 是假的
# == 是判断数据结构当中的元素是否相等
# is 是判断数据结构自身的内存地址是不是相等

# 验证is是判断id的
print(id(mylist))
print(id(mylist2))

# 验证==是判断值的
mylist.append(1)
print(mylist==mylist2)

# 深拷贝 浅拷贝

mylist3 = mylist  # 用数据结构给变量赋值的时候，实际上是赋值的数据结构的内存id，而不是赋值的数据结构的元素 -------浅拷贝
print(mylist3)

mylist.append(3)
print(mylist3)

# 这是为什么？ 操作一个数据结构，另一个数据结构也发生了变化

print(id(mylist3))
print(id(mylist))


# 如何用数据结构赋值的时候只赋值元素，不是赋值内存id？？？？  -------- 深拷贝  

mylist4 = list()
for a in mylist:
	mylist4.append(a)

print(id(mylist4))
print(id(mylist))

# 说明这样就实现了深度拷贝

# 在python里面有一种方法可以自动实现深度拷贝：

# import copy    ------ 这涉及到python面向对象的知识，这里先不讲


