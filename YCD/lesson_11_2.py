#! --*--coding:utf8--*--

# 闭包  ---- 动态创建函数
# 元类  ---- 动态创建类


def createClass():
	class A:
		def run(self):
			print("running")
	return A;

B = createClass();
b = B();
b.run();


#print(type(B))
#print(isinstance(B,type))

def createClass(name):
	class A:
		def run(self):
			print("A running")

	class B:
		def run(self):
			print("B running")

	if name=="A":
		return A;
	if name=="B":
		return B;

C = createClass("A")
c = C()
c.run()

D = createClass("B")
d = D()
d.run()



# 动态创建类
E = type("E",(object,),{"a":"b"})
e = E()
print(e.a)

def fun(self):
	print(12345);

F = type("E",(object,),{"a":"b","f1":fun})   # object类,默认是一切类的父类
f = F()
f.f1()


class O:
	pass
o = O();

class O(object):
 	pass
o = O();


F = type("E",(O,),{"a":"b","f1":fun})   # object类,默认是一切类的父类
f = F()
f.f1()



# 匿名函数

H = type("E",(O,),{"a":"b","f1":lambda self,n:n**2})   # object类,默认是一切类的父类
h = H()
print(h.f1(9))
