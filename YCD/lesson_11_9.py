#!--*--coding:utf8--*-- 

# 文件

# 写
f = open("aaa.txt","w")  # read write
f.write("this line is writed by my code")
f.close()

# 读
f = open("aaa.txt","r")
lines = f.read()
f.close()
