#! --*--coding:utf-8--*--
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy
# ZeroDivisionError
# (try or except) and finally
try:
    a = 10/1
except:
    print("this is an exception")
finally:
    pass
    #print("it finished")


# try:
#     a = 10/0
# except ZeroDivisionError as e:
#     print(e)
# finally:
#     print("it finished")

# Exception
# OverflowError 溢出异常 int long float
# int a = 1 ; b= 2; 8bit 11111111 = 255; c = 256
# ZeroDivisionError
a = 1
b = 2
try:
    expression = (a==b)
    assert expression
except AssertionError as e:
    print("AssertionError:%s == %s" % (a,b))


# AttributeError

class test:
    name=9

t = test()
try:
    print(t.age)
except AttributeError as e:
    print(e)

# BufferError pb 序列化 反序列化的一种工具
# EOFError UNIX上为Ctrl+d，Windows上为Ctrl+Z
# import sys;
# try:
#     s = raw_input('Enter something -->');
# except EOFError: # catch EOFError
#     print '\nWhy did you do an EOF on me?';
#     sys.exit(); # exit the program
# except:   # Catch any error
#     print '\n Some error/exception occurrd.';# here, we are not exiting the program
# print 'Done';
try:
    import aaaa
except ImportError as e:
    print(e)

# LookupError
l = [1,2,3]
try:
    l[3]
except IndexError as e:
    print(e)

d = {"a":1}
try:
    d['b']
except KeyError as e:
    print(e)


try:
    l = [1,2,3]
    d = {"a":1}
    l[3]
    d['b']
except LookupError as e:
    print(e)

# MemoryError

# NameError
try:
    print(name)
except NameError as e:
    name = "xiaoming"
finally:
    print(name)

# ConnectionError
# BrokenPipeError pipe管道
# echo "aaa" | grep aaa
# import time
# f1 = open('a.txt', 'r')
# print("===========")
# time.sleep(7)
# print("===========")
# f1.read()
# f1.close()

# IsADirectoryError NotADirectoryError
# WindowsError
import os
try:
    print(os.listdir("../lesson_190"))
except WindowsError:
    pass

# PermissionError
# linux为例: rwx r:read w:write x:exec
# 111 000
# 111 --> 7 rwx
# 000 --> 0 ---
# 001 --> 1 --x
# 010 --> 2 -w-
# 011 --> 3 -wr
# 100 --> 4 r--
# 101 --> 5 r-x
# 110 --> 6 rw-
# rwxrwxrwx 777 g1 当前用户 g2 当前用户所在分组 g3 其他用户

# ProcessLookupError： subprocess

# ReferenceError：弱引用，试图访问已经垃圾回收的对象

# NotImplementedError
class A:   #
    def abfun(self):   # abstract 抽象
         raise NotImplementedError("abstract method abfun does not be implemented")

class B(A):
    pass

b = B()
#b.abfun()


# self defind Error

class mydefindError(BaseException):
    pass

def testError(args):
    if args == 0:
        raise mydefindError("args can not be 0")

#testError(0)

# TypeError
try:
    "aaa"+1
except TypeError as e:
    print(e)

# 
# UnicodeDecodeError
# UnicodeEncodeError
# python2.x 
from io import BytesIO

b = BytesIO(b"aaaa")
bs = b.read().decode("utf-8").encode("utf-8")
print(bs)

# ValueError
# f1 = open("a.txt","w")
# f1.close()

# f1 = open('a.txt', 'r')
# f1.close()
# try:
#     f1.read()
# except ValueError as e:
#     print(e)


# socket.error
# import socket
# s = socket.socket()
# try:
#     s.connect(("www.baidu.com",800))
# except socket.error as e:
#     print(e)


# warning
# how to install a package into python?
# DeprecationWarning 
# from moudle import class version过时

# Warning 所有警告类别类的基类，它是 Exception 的子类
# UserWarning 函数 warn() 的默认类别
# DeprecationWarning  用于已弃用功能的警告（默认被忽略）
# SyntaxWarning   用于可疑语法的警告
# RuntimeWarning  用于有关可疑运行时功能的警告
# FutureWarning   对于未来特性更改的警告
# PendingDeprecationWarning   对于未来会被弃用的功能的警告（默认将被忽略）
# ImportWarning   导入模块过程中触发的警告（默认被忽略）
# UnicodeWarning  与 Unicode 相关的警告
# BytesWarning    与 bytes 和 bytearray 相关的警告 (Python3)
# ResourceWarning 与资源使用相关的警告(Python3)