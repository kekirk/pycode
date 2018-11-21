import socket,threading
from multiprocessing import Process

def write(sock,addr):
	while True:
		instr = raw_input("                            input__:")
		sock.send(Bytes(instr))

def read(sock,addr):
	while True:
		word = sock.recv(1024).decode("utf-8")
		if word=="exit":
			break
		print("\n"+word+"\n")
		print("                            input__:")

def session(sock,addr):
	speak = threading.Thread(target=write,args=(sock,addr))
	listen = threading.Thread(target=read,args=(sock,addr))
	speak.start()
	listen.start()
	speak.join()
	listen.join()
	print("finish")


if __name__=="__main__":
	s = socket.socket()
	s.bind(("127.0.0.1",800))
	s.listen(5)
	while True:
		sock,addr = s.accept()
		p = threading.Thread(target=session,args=(sock,addr))
		p.start()