#!/usr/bin/env python3
# -*- coding: utf-8 -*-

list = [1,2,4,3,4,5,6,7,6,4,89,4]
a = list[0]
b = list[len(list)-1]
print(list[0],list[len(list)-1],len(list)-1)

list[0]=132124
print(list[0],list[len(list)-1],len(list)-1)

del list[0]
print(list[0],list[len(list)-1],len(list)-1)

print(list.count(4),list.index(4,1,8))
