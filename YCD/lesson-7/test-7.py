## 1
# for a in range(101):
#     if a != 0:
#         print(a)

## 2
# for a in range(100):
#     if a % 2 == 1:
#         print(a)

## 3
# n = 0
# for a in range(101):
#     if a % 3 != 0 :
#         print(a)
#         n = n + a
# print(n)

## 4
# def function(a,b):
#     i = 1
#     while i <= a:
#         j = 1
#         while j <= b:
#             print("#",end="")
#             j += 1
#         print("")
#         i+=1

# def function(a,b):
#     for i in range(a):
#         str_l = ""
#         for j in range(b):
#             str_l += "#"
#         print(str_l)

# l = int(input("Length is: "))
# w = int(input("Wide is: "))

# function(w,l)

# # 5
# def function(a):
#     str_l = ""
#     for i in range(a):
#         str_l += "#"
#         print(str_l)

# def function(a):
#         for i in range(a):
#             str_l = ""
#             for j in range(i+1):
#                 str_l += "#"
#             print(str_l)

# h = int(input("Height is: "))

# function(h)

# # 6
# def function(a):
#     for i in range(a):
#         str_l = ""
#         for j in range(a-i):
#             str_l += "#"
#         print(str_l)
    
# h = int(input("Height is: "))

# function(h)

# # 7
# def function(a):
#     for i in range(a):
#         for j in range(i+1):
#             print("%d*%d=%d" % ((j+1),(i+1),((i+1)*(j+1))), " ", end="")
#         print("")

# h = int(input("乘数 is: "))

# function(h)

# # 8
# def function(a):
#     ino = 0
#     for i in range(a):
#         if (i+1) % 6 == 0:
#             ino += 1
#             print(i)
#     print(ino)

# N = int(input("1到N, N is: "))

# function(N)

# # 10
# a = 3000
# n = 0
# while a >= 5:
#     a = a/2
#     print(a)
#     n += 1
# print(n)

# # 11
# def function(a):
#     for i in range(1,a+1,2):
#         str_l = ""
#         for j in range(i):
#             str_l += "#"
#         print(str_l)
#     for i in range(a-2,0,-2):
#         str_l = ""
#         for j in range(i):
#             str_l += "#"
#         print(str_l)   
#     for i in range(0,a,2):
#         str_l = ""
#         for j in range(a-2-i):
#             str_l += "#"
#         print(str_l)  

# function(7)

# # 12
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# def function(a):
#     for i in range(1,a+1):
#         n = a-i
#         p1 = " "*n+"*"
#         p2 = " *"*(i-1)
#         print(p1 + p2)
#     for i in range(1,a):
#         n = a-i
#         p1 = " "*i+"*"
#         p2 = " *"*(n-1)
#         print(p1 + p2)

# function(5)

# # 13
# for a in range(1,1001):
#     b = a
#     c = 0
#     for i in range(1,b+1):
#         if b%i == 0:
#             c = c+i
#     if c == 2*b:
#         print(b)

# for a in [6,28,496]:
#     b = a
#     c = 0
#     for i in range(1,b+1):
#         if b%i == 0:
#             print(i)
#             c = c+i
#     if c == 2*b:
#         print("--------",b)

# 14
# for a in range(1000,1100):
#     b = str(a)
#     for i in b:
#         print(i)
#     print(b)

# for a in range(1000,10000):
#     b = str(a)
#     n = -1
#     for i in b:
#         n += 1
#         m = -1
#         for j in b:
#             m += 1
#             if m != n:
#                 c1 = int(b[n]+b[m])
#                 q = -1
#                 for e in b:
#                     q += 1
#                     if q != m and q != n:
#                         t = -1
#                         for s in b:
#                             t += 1
#                             if t != m and t != n and t != q:
#                                 c2 = int(b[q]+b[t])
#                                 if a == c1 * c2:
#                                     print(str(a)+"="+str(c1)+"*"+str(c2))

# # 15
# for a in range(100,1000):
#     b = str(a)
#     b1 = int(b[0])**3
#     b2 = int(b[1])**3
#     b3 = int(b[2])**3
#     if a == int(b1)+int(b2)+int(b3):
#         print (a)

# # 16
# while True:
#   for a in range(100):
#     print(a)
#     if a == 5:
#       break
#   break

# # 18
# d = 10000.0
# for i in range(5):
#   d = d*(1+0.003)
#   print (d)

# d = 10000.0
# print(d*(1+0.003)**5)

# # 19
# c = 0
# for a in range(100):
#   b = a+1
#   if b%3==0:
#       print(b)
#       c = c+b
# print(c)

# # 20
# c = 0
# for a in range(100):
#   b = a+1
#   if b%7!=0:
#       print(b)
#       c = c+b
# print(c)

# # 21
# a = 10
# sn = 0
# while a<=20:
#     sn += a
#     a +=1
# print(sn)

# # 22
# def fun(a):
#   for i in range(1,a+1):
#       if a%i==0:
#           print(i)

# fun(45)

# 23
def function(a):
    isPrime = True
    for i in range(2,a):
        if a%i==0:
            isPrime = False
            break
    if isPrime:
        print("%d is Prime Number" %a)
    else:
        print("%d is NOT Prime Number" %a)

n = int(input("请输入数字："))
function(n)