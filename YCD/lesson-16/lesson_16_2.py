#! --*--coding:utf-8--*--
import threading,time
lock = threading.Lock()

# 线程和线程之间变量共享，但是共享的是全局变量，不是局部变量
ticket = 100

def sell():
	count=0
	tname=threading.current_thread().name
	for i in range(100):
		#lock.acquire()
		global ticket
		if ticket<1:
			pass
		else:
			ticket -= 1
			count += 1
		#lock.release()
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




# GIL