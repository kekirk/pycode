a = 10-7 #定义   赋值语句
10 + 10 # 表达式
print(a) #使用   打印语句

#print(b)# 不能使用没有进行赋值的变量
# name = input("姓名") #内置函数--input输入函数
# print(name)
# 快速注释      ctrl + ?
# python是一个动态类型的语言，可以为变量赋值任意类型的值，也可以任意修改
b = 10
b = 'tom'

c = 10 # 在python中所有的整合都为int类型
#在python中，整数的大小没有限制
d = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999 
#如果数字长度太长，可以使用下划线作为分隔符
e = 123_456_789
# 十进制的整数，不能以0开头
# f = 0123
#二进制  0b开头
f = 0b10
#八进制 0o
f = 0o10
#十六进制 0x
f = 0x10
print(f)
# 小数（浮点数） 在python中所有的小数都为float类型
g = 1.23
g = 2.34
# 注意：对浮点数进行计算时，可能会得到一个不精确的结果
g = 0.1 + 0.2
print(g)

# 在python中如何回收变量
	# 1、del 变量名-----手动回收
	# 2、自动回收-------自动
#python中的垃圾回收是自动的也可以手动
del a
print(a)
