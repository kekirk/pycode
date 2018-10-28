#! --*--coding:utf-8--*--
import os, ntpath

print (os.path)
print (os.path.abspath("."))

d1 = os.path.abspath(".")

print (os.path.join(d1, "lesson_13.py"))

d2= os.path.join(d1, "lesson_13.py")
# os.mkdir("testmkdir")
# rm = "testmkdir"
# os.rmdir(rm)

print(d1)
print(os.path.split(d1))
print(os.path.splitext(d2))

print (os.listdir("."))

print(os.path.isdir(d1))

print(os.path.isdir(d2))

print([ x for x in os.listdir(".") if os.path.isdir(x)])

print([ x for x in os.listdir(".") if not os.path.isdir(x)])

# print([ x for x in os.listdir(".") if os.path.splitext(x)])
print([x for x in os.listdir(".") if os.path.isfile(x) and os.path.splitext(x)[1]==".txt"])