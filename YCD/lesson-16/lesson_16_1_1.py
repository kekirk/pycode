

from multiprocessing import Process
import os,time
a = 0

def fun():
	pid = os.getpid()
	for i in range(9):
		global a
		a += 1
		print(str(pid)+"========="+str(a)+"\n")
		time.sleep(1)

if __name__=="__main__":
	t1 = Process(target=fun)
	t2 = Process(target=fun)
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print("end==========")