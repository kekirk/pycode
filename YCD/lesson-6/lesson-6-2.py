#循环
#反复执行指定的代码段
# while for
# while
#语法
# while 条件表达式:--------if 条件表达式:
# 		代码块
# 死循环----条件表达式永远为True，永远的执行代码块     while True: 代码块
#while 循环 3个要素    初始化语句 i = 1       条件表达式  i <= 10        修改初始化变量的值 i +=1
i = 1
while i >= 10:
	print("hello")
	i += 1
else: # 条件表达式为True，循环执行完之后再运行else内容        条件表达式为False，也会执行else中的内容
	print("over")

# 1+2+3+4+5.....=5050
#0+1 = 1 1+2=3 3+3=6 6+4=10 10+5=15 15+6=21
sum = 0
i = 1
while i <= 100:
	if i % 2 == 0:
		sum = sum + i
	i += 1
else:
	print(sum)

sum = 0
i = 0
while i <= 100:
	sum += i
	i += 2
print(sum)

#100以内的7的倍数之和以及个数
sum = 0
count = 0
i = 1
while i <= 100:
	if i % 7 == 0:
		sum += i
		count += 1
	i += 1
print(sum,count)

#找出1000以内所以的水仙花数   153=1**3+5**3+3**3
i = 100
while i <= 999:
	a = i // 100
	b =( i - a * 100) // 10
	c = i % 10
	if (a**3+b**3+c**3) == i:
		print("水仙花:",i)
	i += 1

#输入任意数，检查是否为素数(质数)
a = int(input("输入数字:"))
flag = True
i = 2
while i < a:
	if a % i == 0:
		flag = False
	i += 1
if flag:
	print(a,"是素数")
else:
	print(a,"不是素数")

#嵌套循环
#      ******
#      ******
#      ******
#      ******
#      ******
#      ******
i = 0
while i <=5:
	j = 0
	while j <= 50:
		print("*",end="")
		j += 1
	print()
	i += 1
#
# 		*
# 		**
# 		***
# 		****
# 		*****
# 		******
i = 1
while i <= 6:
	j = 1
	while j <=i:
		print("*",end="")
		j += 1
	print()
	i +=1
# 1*1=1
# 2*1=2 2*2=4
# 3*1=3 3*2=6 3*3=9 
# 4*1=4 4*2=8 4*3=12 4*4=16
i = 1
while i <= 9:
	j = 1
	while j <= i:
		print(" ",i,"*",j,"=",i*j,end="")
		j += 1
	print()
	i += 1
# 1- 100 所有的素数有哪些?
i = 2
while i <= 100:
	flag = True
	j = 2
	while j < i:
		if i % j == 0:
			flag = False
		j += 1
	if flag:
		print(i)
	i += 1

# break   循环的终止
# continue   跳过这次循环
# 共同点 break和continue之后不能有任何语句
i = 0
while i < 10:
	if i == 5:
		break
		print("abc")
	print(i)
	i += 1


	#循环练习 https://yiqixie.com/d/home/fcAD2b_Rrkdj44jOfLPzudiph