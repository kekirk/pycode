#! --*--coding:utf-8--*--
# 2.x
# 3.x 

# I/O   

# I --- input

# O --- output


# # file处理  # 硬盘IO

# f = open("aaa.txt","r") # read
# text = f.read()
# print(text)
# f.close()


# f = open("aaa.txt","w") # write
# f.write("aaaaa \n")
# f.close()

# # f = open("aaa.txt","w+")
# # f.write("aaaaa")
# # f.close()


# f = open("aaa.txt","a") # append write
# f.write("aaaaa\n")
# f.close()



# with open("aaa.txt","a") as f:
# 	f.write("=============================")




# StringIO   # 内存IO

# python2 字符编码bug python3 优化

# 2.x
from StringIO import StringIO

output = StringIO()
output.write('First line.\n')
#print(output.getvalue())


#3.x
#from io import StringIO

#f = StringIO()
#f.write('HELLO')
#f.write("world")
#print(f.getvalue())





f = StringIO()  # 字符流
f.write("HELLO \n")
f.write("world \n")


print(f.getvalue())



class MyStringIO():
	def __init__(self,*args,**kv):   # 多态
		pass


f = StringIO("hello \n world \n goodbye\n")


while True:
	s = f.readline()
	if s == "":
		break
	else:
		print(s)



#^$\n   ---- ^ 一行的开头 $ 一行的结束   \n换行

f=open("aaa.txt","r")
while True:
	s = f.readline()
	if s == "":
		break
	else:
		print(s)

f.close()


# Bytes    ---- bit 位, 二进制的方式存储，01010101 
# 1Byte = 8bit <= 256个编码
# ASCII 编码方式， A 8bit 
# 最大的一个8bit 二进制 = 10进制的几？？？？
# 11111111 = 255
# 00000000 = 0
# 1*1+1*2+1*4+1*8+1*16+1*32。。。。。
# 1*2**0+1*2**1+1*2**2+。。。。。。1*2**8
# 999 = 9*100+9*10+9*1
# utf8 ----- 中文编码
# 我  0101000000101


# BytesIO

#import BytesIO


import sys
reload(sys)
sys.setdefaultencoding('utf8')

from io import BytesIO  # 字节流


f = BytesIO()
f.write("中文")


print(f.getvalue())


# '中文'  -----> 内存
# "" -----> 内存