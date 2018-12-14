

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