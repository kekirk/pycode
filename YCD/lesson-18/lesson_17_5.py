#! --*--coding:utf-8--*--
import socket

# 客户端
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


s.connect(("www.baidu.com",80))

s.send("GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n")

buffer= []

while True:
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break

web_content = ''.join(buffer)

print(web_content)

s.close()

# 响应头
# 响应体

# 
#test = "aa\naaa\naa"
#print(test.split("\n"))

header,html = web_content.split("\r\n\r\n")

# \r return
# \n new line
# 



