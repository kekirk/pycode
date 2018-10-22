#! --*--coding:utf-8-*--


#函数的解包

def fun(a,b,c):
	print(a);
	print(b)
	print(c)

fun(1,2,3)
fun(a=1,b=2,c=3)

t = (1,2,3)
fun(*t)

t={"a":1,"b":2,"c":3}
fun(**t)











# t=(1,2,3)

# fun(*t)


# t


# fun(**t)

