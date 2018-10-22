#! --*--coding:utf8--*--

#
# def fibonacci(n):
# 	if n == 0:
# 		return 0
# 	elif n == 1:
# 		return 1
# 	else:
# 		return fibonacci(n-1)+fibonacci(n-2)

# 0
# 0 1
# 0 1 1
# 0 1 1 2
# 0 1 1 2 3
# 0 1 1 2 3 5

# 递归
# 自身调用自身
# 自身 ---- 函数  

# 8f 
# 6f = 5f + 4f 
# 5f = 4f + 3f
# 4f = 3f + 2f
# 3f = 2f + 1f

def febonacci(n):
	if n == 0:
		return 0;
	if n == 1:
		return 1;
	return febonacci(n-1)+febonacci(n-2)

#bprint(febonacci(8))

# 循环的特殊写法

for n in range(8):
	pass
	#print(febonacci(n))

print([febonacci(n) for n in range(8)])

def febo(n,febonacci):
	res = list()
	for x in range(n):
		res.append(febonacci(x))
	return res

res = febo(8,febonacci)
print(res)






# #10
# 0 
# 0 1
# 0 1 1
# 0 1 1 2
# 0 1 1 2 3
# 0 1 1 2 3 5
# 0 1 1 2 3 5 8
# 0 1 1 2 3 5 8 13
# 0 1 1 2 3 5 8 13 21
# 0 1 1 2 3 5 8 13 21 34






#print([fibonacci(x) for x in range(11)])
