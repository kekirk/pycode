#！ --*--coding:utf-8--*--
import socket,threading
from multiprocessing import Process


# def work(sock,addr):
# 	print(sock)
# 	print(addr)
# 	while True:
# 		pass

# def tcplink(sock,addr):
# 	print("Accept new connection from %s:%s" % addr)
# 	sock.send(b"welcome")
# 	while True:
# 		data = sock.recv(1024)
# 		time.sleep(1)
# 		if not data or data.decode("utf-8")=="exit":
# 			print("exit")
# 			break
# 		sock.send("Hello ,%s" % data.decode("utf-8").encode("utf-8"))
# 	sock.close()

# client message(utf-8)   server message(unicode) message.decode(utf-8)

# main_process
# sub_thread sub_process
# 异步 ： in parallel 并行
# 同步 ： in queue 串行

# gui

def recive(sock):
	while True:
		rm = sock.recv(1024)
		print("\n"+str(rm)+"\n")
		print("                              input__:")

def send(sock):
	while True:
		instr = raw_input("                              input__:")
		sock.send(instr)

def session(sock):
		#print(sock.recv(1024))
		#sock.send(b"welcome")
	t1 = threading.Thread(target=recive,args=(sock,))
	t2= threading.Thread(target=send,args=(sock,))
	t1.start()
	t2.start()


if __name__=="__main__":
	s = socket.socket()
	# 127.0.0.1 ---- 规定127.0.0.1代表本机ip
	s.bind(("127.0.0.1",700))
	# 监听
	s.listen(5)
	while True:
		sock,addr = s.accept()
		#print(sock.recv(1024))
		#sock.send(b"welcome")
		#p = Process(target=session,args=(sock,addr))
		#p.start()
		t = threading.Thread(target=session,args=(sock,))
		t.start()


# ctrl + alt + delete


# pickle.PicklingError: Can't pickle
# pickle 无法将一个socket对象进行序列化 这是为什么？
# 这是由window操作系统导致  
# 多进程 通过os.fork() 就可以在linux当中启动一个子进程，但是在window中
# 这个方式是不行的
# 怎么在windows中解决这个bug  ---- 将多进程变成多线程



# pickle 序列化  --- 将一个python的对象，进行序列化之后，写到内存里，
# 或者写到二进制文件里，或者在网络中进行传输
# dict 字典 d = dict() tcp：面向字节流的一种传输协议
# 怎样将一个内存对象变成字节流 ：pickle进行序列化 14节课