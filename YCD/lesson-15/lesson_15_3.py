#! --*--coding:utf-8--*--
import subprocess

# nslookup  --- name server DNS

# r = subprocess.call(['nslookup','www.python.org'])
# r1 = subprocess.call(['nslookup','www.baidu.com'])
# r2 = subprocess.call(['nslookup','www.qq.com'])
# print(r)
# print(r1)
# print(r2)

# 子进程的输入和输出问题------ 进程间的通信
# map list set tuple  
# queue  ---- 有序可更改的数据结构-----消息队列
# 生产者---消费者模式

from multiprocessing import Process, Queue
import os, time, random

def fun1(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

def fun2(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    q = Queue()
    p1 = Process(target=fun1, args=(q,))
    p2 = Process(target=fun2, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.terminate()