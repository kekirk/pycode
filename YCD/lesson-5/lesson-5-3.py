#分支 
# 公式
#  if 条件表达式（布尔表达式）:
			# 语句
			# 语句
			# 语句
#执行的流程
# if语句在执行时，会先对条件表达式进行判断，如果为True，则执行if后的语句，如果为False则不执行
# 默认情况下，if语句只会控制紧随其后的语句，如果希望if可以控制多条预计，则可以在if后跟一个代码块
# 代码块
# 	代码块中存折一组代码，同一个代码块中的代码，要么都执行要么都不执行
# if True:print("hello")
num = 11
if num > 10 :print("10")
print("aaaaa")
#python是严格检查缩进
if True:
	print("123")
	print("456")
	print("789")
print("hello")

if num > 10 or num < 20:
	print("bbbb")
if 10 < num < 20:  # num > 10 and num < 20
	print("cccccc")
#练习：输入用户名，并判断用户名是否是admin，如果是则显示欢迎管理员，如果不是则什么也不做
name = input("请输入用户名：")
if name == 'admin':
	print("欢迎管理员")
#输入年龄，如果大于18岁，则显示你已经成年了
age = int(input("请输入年龄!"))
print(type(age))
if age > 18:
	print("已经成年")
# if - else 语句
#语法
# 	if 条件表达式：
# 		代码块
# else:
# 		代码块
# 执行流程
# 	进行求值判断
# 		如果为True则执行if后的代码块
# 		如果为False则执行else后的代码块
if age > 18:
	print("成年")
else:
	print("未成年")
#if-elif-elif.......else
#语法
# 	if 条件表达式:
# 		代码块
# 	elif 条件表达式:
# 		代码块
#  elif 条件表达式:
# 		代码块
# 	[else]:
# 		代码块
# 执行流程
# 		自上向下依次条件表达式进行求值判断
# 		如果表达式为True，则执行代码块，然后结束当前流程
#		如果表达式为False，则继续向下判断，直到找到True为止
# 		如果所有表达式为False，则执行else的代码块
if age > 50:
	print("天命之年")
elif age > 40:
	print("不惑之年")
elif age > 30:
	print("而立之年")
elif age > 20:
	print("弱冠之年")
else:
	print("老年")
	if age == 19:
		print("abc")
	if age == 18:
		print("bcd")
print("over")

#if 直接之间是可以嵌套
# if age > 20:
# 	if age > 30:
# 		if age > 40:
# 			if age > 50:
# 				print("天命之年")
# 			print("不惑之年")
# 		print("而立之年")
# 	print("弱冠之年")