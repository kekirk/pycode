# !/usr/bin/env python3
#! --*--coding:utf-8--*--
# import os, ntpath
import pickle

d = dict(name="CKJ",age=55)
print(d)

print(pickle.dumps(d))

f = open("dump.txt","wb")
pickle.dump(d,f)
f.close()

f = open("dump.txt","rb")
d1 = pickle.load(f)
f.close()
print(d1)

# f = open("dict.txt","r")
# d2 = f.read()
# d3 = eval(d2)   #转义
# f.close()
# print(d2,type(d2))
# print(d3,type(d3))

import json

print(d)
print(json.dumps(d))

c = "ehsdfsd sdfsdf"
jc = json.dumps(c)
print(jc)

f = None
jf = json.dumps(f)
print(jf)