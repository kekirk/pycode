#！ --*--coding:utf-8--*--


# 无序的数据结构
# 字典

# 字典 ------ 是hash表的一种python的具体实现的方式

# 键值对  ----- 与列表是不同的

# [1,2,3,4,5]  1-- 0 , 2-- 1,          值 ----- 序号
# {"k":1,"k2":2,"k3":3}    1--k , 2 -- k2, 3--k3  ,   值 --- "名字"（键）

# 键----值对

# 定义一个字典

#第一种定义的方式

d ={}
# l = [] --- 列表 ，t = () -- 元组，d = {} ---- 字典
print(d)


d["n1"]=1
print(d)


d["name"]="jiang"
print(d)


d["name2"]="chun"
print(d)

# # （字符串 数字）【不同的变量类型】 可以共同存在字典里，同时也可以同时存在列表里，也可以同时存在元组里
# l = [1,"aaa"]
# print(l)
# t=(1,"aaa")
# print(t)

# 存储顺序，实际上是没有先后意义的，因为字典本身这种数据结构就是一种没有顺序的数据结构

# 第二种定义字典的方式

d = dict()

print(d)

d['name']="jiang"
print(d)

# 操作

#增加
d['name1']=1
d["name4"]=2

print(d)

# 查找
# a = [1,2,3]
# a[1]
print(d["name4"])
print(d["name1"])


# 删除
del d["name4"]
print(d)

t=5
d['name5']=t
del d['name5']
print(t)

# 更改
print(id("hello"))
d["name"]="hello"
print(d)
del d["name"]
print(id("hello"))


## gc -- 垃圾回收机制，是通过python解释器来控制的
## del d; print(d)
## 也是可以通过程序员自己控制



## 列表 与 字典 （增加操作） 的区别

## 注意： 字典的更改与增加的操作，是语法一样的，

## 
d={"k1":1,"k2":2}

# 当我的Key已经存在时，我属于更改的操作
d['k1']=3
# 当我的Key不存在时，我属于增加操作
d["k3"]=3



## 增加和更改-----与列表的区别
a = [1,2,3,4]
# 当我的序号(index)已经存在时，我属于更改的操作
a[3]=5
print(a)
# 当我的index不存在时，我属于增加操作 （这是错误的）
a.append(9)
#a[4]=9


# 字典的value可以改，那key可以改吗?
# 不能更改

## 
d={"k1":1,"k2":2}

n = d["k2"]
del d['k2']
d['k3'] = n
print(d)



