import socket,threading
from multiprocessing import Process

def write(s):
	while True:
		instr = raw_input("                            input__:")
		s.send(Bytes(instr))


def read(s):
	while True:
		word = s.recv(1024).decode("utf-8")
		if word=="exit":
			break
		print(word+"\n")


def session(sock):
	speak = threading.Thread(target=write,args=(sock,))
	listen = threading.Thread(target=read,args=(sock,))
	speak.start()
	listen.start()
	speak.join()
	listen.join()
	print("finish")


if __name__=="__main__":
	s = socket.socket()
	s.connect(("127.0.0.1",800))
	while True:
		p = threading.Thread(target=session,args=(s,))
		p.start()
		p.join()
		print("============")
		
