#! --*--coding:utf-8--*--

#serilizable 可序列化


#1233455678990


def a():
	return 1;


#print(globals())
import pickle
#print(globals())
# d = dict()

d = dict(name="jiang",age=12)
print(d)

# dumps
print(pickle.dumps(d))

#b'\x80\x03}q\x00(X\x01\x00\x00\x00aq\x01K\x01X\x01\x00\x00\x00bq\x02K\x02u.'
# bytes 字节

from io import BytesIO  # 字节流
f = BytesIO(b'\x80\x03}q\x00(X\x01\x00\x00\x00aq\x01K\x01X\x01\x00\x00\x00bq\x02K\x02u.')
bl = f.read()

# w wb write binary
f = open("bytesIO.txt","wb")
pickle.dump(d,f)
f.close()

#反序列化
# r read rb binary
f=open("bytesIO.txt","rb")
d1 = pickle.load(f)
f.close()
print(d1)


# f = open("dict.txt","r")
# d2 = f.read()
# print(type(d2))
# d3 = eval(d2)   # 转义
# print(d3)
# print(type(d3))
# print(d)
# print(str(d))

# json 数据结构 ---- js javascript

import json

print(d)

jd = json.dumps(d)  # {} ---- {}
#print(type(jd))

l = [1,2,3,4,5]

jl = json.dumps(l)  # [] ---- []
print(type(jl))

t = (1,2,3,4,5)

jt = json.dumps(t)  # () ---- ()
print(jt)

a = 18
ja = json.dumps(18) # int --- int
print(ja)

b = True
jb = json.dumps(b) # True --- true
print(jb)


c = "hello world" # str ---- string
jc = json.dumps(c)
print(jc)

f = None
jf = json.dumps(f) # None -- null
print(jf)


# print(p1.__dict__)

# p2 = person.__dict__

# print(type(p2))

# p3 = dict(p2)
# print(type(p3))
# print(p3)
# print(str(p3))

# jclass = json.dumps(str(p3))
# print(jclass)

# d = dict(name="jiang",age=12)
# print(type(d))


# dictproxy --- ?

# json反序列化


class person(object):
	
	def __init__(self,name,age):
		self.name = name
		self.age = age

p1 = person("xiaoming",18)

def todict(p1):
	return {
	"name":p1.name,
	"age":p1.age
	}

jp = json.dumps(p1,default=todict)
print(jp)

# object -------> dict -----> json

# 网络通信

# json ---------> dict -----> object

def dedict(d):
	return person(d["name"],d["age"])


p2 = json.loads(jp,object_hook=dedict)
print(p2)



