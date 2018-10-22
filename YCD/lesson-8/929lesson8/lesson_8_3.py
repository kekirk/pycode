#! --*--coding:utf-8--*--

# 无序的数据结构，跟字典不一样

# 集合 ---- set

# 定义一个集合

#没有值
a = set()
print(a)


#有值
a = set([1,2,3,4,5])
print(a)



## 集合和字典的区别
# 集合当中的元素不能重复，字典当中的元素是可以重复的

a = {"a":1,"b":1,"c":2}
print(a)

b = set([1,1,1,1,2,2,3,3])
print(b)



## 操作
#增加
##  b[0]=1
##  b['a']=1

b.add("Sun")
print(b)

#删除
b.discard("Sun")
print(b)

# 交集 --- 并集 --- 差集

c=set([1,2,3,"aaa"])
print(b)
print(c)

# 交集
m = b & c
print(m)

#并集
m = b | c
print(m)


# 差集
n = b - c
print(n)

n = c-b
print(n)