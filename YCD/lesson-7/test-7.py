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

def function(a):
    for i in range(1,a+1):
        n = a-i
        p1 = " "*n+"*"
        p2 = " *"*(i-1)
        print(p1 + p2)
    for i in range(1,a):
        n = a-i
        p1 = " "*i+"*"
        p2 = " *"*(n-1)
        print(p1 + p2)

function(5)