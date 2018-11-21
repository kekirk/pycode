#! --*--coding:utf-8--*--

from multiprocessing import Pool,Process # 池子
#                            job1 job2 job3 job4 job5
# 进程池 ---- 一堆进程  ----- p1 p2 p3 p4
# 一个进程就是一个进程  ------ p1 p2 p3 p4 p5
import time
import random
a = 1
def Query(i):
	for b in range(100):
		global a
		a += 1

#Then we use "Async. Run" to run the tasks in parallel
# parallel---并列(异步)   ----- in queue 队列 (同步)
import os

if __name__=="__main__":
	print(os.getpid())
	p = Pool(4)
	for i in range(7):
		p.apply_async(Query,args=(i,))  #async----异步   vs 同步
	p.close()
	p.join()
	print("all process is end")







