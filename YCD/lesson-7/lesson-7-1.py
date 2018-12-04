# # 1
# for a in range(100):
# 	print(a+1)


# # 2
# for a in range(100):
# 	if (a+1) % 2 == 1:
# 		print(a+1)


# # 3
# n = 0
# for a in range(100):
# 	if (a+1) % 3 != 0:
# 		n = n + a+1
# print(n)


# # 4
# def fun(a,b):
# 	for i in range(a):
# 		str = ""
# 		for j in range(b):
# 			str = str + "#"
# 		print str

# fun(3,4)

# # 5
# def fun(a):
# 	for i in range(a):
# 		str=""
# 		for j in range(i+1):
# 			str = str+"#"
# 		print str

# fun(4)

# #1 --- 5

# #1 --- 4
# #2 --- 3
# #3 --- 2
# #4 --- 1

# # 6
# def fun(a):
# 	for i in range(a):
# 		str=""
# 		for j in range(a-i):
# 			str = str+"#"
# 		print(str)
# fun(5)
# fun(4)


# # 7
# def fun(a):
# 	for i in range(a):
# 		line=""
# 		for j in range(i+1):
# 			line = line+str((j+1))+"*"+str((i+1))+"  "
# 		print (line)

# fun(9)



# #9
# n=0
# for i in range(100):
# 	if (i+1)%6==0:
# 	 	n = n+1
# 	 	print(i)
# print(n)


# # 10
# a = 3000
# i=0
# while a >= 5:
# 	i = i + 1
# 	a = a-(a/2)
# print(i)

# # 11

# def fun(a):
# 	for i in range(a):
# 		str=""
# 		for j in range(i+1):
# 			str = str+"#"
# 		if (i+1)%2 == 1:
# 			print(str)
# 	str = ""
# 	for i in range(a+1):
# 		str = str+"#"
# 	print(str)
# 	for i in range(a):
# 		str=""
# 		for j in range(a-i):
# 			str = str+"#"
# 		if(i+1)%2 == 1:
# 			print(str)
# fun(5)



# # 12
# #     *
# #    * *
# #   * * *
# #  * * * *
# # * * * * *
# #  * * * *
# #   * * *
# #    * *
# #     *
# # 
# # 1 -- 4 -- 1 -- 0 
# # 2 -- 3 -- 1 -- 1 
# # 3 -- 2 -- 1 -- 2    
# # 4 -- 1 -- 1 -- 3
# # 5 -- 0 -- 1 -- 4

# # 1 -- 1 -- 1 -- 3
# # 2 -- 2 -- 1 -- 2
# #                1
#         #        0

# for a in range(5):
# 	n = 5 - (a+1)
# 	p1 = " "*n+"*"
# 	p2 = " *"*a
# 	print(p1 + p2)

# for a in range(4):
# 	n = a+1
# 	p1 = " "*n+"*"
# 	p2 = " *"*(4-(a+1))
# 	print(p1+p2)


# #13
# for a in range(1000):
# 	b = a+1 
# 	c = 0
# 	for i in range(b):
# 		if b%(i+1)==0:
# 			c = c+ i+1
# 	if c == 2*b:
# 		print(b)


# #13
# for a in [6,28,496]:
# 	b = a
# 	c = 0
# 	for i in range(b):
# 		if b%(i+1)==0:
# 			print(i+1)
# 			c = c+ i+1
# 	if c == 2*b:
# 		print("~~~~~~~",b)


# #14
# for a in range(1000,10000):
# 	b = str(a)
# 	#print b
# 	n = -1
# 	for i in b:
# 		n = n+1 
# 		m = -1
# 		for j in b:
# 			m = m+1
# 			if m != n:
# 				c1 = int(b[n]+b[m])
# 				q= -1
# 				for e in b:
# 					q = q+1
# 					if q!=n and q!=m:
# 						t = -1
# 						for s in b:
# 							t = t+1
# 							if t!=m and t!=n and t!=q:
# 								c2 = int(b[q]+b[t])
# 								if c1*c2 == a:
# 									print(str(a)+"="+str(c1)+"*"+str(c2))







# #15
# for a in range(100,1000):
# 	b = str(a)
# 	b1 = int(b[0])*int(b[0])*int(b[0])
# 	b2 = int(b[1])*int(b[1])*int(b[1])
# 	b3 = int(b[2])*int(b[2])*int(b[2])
# 	if a == int(b1)+int(b2)+int(b3):
# 		print a




# #16
# while True:
# 	for a in range(100):
# 		print a
# 		if a == 5:
# 			break
# 	break


# #18
# d = 10000.0
# for i in range(5):
# 	d = d*(1+0.003)
# 	print d

# #18
# d = 10000.0
# print(d*(1+0.003)**5)


# #19
# c = 0
# for a in range(100):
# 	b = a+1
# 	if b%3==0:
# 		#print b
# 		c = c+b
# print c

# #20
# c = 0
# for a in range(1000):
# 	b = a+1
# 	if b%7!=0:
# 		#print b
# 		c = c+b
# print c


# #21
# for a in range(10,21):
# 	pass

# a=10
# b=0
# while a<=20:
# 	b = b+a
# 	a=a+1
# print(b)

# #22
# def fun(a):
# 	for i in range(a):
# 		n = i+1
# 		if a%n==0:
# 			print(n)

# fun(4)


#23
# def fun(a):
# 	n = True
# 	if a == 1 or a==2:
# 		print a
# 	else:
# 		for i in range(2,a):
# 			if a%i==0:
# 				n = False
# 				print " not"
# 				break
# 		if n:
# 			print "yes"

# fun(4)

# #24
# def fun(a):
# 	b = str(a)
# 	n = 0
# 	e = 0
# 	for i in b:
# 		if i> e:
# 			e = i
# 		if int(i)==0:
# 			n = n+1
# 	print(n)
# 	print(e)

# fun(10034)



# #25
# a = 1020;
# n = 0
# while a>0:
# 	n = n+1
# 	a=a/2-2
# print(n)


# #26
# e=1;
# for i in range(9):
# 	e = (e+1)*2

# print(e)


# #27
# def fun(c):
# 	n = 0
# 	while n>5:
# 		n = n+1
# 		if c<0:
# 			break


#29
def fun(cs):
	sum=0
	n = 0
	for c in cs:
		if c>=80:
			n = n+1
			sum = sum + c
		else:
			continue
	print(sum/n)

fun([80.0,87.0,83.0,70.0,60.0])



# #30
# for n in range(1,101):
# 	for j in range(1,101-n):
# 		for e in range(1,101-n-j):
# 			if (n+j+e) == 100 and 5*n+3*j+(1/3*e)==100:
# 				print(n,j,e)

# #36
# def fun(n):
# 	s = 0
# 	for i in range(2,n+2):
# 		s = s + i/(i-1)
# 	print(s)

# fun(8)


# #37
# d = 13
# n = 0
# while d<15:
# 	n = n+1
# 	d = d*(1+0.07)
# print(n)



# #38
# n = 1
# for i in range(2,51):
# 	n = n+(i-1)

# print(n)



# #42
# n = 1000
# e =0
# while n>=38:
# 	e=e+1
# 	n= n-38
# print(e)
# print(n)

# print(38*26)

# #43
# j = 49
# e = 1
# while j>=1:
# 	j = j - 1
# 	e = e + 1
# 	if j*2+e*4==160:
# 		print j
# 		print e

# print(20*2+30*4)



