# mylist = [1,2,3,4,5]

# def deepCopy(listname):
#     '''
#       测试功能
#     '''
#     cmd = listname + " = list()"
#     exec(cmd) 
#     # print(listname)
#     for a in mylist:
#         cmd1 = listname + ".append(a)"
#         exec(cmd1)
#     # print(listname)
#     return eval(listname)


# listA = deepCopy("listA")
# print(listA)
# # help(deepCopy)
# # code = "listname" + " = list()"
# # exec(code)
# # print(listname)

# def canNullArg(arg=2):   # 缺省 ----- 默认
#     print(arg)

# canNullArg()
# canNullArg(arg=3)
# canNullArg(8)

# def giveArgs(arg1,arg2,arg3):
#     print(arg1)
#     print(arg2)
#     print(arg3)

# print('-----------------------')
# giveArgs(1,2,3)
# print('-----------------------')
# giveArgs(arg1=1,arg3=2,arg2=3)

# def unlimitLengthSum(*args):     #Sum ---- 求和
#     print(args)
#     res = 0
#     for s in args:
#         res += s
#     return res

# print('-----------------------')
# num = unlimitLengthSum(1,2,3,4,5,7,2,9,3,7,2,8,7,5)
# print(num)

# def unlimitLength(**kvargs):
#     a = kvargs['dividend']
#     b = kvargs['divisor']
#     print(a/b)

# unlimitLength(divisor=2,dividend=4)

# a = 4

# def localArg(a):
#     print(a)

# localArg(8)

# print(globals())

# def localNameSpace(a,b,c):
#     print(locals())

# localNameSpace(1,2,3)

# def requestGlobal(b): 
#     global a
#     a = a+b
#     print(a)

# requestGlobal(8)

# print(a)

# fl = [1,2,3,4,5,6,7,8,9,10]
# def factorial(n):
#     for a in fl[0:n]:  #  优化过了
#         print("s")
#         n += 1
#         print("----",a,n)
# factorial(5)

# def factorial(n):
#     if n == 1:
#         return 1
#     return n* factorial(n-1)

# print(factorial(10))

# def fun(x):
#     return x*x

# map(fun,)

# def recursion(i):   #定义函数
#     print(i)
#     if i/2 > 1:   #判断递归条件，退出
#         re = recursion(i/2)  #递归函数自身
#         print('返回值:',re)
#     print('上层递归值：',i)
#     return i     #返回值

# recursion(10)

# def twosplit(sourceDate,findData):
#     sp = int(len(sourceDate)/2)  #序列长度
#     if sourceDate[0] == findData:
#         print('找到数据:',sourceDate[0])
#         return 0
#     else:
#         if findData in sourceDate[:sp]: #判断在左边
#             print('数据在左边[%s]' %sourceDate[:sp])
#             twosplit(sourceDate[:sp],findData)  #递归函数
#         elif findData in sourceDate[sp:]: #判断在右边
#             print('数据在右边[%s]' %sourceDate[sp:])
#             twosplit(sourceDate[sp:], findData)
#         else:
#             print('找不到数据')

# if __name__ == '__main__':
#     data = [1,2,'c',3,4,5,6,7,8,17,26,15,14,13,12,11,'a','b']
#     #data = list(range(1000000))
#     twosplit(data,'c')

# a = [[col for col in range(4)] for row in range(4)]
# for i in a:print(i)   #打印二维数组
# print('--------------------')
# for lf,rig in enumerate(a):  #循环数组，打印数组下标和元素
#     for cf in range(lf,len(rig)):  #从下标数组开始循环到列表长度 
#         tmp = a[cf][lf]      #存储列表元素中的元素
#         a[cf][lf] = rig[cf]  
#         a[lf][cf] = tmp
#     print('+++++++++++++++++')
#     for i in a:print(i)

# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)

# res = fact(5)
# print(res)

def age(n):
    if n == 1:
        return 18
    return age(n-1)+2

print(age(5))