#! --*--encoding:utf-8--*--


# socket ---- 插座 --- 网络套接字(ip+port)
# 
# AF_INT

# IPv4   IPv6   v:version v4 v6
# IPv4的ip分配算法有局限性，ip总数量有限
# IPv6 

# domain name 域名 比如：www.baidu.com www.sina.com www.qq.com
# 域名就是ip的名字 域名服务商那里去交费注册

# ping : Packet Internet Groper
# Packet 包 : 压缩包  
# 网络七层协议 
# OSI的7层从上到下分别是 
# 7 应用层 s.send() 
# 6 表示层 
# 5 会话层 
# 4 传输层 
# 3 网络层 
# 2 数据链路层 
# 1 物理层 

# server -----> 7layer--->1layer:打包
# -----> client 1layer--->7layer:解包

# port:80 web应用的默认端口


# s.send("message")
# message: 

# GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n
# 浅谈HTTP中Get、Post、Put与Delete的区别

# GET : 索取数据  ---- select
# PUT : 发送数据
# POST: 发送数据
# DELETE:删除数据 ---- delete

# PUT VS POST:
# 当我的URL可以在客户端确定的时候，就用PUT, ---- update
# 当我的URL不可以在客户端确定的时候，就用POST;  ---- insert


# request 请求

# response 回应
# HTTP/1.1 200 OK  200：状态码，非常正常；404：这个网页不存在
# Date: Fri, 02 Nov 2018 14:26:59 GMT
# Server: BWS/1.1 BWS是Baidu Web Server，是百度开发的一个web服务器
# Set-Cookie：爬虫
# 


