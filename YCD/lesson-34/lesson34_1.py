

# readonly va1
#算数运算符
# expr 1 + 1
# epxr 1 \* 1
# expr 1 == 1

if [ 1 == 1 ]
then
    echo "equal"
fi

if [ 1 == 1 ];then
   echo "equal"
fi


if [ 1 == 1 ];then echo "equal";fi

# 比较运算符
if [ $a -eq $b ];then echo "eq";fi
if [ $a -ne $b ];then echo "eq";fi
if [ $a -gt $b ];then echo "eq";fi
if [ $a -lt $b ];then echo "eq";fi
if [ $a -le $b ];then echo "eq";fi
if [ $a -ge $b ];then echo "eq";fi

# 逻辑运算符
if [ $a != $b ];then echo "eq";fi
if [ $a == $b -o $a != $b ];then echo "eq";fi
if [ $a == $b -a $a != $b ];then echo "eq";fi

if [[ $a == $b && $a != $b ]];then echo "eq";fi
if [[ $a == $b || $a != $b ]];then echo "eq";fi

# 字符运算符
b=""
if [ -z $b ];then echo "null";fi
if [ -z "$b" ];then echo "null";fi

if [ -n "$b" ];then echo "not null";fi
if [ -n $b ];then echo "null";fi

if [ $b ];then echo "not null";fi

if [ $b ];then "not null";else echo "null";fi

# pwd 当前工作目录
# 文件运算符
if [ -r $file  ];then echo "read";fi
if [ -w $file  ];then echo "write";fi
if [ -x $file  ];then echo "execute";fi
if [ -d $file  ];then echo "derictory";fi
if [ -f $file  ];then echo "file";fi
if [ -s $file  ];then echo "space";fi
if [ -e $file  ];then echo "exist";fi

if test -r $file;then echo "read";fi

# echo
echo "hello"
echo \"hello\"

echo $file
echo "$file"
echo '$file'

echo "hello \n"
echo -e "hello \n"
echo -e "hello \c";echo "world"

echo "hello" > res.txt 
echo "hello" >> res.txt
# cat fileName 查看文件内容

# date 显示系统时间
echo `date`

printf "hello,world\n"
printf "%s\n" "hello"
printf "%-10s" aa bb cc dd
printf "%-10s\n" aa bb cc dd
printf "%-10s %-8s %-6s %-4s" aa bb cc dd

printf "%-.2f\n" 844
printf "%-d\n" 844

printf "%s %d\n"


printf "%s\t%s\n" hello world
printf "%s\t%s\r\n" hello world   #回车换行
printf "%s\t%s\r\n\f" hello world #换页
printf "%s\v" hello world hello shell hello baby
printf "%s\\\\\n" hello
printf "%s\b" hello

a=$((1+2))
a=$[1+1]
a=`expr 1 + 1`

# 流程控制
if [ 1 == 1]
then
	echo "=="
elif [ 1 -gt 1]
then
	echo ">"
elif [ 1 -lt 1]
then
	echo "<"
else
	echo "else"
fi

# 
for a in aa bb cc dd ee ff
do 
	echo $a
done
arr=(aa bb cc dd ee ff)
for a in ${arr[@]}
do
	echo $a
done
#
while true
do
	echo "a"
done

while :
do 
	echo "a"
done

for((;;))
do
	echo "a"
done

#
num=1
max=4
while [ $num -lt $max ]; do     echo $num;     num=$[$num+1]; done
while(( $num<$max )); do     echo $num;     num=$[$num+1]; done
while(( $num<$max )); do     echo $num;     let num++; done
# 读取键盘输入
while read FILM
do
        echo $FILM
done

# until----while
a=10

until [ $a -lt 3 ]
do
        echo $a
        let a--;
done


echo "please type one number"
read aNum
case $aNum in
        1) echo "this is 1";;
        2) echo "this is 2";;
esac

# break
# continue

# function

# redirect
# cat 文件名  

# ^ $
# X往前删除 x往后删除
# d双击 删除行 D双击 删除行不换行
# u

# yy 复制 p 粘贴

# :/if 向下
# :?if 向上

# cat users | wc -l

# wc -l aaaa > /dev/null 2>&1

# source/. 引用

# mysql linux
# nginx pythonweb
# linux 命令

# cd change directory
# mkdir  make directory
# pwd    print work directory

# yum  管理工具
# make zlib zlib-devel gcc-c++ libtool openssl openssl-devel

# PCRE
# wget http://downloads.sourceforge.net/project/pcre/pcre/8.35/pcre-8.35.tar.gz

# tar -zxvf 

# x : 从 tar 包中把文件提取出来
# z : 表示 tar 包是被 gzip 压缩过的，所以解压时需要用 gunzip 解压
# v : 显示详细信息
# f xxx.tar.gz : 指定被处理的文件是 xxx.tar.gz