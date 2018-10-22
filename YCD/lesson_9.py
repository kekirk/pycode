#! --*--coding:utf-8--*--


# 对于有序数据结构的通用操作

# + 和 *
# +的操作
mylist=[1,2,3,4,5,2]
mylist1 = [1,2,3,4,5,7]
print(mylist + mylist1)
# [1,2,3,4,5,2,1,2,3,4,5,7]

a = (1,2,3,4)
b = (2,3,4,5)
print(a+b)

# *的操作
print(mylist * 3)
# [1,2,3,4,5,2,1,2,3,4,5,2,1,2,3,4,5,2]

print(a*3)

# in ,not in

print(3 in a)  # True
print(7 in a)  # False
print(7 not in a) # True


print((1,2) in a)
print([1,2,3] in mylist1)

# len ---- length --- 长度
print(len(a)) #  4
print(len(mylist1))  # 6




# max() -- 最大 
print(max(a)) # 4
print(max(mylist1))

mylist3 = ["ab","ac","ba","bb","ca"]
print(max(mylist3)) 

# min()
print(min(mylist1))

mylist2 = ["a","b","c","c","b","e"]
print(min(mylist2))
print(min(mylist3))


# list.count()   ------- count 数量
print(mylist2.count("a")) # 1
print(mylist2.count("b")) # 2

# -- len -- 函数   count -- 方法 # :涉及到面向对象编程的知识；
# list.index()   ------ index （索引，--查到数据的序号）（目录 -- 查到单词的页数）
# index 返回的是数据结构中满足条件的第一个元素的序号
print(mylist2.index("c")) # 2

# print(mylist.index(2,2))
# mylist2 = ["a","b","c","c","b","e"]
# index 进行序号查找的时候，起始地查找位置；
print(mylist2.index("c",3)) # ---- 3
print(mylist2.index("b",2)) # ---- 4