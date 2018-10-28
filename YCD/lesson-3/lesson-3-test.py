#!/usr/bin/env python
# -*- coding: utf-8 -*-

# a = 10
# print (a)

# name = input("姓名：")
# age = input("年龄：")
# # print(type(age))
# print(name,90-int(age))
# print("Hello,", name,", nice to see you!")

# b = 123_456_789
# b1 = 0b10
# b2 = 0o10
# b3 = 0x10
# print(b1,b2,b3)

# g = 0.1 + 0.2
# print(g)

# d = True
# print(type(d))

# print(10==10)
# print(15<12)

# a = 5
# a %=3
# print (a)

# print(True and False)
# print(a == 10 and b < 1000 and 100 == 100 or 5 > 2 or 1 < 10)

n = 5
m = 13
print("n =",n,", m =",m)

temp = n
n = m
m = temp
print("n =",n,", m =",m)

n = n^m
print(n)
m = n^m
print(m)
n = n^m
print("n =",n,", m =",m)
