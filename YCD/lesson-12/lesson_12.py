#!--*--coding:utf8--*-- 


# __slots__

class A:
	pass


a = A();


a.name = "jc"

print(a.name)



class B(object):
	__slots__=("name","age")

b = B()
b.gender = "girl"
print(b.gender)




class Student(object):
	__slots__ = ('name', 'age')

s = Student()

s.name = 'Michael' # 绑定属性'name'
s.age = 25 #

s.score = 99