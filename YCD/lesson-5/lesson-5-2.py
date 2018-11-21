#1 n = 5 m = 13
n = 5
m = 13
#方案1
# temp = n
# n = m
# m = temp
#方案2
# n = n + m
# m = n - m
# n = n - m
#方案3
n = n ^ m # ^ 位运算符     
m = n ^ m
n = n ^ m
print("n=",n,"m=",m)

#2
a = 60
print(bin(a))
print(hex(a))
#3
a = 3
b = 8
# c = a += 1  # python在赋值运算符是不能连续使用的
if a > b:
	a += 1
	c = a
else:
	b += 1
	c = b
print("a=",a,"b=",b,"c=",c)
print("a="+str(a)+"\tb="+str(b)+"\tc="+str(c))

# c =( a += 1)
# print(c)
#4
print(2 * 8)
print(2 << 3)
#5
a = 10
print(a)
#6
b = 10.1
print(b)
#7
c = True
print(c)
#8
d = a + b
print(d)
#9
import math
r = 10
f = math.pi * r * r
print(math.pi)
print(f)
#10
print(chr(65))
#16
a = 9
b = 9
print(a > b)
#19
a = 10
b = 20
c = 30
print("结果:",(True == (c < a)))
print((a >= b), (b == c))
print((a >= b) == (b == c),c < a)
print("结果:",(a >= b) == (b == c) == (c < a)) #False == False == False  = True      8 < a < 20  **********************
print((a != b) ==(a != c) == (c == a))
print(not(a > b))
#20
x = 5
print("x =",x)
x /= x + x
print(x)
x /= x + x
print(x)
x *= x
print(x)
#21
a = 1
b = 3
c = 9
m = ( a > b)  and (b < c)
print(m)
m = (a >= b) and (b == c) or (c < a)
print(m)
#22
a = 5
b = 9
print(a & b)
print(a | b)
print(a ^ b)