#! --*--coding:utf-8--*--

# process memory独立 进程通信---消息队列
# threading memory共享 加锁

import threading,time

a = 0

def fun():
	#os.getpid()
	tname=threading.current_thread().name
	for i in range(100):
		global a
		a += 1
		print(tname+"========="+str(a)+"\n")
		time.sleep(1)
	print("end==========")


t1 = threading.Thread(target=fun,name="t1")
t2 = threading.Thread(target=fun,name="t2")
t1.start()
t2.start()
t1.join()
t2.join()
print("end==========")