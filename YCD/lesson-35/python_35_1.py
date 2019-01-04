# 因此改用pcre来解决C语言中使用正则表达式的问题(perl)

# Apache HTTP
# R脚本语言

# Nginx内部对Pcre库进行了再次封装，具体在src/core/ngx_regex.c文件中。nginx_regex_*函数基本上对pcre所有的接口都进行了二次封装。其中最关键的是对内存的处理，
# 该内存处理采用了Nginx内置的内存池概念。

# nginx的rewrite伪静态匹配规则用到正则，pcre就用来干这个。

# rewrite指令的功能就是，使用nginx提供的全局变量或自己设置的变量，
# 然后结合正则表达式和标志位实现url重写以及重定向。
# rewrite指令只能放在server、location或if中，
# 并且只能对域名后边的除去传递的参数外的字符串起作用，
# 例如 http://ywnds.com/a/we/index.php?id=1&u=str，
# 只对/a/we/index.php重写，语法如上面所示。

# http://nginx.org/download/nginx-1.6.2.tar.gz

# make & make install

# /home/hadoop/nginx/pcre-8.35/pcre.h
# /usr/include/pcre.h
# /usr/local/include/pcre.h

# vim ngx_regex.h
# #include <pcre.h>


creating objs/Makefile

Configuration summary
  + using PCRE library: /home/hadoop/nginx/pcre-8.35
  + using system OpenSSL library
  + md5: using OpenSSL library
  + sha1: using OpenSSL library
  + using system zlib library

  nginx path prefix: "/nginx"
  nginx binary file: "/nginx/sbin/nginx"
  nginx configuration prefix: "/nginx/conf"
  nginx configuration file: "/nginx/conf/nginx.conf"
  nginx pid file: "/nginx/logs/nginx.pid"
  nginx error log file: "/nginx/logs/error.log"
  nginx http access log file: "/nginx/logs/access.log"
  nginx http client request body temporary files: "client_body_temp"
  nginx http proxy temporary files: "proxy_temp"
  nginx http fastcgi temporary files: "fastcgi_temp"
  nginx http uwsgi temporary files: "uwsgi_temp"
  nginx http scgi temporary files: "scgi_temp"


# http uwsgi

# uWSGI是一个Web服务器，
# 它实现了WSGI协议、uwsgi、http等协议。
# Nginx中HttpUwsgiModule的作用是与uWSGI服务器进行交换。
# WSGI是一种Web服务器网关接口。它是一个Web服务器
# （如nginx，uWSGI等服务器）
# 与web应用（如用Flask框架写的程序）通信的一种规范。

# Nginx(HttpUwsgiModule)--uWGSI(uwsgi)--Flask(pythonWeb)

# WSGI是一种通信协议。
# uwsgi是一种线路协议而不是通信协议，在此常用于在uWSGI服务器与其他网络服务器的数据通信。
# 而uWSGI是实现了uwsgi和WSGI两种协议的Web服务器。

# make & make install

# /path/to/nginx -v

# 配置
# /path/to/nginx.conf
# ./nginx -t

#  ps -aux

# 作用
# 静态页面服务器

# ./nginx -s stop
# ./nginx
# ./nginx -s reopen

# nginx 反向代理
# 什么是代理服务器？
# 代理通常用于在多个服务器之间分配负载，
# 无缝地显示来自不同网站的内容，或者通过HTTP以外的协议将请求传递给应用服务器

# FastCGI，uwsgi，SCGI和memcached。

# uwsgi
# pip install uwsgi

# #include <Python.h>

# yum install python-devel.x86_64 

# flaskappbuilder flask django

# wget http://projects.unbit.it/downloads/uwsgi-latest.tar.gz

#  netstat -tulpn

# uwsgi --http :8080 --wsgi-file web.py
# uwsgi --http :8080 --wsgi-file web.py --master --processes 4 --threads 2 

# 80(nginx) --- 8080(uwsgi)

# 404?
# socket(ip:port)   通信协议(http,uwsgi)
# uwsgi --socket :8080 --wsgi-file web.py


# location / {
#             root   html;
#             index  index.html index.htm;
#         }
# location /uwsgiweb {
#                 include uwsgi_params;
#                 uwsgi_pass 127.0.0.1:8080;
#         }
# location /httpweb {
#                 proxy_pass http://127.0.0.1:7070;
# }
# location /tomcatweb {
#                 proxy_pass http://127.0.0.1:9090;
# }

# proxy_buffers

# chrome --- nginx -- http -- web.py 
# 异步 proxy_buffers off
# 同步

# response
# header
# body

# proxy_buffering on;
# proxy_buffers 16 4k; # body
# proxy_buffer_size 2k; # header


# bind ip

# 公网ip 内网ip

# public web
# private web