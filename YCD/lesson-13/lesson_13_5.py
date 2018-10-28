#! --*--coding:utf-8--*--

import sys # systerm  
import os # opretion systerm


# package 

# 文件夹/__init__.py

from mypackage.moudle1 import myclass

myobject = myclass()
print(myobject)

from mypackage import moudle1

myobject2 = moudle1.myclass()
print(myobject2)

import mypackage
myobject3 = mypackage.moudle1.myclass()
print(myobject3)
mypackage.moudle1.myfun()

from mypackage.moudle1 import myfun
myfun()

from mypackage.moudle1 import myargs
print(myargs)

import mypackage.moudle1

mypackage.moudle1.myclass()


import mypackage.moudle1 as m1
m1.myclass()

# 导入文件
import lesson_11_7 as l7

# import ----- import原理

import mypackage
mypackage.moudle1.myclass()










