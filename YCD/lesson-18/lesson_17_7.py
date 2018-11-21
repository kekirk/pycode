#！ --*--coding:utf-8--*--
import socket,threading
from multiprocessing import Process


# 127.0.0.1 ---- 规定127.0.0.1代表本机ip


# 监听


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
	sock = socket.socket()
	#s.bind(("127.0.0.1",800))
	sock.connect(("127.0.0.1",700))
	while True:
		t = threading.Thread(target=session,args=(sock,))
		t.start()
		t.join()