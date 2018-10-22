#! --*--coding:utf8--*--



# 程序= 数据结构+算法
# 算法主要在函数中实现

# 递归 ----  就是一种算法

# 10的阶乘

# 10! = 10*9*8*7*6*5*4*3*2*1
# 4! = 4*3*2*1

n = 10
for a in range(1,10):
	n *= a
print(n)

def factorial(n):
 	#b = n 
 	for a in range(1,n):     #*****
 		n *= a

factorial(10)

fl = [1,2,3,4,5,6,7,8,9,10]
def factorial(n):
	for a in fl[0:n]:  #  优化过了
		print("s")
		n += 1
		print("----",n)
factorial(5)



def factorial(n):
 	for a in range(1,n):     #*****
 		n *= a

factorial(10)


# # 递归式函数

# # 10! = 10 * 9!
# # 9! = 9 * 8!
# # 8! = 8 * 7!
# # 7! = 7 * 6！
# # 6! = 6 * 5!
# # 5! = 5 * 4!
# # 4! = 4 * 3！
# # 3! = 3 * 2!
# # 2! = 2 * 1!
# # 1! = 1

def factorial(n):
	if n == 1:
		return 1
	return n* factorial(n-1)

print(factorial(10))



