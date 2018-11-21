#数据类型转换
#类型转换的四个函数 int()  float()   str()   bool()-------bin()  hex()  chr()
#int() 可以将其他的对象转换为整型
#print(1+False)# 1
a = True
a = False
a = int(a)
#int() 函数不会对原来的变量产生影响，它是对象转换为指定的类型并将其作为返回值返回
#规则
# 	True  --> 1    False --> 0
#  字符串:合法的整数字符串，直接转换为对应的数字
# 				如果不是一个合法的整数字符串，则报错
#  浮点数：直接取整，舍弃小数部分
# 注意：对于其他不可转换为整数的对象，报错

a = '123'
a = int(a)

a = 11.6
a = int(a)

# a = None
# a = int(a)

#float()浮点数
a = 1
a = float(a)

# bool() 可以将对象转换为布尔值，任何对象都可以转换为布尔值
#规则：对于所有表示空的对象都会转换为False,其余的转换为True   哪些表示空：0、None、''
a = -100
a = bool(a)

a = 0
a = bool(a)

a = ''
a = bool(a)

a = None
a = bool(a)

a  = 'abc'
a = bool(a)

print('a=',a)
print('a=',type(a))

# 课后练习：熟练使用类型转换函数

print("=="*20)

#比较运算符的补充
# ==  ！=   对象值的比较，而不是id
# 成员运算符
# is
# is not
result = 1 is True
result = 1 is not True
print(result)
print(id(1),id(True))

print("==="*20)
#逻辑运算符补充
# and(短路与) or(短路或) not
True and print("111") #左边是True，会运行右边所以print执行了  True and True = True    True and False = False    False and True = False    False and False = False
False and print("222")#左边是False，右边不执行
print("333") and True
print("3334") and False
False or print("444")# False or False = False   True or False = True   False or True = True    True or True = True
True or print("555")
print("5551") or False

print("==="*20)
#非逻辑运算
# 非布尔值的与、或运算
# 	当对非布尔值进行与运算时，python会将其当作布尔值运算，最终会返回原值
result = 1 and 2 #2   True and True
result = 1 and 0 #0   True and False
result = 0 and 1 #0   False and True
result = 0 and None #0 False and False
# 与运算符的规则
# 	与运算符找False的，如果第一个值为False，则不看第二个值
# 	如果第一个是False，则直接返回第一个值，否则返回第二个值
# 或运算符的规则
# 	或运算符找True，如果第一个值为True，则不看第二个值
#	如果第一个值是True，则直接返回这个值，否则返回第二个值

result = 1 or 2 # 1   True or True
result = 1 or 0 # 1   True or False
result = 0 or 1 # 1   False or True
result = 0 or None # None  False or False
print(result)
print("=="*20)
#三元运算符（条件运算符）
# 语法：语句1 if 条件表达式(布尔表达式) else 语句2
#	执行的流程
# 	条件运算符在执行时，会先对条件表达式进行求值判断
# 	如果判断结果为True，则执行语句1，并返回执行结果
# 	如果判断结果为False，则执行语句2，并返回执行结果
# print('hello') if True else print("welcome")
a = 30
b = 50
print("a大") if a > b else print("b大")
#获取a和b之间的最大值
max = a if a > b else b
print(max)
#课后练习：a b c 三个变量，求出其中的最大值
