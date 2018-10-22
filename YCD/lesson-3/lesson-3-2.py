# name = input("姓名")
# age = input("年龄")  # input 返回值是一个字符串
#在python中，编写表达式时，要做到数据类型的一致性
# age = -10
# age = 10.1
# print(type(age))
# print(type(str(age)))
# print(name,90-int(age))
# 常用的 int() str() float()
#课后练习：用户年龄demo多写两次

#算术运算符
a = -10
b = 20
c = a + b
print(c)

# a = 6
# b = 4
# c = a / b
# print(c)

# a = 6
# b = 5
# c = a % b # ***********************************
# print(c)

# print(10 ** 20)

a = 6
b = 4
c = a // b
print(c)

# bool 布尔型
d = True
print(type(d))

print(a == b)
print(20 != 20)
print(10 > 8)
print(8 >= 8)

a = 10
a //= 20# a = a + 20
print(a)

a = 10 > 2
b = 100 < 1000
c = a and b# True and True = True       True and False = False     False and True = False     False and False = False
print(False or False)# True or True = True       True or False = True     False or True = True     False or False = False
print((a == 10) and b < 1000 and 100 == 100 or (5 > 2) or 1 < 10)
print(not(False))