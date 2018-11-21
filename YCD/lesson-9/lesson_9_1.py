#! --*--coding:utf8--*--


# 切片 ---- slice

mylist=[1,2,3,4,5,6,7,8]

# print mylist[1:]

# 给定起始位置
print(mylist[1:])

# print mylist[-1]
# 给定结束位置
print(mylist[-1])
print(mylist[:-1])

# 起始位置，结束位置都给定
# 冒号加在前面，冒号加在后面
# 前闭后开；
print(mylist[1:-1])

# 起始，结束都不给定
# print mylist[:]
print(mylist[:])


# print mylist[1:6:2]
# 给定步长 ---- 一步走多长  步长 = 2，一步走两个元素的长度
# 如果给定的步长为正数，则小的序号在前面，大的序号在后面
print(mylist[1:6])
print(mylist[1:6:2])
print(mylist[0:6])
print(mylist[0:6:2])


# 给定步长，但是步长是负数，所以是倒叙的切片
# print mylist[::-1]
print(mylist[::-1])
print(mylist[:4:-1]) 
print(mylist[:3:-1]) # [8,7,6,5]
print(mylist[:3:-2])
print(mylist[1::-1])
mylist=[1,2,3,4,5,6,7,8]


# 如果给定的步长为负数，然后我的切片的序号是倒叙的
# 如果给定的步长为负数，则大的序号在前面，小的序号在后面，
print(mylist[1:4:-1]) 
print(mylist[2:4:-1]) 
# [7, 6]
mylist2 = mylist[5:7:1]
print(mylist2[::-1])
print(mylist[6:4:-1]) 
# 给定的步长不能为零
#print(mylist[1:6:0])