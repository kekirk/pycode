#! --*--coding:utf-8--*--
import time
import datetime

t = time.time()
print(t)
print(int(t))

print(t*1000)
print(int(t*1000))

#print(datetime.datetime.now())
print(time.localtime(t))
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(t)))

# http://www.runoob.com/redis/strings-getbit.html
# bitmap 位图索引
# bloom filter  --> 搜索引擎
# 255 11111111
#     10111111
#     00001111

print(hash('apple') % 8)

# n = 0000 0000

# n = 00001000

print(hash('world') % 8)

print(hash('orange') % 8) 