#！ --*--coding:utf-8--*--
## 定义---列表

# 第一种定义列表的方式
# 列表能存储什么数据？
# 数字 字符串 列表本身

a = []
# [  7,8,9                ]
# id(a) 
print(id(a))


# a[0]=7

a.append(7)
a.append(8)
a.append(9)


print(a)

print(a[0])
print(a[1])
print(a[2])
# append -- 增加
#                                     8
# 
print(id(a))
print(id(7))
print(id(8))


#    52512264
#a =[44392600,44392576,id(9),  ]
#a[0]


# 第二种定义列表的方式

b = list()
#print(b)
b.append(2)
b.append(3)

print(b)

#a=[]
#a=list()
# a[0]=7
a[0]=9

print(a)

## 操作
## 增加 查找 更改 删除

# 增加
a.append(10)

# 增加多个
c=[1,2]
d=[3,4]
print(c+d)

c=[1,2]
c.extend([4,5,6])
print(c)



#查找
print(a[2])


#更改
a[0]=11
print(a)

a.append([4,5,6])
print(a)


#删除
del a[4]
print(a)


# del的删除方式，是永久在内存删除吗
n = 8
a.append(n)
print(a)

del a[4]
print(a)

print(n)

del n
print(n)

# n 变量 a 数据结构






























