#if 语句的练习
#	1、编写一个程序，获取用户输入的整数，判断是奇数还是偶数
a = int(input("请输入一个整数："))
if a % 2 == 0:
	print("偶数")
else:
	print("奇数")
#	2、编写一个程序，检查任意年是否是闰年
year = int(input("请输入年份："))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
	print("该年为闰年")
else:
	print("不是闰年")
#	3、计算狗的年龄  狗的年龄是5岁，相当于人的年龄是多少？  1==10.5      2==21   3==21+4    4==21+4+4
dog_age = int(input("请输入狗的年龄:"))
if dog_age > 0:
	#计算
	if dog_age <= 2:
		print("相当于人的年龄:",dog_age * 10.5)
	else:
		a = 2*10.5
		#计算年龄的核心算法
		a += (dog_age - 2) * 4
		print("相当于人的年龄",a)
else:
	print("请输入合法的年龄!")

#	4、判断成绩，显示不同的奖励
score = float(input("请输入成绩："))
if score == 100:
	print("奖励一台车")
elif score >= 80 and score <= 99:  # 80 <= score <= 99
	print("奖励iphone")
elif score >= 60 and score <= 79:
	print("奖励一顿饭")
#	5、女方家长要嫁女儿，必须要有条件，1，财富10000000    2，帅    3，身高180
a = 10000001
b = True
c = 181
if a >= 10000000 and b == True and c > 180:
	print("一定要嫁给他")
elif a >= 10000000 or b == True or c > 180:
	print("比上不足比下有余")
else:
	print("不嫁")
#	6、从键盘输入年、月、日判断这一天是当年的第几天
year = int(input("请输入年："))
month = int(input("请输入月："))
day = int(input("请输入日："))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
	month_2 = 29
else:
	month_2 = 28

if month == 1:
	print("是当年的第: %s 天"%day)
elif month == 2:
	print("是当年的第: %s 天"%(31+day))
elif month == 3:
	print("是当年的第: %s 天"%(31+month_2+day))
elif month == 4:
	print("是当年的第: %s 天"%(31+month_2+31+day))
elif month == 5:
	print("是当年的第: %s 天"%(31+month_2+31+30+day))

if score % 3 == 0 or score % 5 == 0 or score % 7 == 0:
	print("可以被3或5或7整除")

print("平方值：",score ** 2)
print("立方值：",score ** 3)

#定义3个数，求其中的最大值
a = 30
b = 20
c = 10

max_1 = c if c > b else (a if a > b else b)
print(max_1)
print(max(a,b,c))


min_1 = c if c < b else (a if a < b else b)
print(min_1)
print(min(a,b,c))
