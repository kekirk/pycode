#! --coding:utf-8--*--


#列表通过切片赋值



mylist=[1,2,3,4]


print(mylist[1:3])


mylist[2]=1
mylist[3]=4

print(mylist)

mylist[1:3]=[3,2]
print(mylist)