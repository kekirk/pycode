#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import subprocess

# r = subprocess.call(["nslookup", "www.baidu.com"])

# print(r)

from Multiprocessing import Process, Queue
import os, time, random

def fun1(q):
    print(os.getpgid())
    for value in ['a','b','c','d']:
        q.put(value)
        time.sleep(random.random())

def fun2(q):
    print(os.getpgid())
    while  True:
        value=q.get(True)
        print(value)

if __name__=="__main__":
    q =Queue()
    p1 = Process(target=fun1,args=(q,))
    p2 = Process(target=fun2,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.terminate()
