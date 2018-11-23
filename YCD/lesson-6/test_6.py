#定义3个数，求其中的最大值
a = 30
b = 10
c = 20

max_1 = c if c > b else (a if a > b else b)
print("max_1 =",max_1)
print("Max of a,b,c is",max(a,b,c))
print("Min of a,b,c is",min(a,b,c))

# i = 1
# while i <= 10:
#     print("hello")
#     i += 1
# else: 
#     print("------"*5)
#     print("End")
# 100以内数相加
sum = 0
i = 1
while i<=100:
    sum += i
    i+=1
print("100以内数相加")
print("SUM is",sum)

# 100以内偶数相加
sum = 0
i = 0
while i<=100:
    sum += i
    i+=2
print("100以内偶数相加")
print("SUM is",sum)

# 100以内奇数相加
sum = 0
i = 1
while i<=100:
    sum = sum + i
    i+=2
print("100以内奇数相加")
print("SUM is",sum)

# 100以内7的倍数相加及个数
print("100以内7的倍数相加及个数")
sum = 0
count = 0
i = 1
while i <= 100:
    if i %7 ==0:
        sum += i
        count +=1
        # print(i)
    i += 1
print(sum,count)

#找出1000以内所以的水仙花数
i = 100
while i <= 999:
    a = i//100
    b = i//10%10
    # b =( i - a * 100) // 10
    c = i%10
    if (a**3+b**3+c**3) == i:
        print("水仙花数:",i)
    i +=1
else:
    print("End.")
