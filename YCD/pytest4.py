#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from io import StringIO


f = open("aaa.txt","w")
f.write("test a word line \n")
f.close()

f = open("aaa.txt","a")  # append
f.write("test a new line \n")
f.close()

with open("aaa.txt","a") as f:
    f.write("=================== \n")

f = open("aaa.txt","r")
txt = f.read()
print(txt)
f.close()

f = StringIO()
f.write("HELLO \n")
f.write("WORLD \n")
print(f.getvalue())

f = StringIO("Hello\nWorld\nGoodbye")
while True:
    s = f.readline()
    if s == "":
        break
    else:
        print(s)

from io import BytesIO
f = BytesIO()
f.write("中文".encode("utf-8"))
print(f.getvalue())