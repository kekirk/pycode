#! --*--coding:utf8--*--



def move(n, a, b, c):
    if n == 1:
        print('{}-->{}'.format(a,c))
        return
    move(n-1, a, c, b)  # 将汉诺塔看成最底下和其他两层，先将上面的移到B位置
    move(1, a, b, c)  # 将最底下的移到C位置
    move(n-1, b, a, c)


move(3,"a","b","c")


# java 
# 堆栈
# 先进后出