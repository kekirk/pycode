#! --*--coding:utf-8--*--


# Oracle vm virtual box
# VMware

# linux 操作系统 开放源码
# 版本: redhat ubuntu centos debian
# centos
# ubuntu 用户友好 仁慈
# BIOS:Basic I/0 Server,开机引导系统
# grub2>

# 内存
# 虚拟硬盘 操作系统 硬盘格式化


# ifconfig|grep 192

# putty

# shell 脚本（壳）解释型语言  解释器
# Bash
# C Shell
# K Shell
# Shell for root

# ls /usr/bin/sh   ：list

# 输出hello world

# vim demo.sh      :vim 编辑器

# i                ：INSERT 进入可写状态 -- INSERT --

# #!/usr/bin/sh
# echo "hello world!"
# Esc
# :
# wq        :write+quit 保存更改+退出

# chmod +x demo.sh     :chmod change module +x executable

# demo.sh + 回车       :command not found  ,PATH

# ./demo.sh            : ./ 当前路径

# shell当中的变量：
# v1="hello"  中间不能有空格
# 合法变量 ： aaa  aaa_aaa _aaa aaa2
# 不合法变量: 2aaa ?aaa aaa*aaa aaa(aaa aa\aa aa/aa aa.aa
# 不合法变量: 保留字

# 定义变量
# aa=1
# aa="aa"
# aa='aa'
# 变量的使用
# echo $a
# echo ${a}

# unset a

# a="hello world"
# a='hello world'

#  echo $a,$b
# echo $a $b
# echo $a$b

# echo ${#a} 
# echo ${a:1:4}
# echo `expr index "$a" olleh`
# expr index "$a" olleh
# `$command` 执行``里面的命令，并返回执行结果

# 数组
# array1=(a b c d e f)
# array2[0]=1;array2[1]=1;array2[2]=1
# echo ${array1[0]};echo ${array1[1]};echo ${array1[2]}
# echo ${array1[@]}
# echo ${#tarray[*]}
# for t in ${tarray[*]};do echo $t; done   ----- {print t}
# 

# :<<u
# > aaa
# > aaa
# > aaa
# > u

# $0  ---当前被执行的shell程序文件名

# ./demo.sh aa bb
# echo $1
# echo $2

# a="hello"

# echo $a
# echo "$a"
# echo '$a'

echo $$     #pid
echo $?

# for t in "$@";do #数组
#   echo $t
# done

# for t in "$*";do #字符串
#   echo $t
# done