# 定义---列表
a = [ ]
# print(id(a))

a.append(7)
a.append(8)
a.append(9)

print(a)

# print(a[0])
# print(a[1])
# print(a[2])

# print(id(a))
# print(id(7))
# print(id(8))

# print(a)

a.append(12)
print(a)

print(a[2])

a[0] = 11
print(a)

c=[1,2]
c.extend([4,5,6])
print(c)

a.append([1,2,3])
print(a)
print(a[4])

# print(a+c)
del a[4]
print(a)