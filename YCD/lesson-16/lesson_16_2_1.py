#! --*--coding:utf-8--*--
import threading,time
lock = threading.Lock()

# 线程和线程之间变量共享，但是共享的是全局变量，不是局部变量
ticket = 100

def sell():
	count=0
	tname=threading.current_thread().name
	for i in range(100):
		lock.acquire()
		global ticket
		if ticket<1:
			pass
		else:
			ticket -= 1
			count += 1
		lock.release()
		#print(tname+"========="+str(ticket)+"\n")
		time.sleep(1/100)
	print(tname+":"+str(count)+"\n")


t1 = threading.Thread(target=sell,name="t1")
t2 = threading.Thread(target=sell,name="t2")
t3 = threading.Thread(target=sell,name="t3")
t4 = threading.Thread(target=sell,name="t4")
t5 = threading.Thread(target=sell,name="t5")
t6 = threading.Thread(target=sell,name="t6")
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()

print("end==========")

# cpu t1 t2
# t1 t2   ticket = 89
# t1 lock global ticket ----> 87;  ticket = ticket -1 ---> 86 lock
# t2 lock global ticket ----> 88;  ticket = ticket -1 ---> 87


# GIL global interpreter Lock 
# java 4threads  ----- 4核CPU 1核/1thread 400%  -- 同时运行
# python 4threads ---- 4核CPU             100%  -- 不同时运行

# python多线程 cpu的利用率很低   .py 主进程 1核CPU 4threads 
# python多线程不适合处理cpu密集型的工作  多核运算 
# python多进程处理cpu密集型的工作 4核cpu 4ps 

# python多线程适合处理I/O密集型工作

# 爬虫 ---- 利用python代码自动读取别人网站上的数据，并保存数据
# Input Output  ---> I/O耗时，I/O等待 2秒

# python多线程
# t1 0.5秒   2秒 0.5秒  3秒  -- 15秒
# t2 0.5秒   2秒 0.5秒
# t3 0.5秒   2秒 0.5秒
# t4 0.5秒   2秒 0.5秒
# t5 0.5秒   2秒 0.5秒   5秒
