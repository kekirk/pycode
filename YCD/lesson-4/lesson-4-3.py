#布尔值（bool）
# True  False
a = True
a = False
print('a = ',a)

#布尔值实际上也属于整型,True相当于1，False相当于0
print(1+True)

#None(空值)
#None专门用来表示不存在
b = None
print(b)

#数据类型
	#数值
		#整型
			#布尔值
		#浮点型
		#复数
	#字符串
	#空置

#检查类型
#type()内置函数，这个有返回值
c = type('123')
print(type(1))
print(type(1.5))
print(type(True))
print(type('hello'))
print(type(None))
f = 10
m = f
print(id(f))
print(id(m))