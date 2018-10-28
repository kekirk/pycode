#! --*--coding:utf-8--*--

#
import os
print(os.path)
print(os.path.abspath("."))


# cd change directory 
# .. 上一层目录
d1= os.path.abspath(".")

d2 = os.path.join(d1,"aaa.txt")

#mkdir vippython

# make directory
#
#os.mkdir("testmkdir")

# rm remove directory
#os.rmdir("testmkdir")


print(d1)

print(os.path.split(d1))
# split 拆分
# split ext --- extend
print(os.path.splitext(d2))

# f = open("newfile.txt","w")
# f.close()
#os.rename("newfile.txt","newfile2.txt")
#os.remove("newfile2.txt")


print(os.listdir("."))

print(os.path.isdir(d2))


print([ x for x in os.listdir(".") if os.path.isdir(x)])


print([ x for x in os.listdir(".") if not os.path.isdir(x)])


print([x for x in os.listdir(".") if os.path.isfile(x) and os.path.splitext(x)[1]==".py"])