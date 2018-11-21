#! --*--coding:utf-8--*--


#正则表达式  regular expression

import re
# \d \转义  d data

string = '007899'
st = re.match('00\d',string).span()
print(string[st[0]:st[1]])

# span --- 跨度
print(re.match('www','www.baidu.com').span())
# math默认从其实位置开始匹配
print(re.match("com",'www.baidu.com'))

# group
line = "Cats are smarter than dogs"
print(re.match(".*",line).span())
#print(line[0:26])
# \d --- 数字
# .----任意一个字符
# *不定长的数量

data="98787d867543"
print(re.match('\d*',data).span())

line = "Cats are smarter than dogs"
matchRes = re.match("(.*) are (.*) (.*)",line)
print(matchRes.group())
print(matchRes.group(1))
print(matchRes.group(2))
print(matchRes.group(3))
# 贪婪模式 vs 非贪婪模式
matchRes = re.match("(.*) are (.*?) (.*)",line)
print(matchRes.group())
print(matchRes.group(1))
print(matchRes.group(2))
print(matchRes.group(3))

# re.search
print(re.match("com",'www.baidu.com')) # 默认从起始位置匹配
print(re.search("com",'www.baidu.com')) # 不从起始位置匹配

# regular 
# 00\d*  \d -- 一个数字
# \w  ---- 一个字母或数字
print(re.match("00\w",'007'))
print(re.match("\w*","hello world").span())
print(re.match("\w*.","hello world").span())

line = "Cats are smarter than dogs"
res = re.match("(\w*) (\w*) ",line)
print(res.group())
print(res.group(1))
print(res.group(2))

# .
# \d* \d{3}
print(re.match("\d{3}","00011100203").span())
print(re.match("\d{3}","aaa11100203"))
print(re.search("\d{3}","aaa11100203").span())

# \s 一个空格
print(re.search("\s","aaaa	aaaa").span())
print(re.search("\s","aaaa aaaa").span())

# \d \d* \d{3} \d{3,8}

print(re.match("\d{3,8}","123456789").span())
print(re.search("\d{3,8}","a123456789").span())
print(re.match("\d{3,8}","12345678h").span())
# span --- (a,b) a被包含 b不包含 --- 从零开始，前闭后开

s = "123456789"
print(s[0:8])

print(re.match("\w{3}\d*","aaa"))

# None object *代表不定长---0也是可以的

# \d+
print(re.match("\w{3}\d+","aaa"))

# \d+ +代表了不包含零  [a,b]
print(re.match("\w{3}\d+","aaa123456").span())

# \d+ vs \d* +~[1,+INF) *~[0,INF)

# 进阶
#[0-9a-zA-Z]
print(re.match("[0-9a-zA-Z]",'01234abcdABCD').span())

# match 1 字符类型  2 匹配长度  [a,b)

# [0-9]  结束值<=1 其实值>=0  [0,2)
# 

print(re.match("[0-9a-zA-Z]",'abcdABCD').span())


# []
print(re.match("[0-9a-zA-Z]",'Ab2').span())

# [] --- 匹配规则是一个整体
print(re.match("[0-9a-zA-Z]",'0aA').span())

print(re.match("[0-9a-zA-Z]{3}",'0aA').span())

print(re.match("[0-9a-zA-Z]+",'0aA').span())

# |
print(re.match("(a|p|c)ython",'python').span())

print(re.match("[apc]ython",'python').span())

# [apc] == (a|p|c)
# (a|p|c)ython == [apc]ython 

# () []
print("=========================")
print(re.match("(jy|py|cy)thon",'python').span())
print(re.match("[jypycy]thon",'python'))
# () 或关系的元素可以是多个字符，
# [] 或关系的元素只能是单个字符

print(re.match("[apc0-9]",'apc9').span()) #
# (apc|0-9) (a|p|c|0-9)



print(re.match("\d{3}","01234").span())
print(re.search("\d{3}","01234").span())

# match 从开始匹配，search 不是从开始匹配,优先从开始进行匹配

# ^
print(re.search("\d{3}","a01234").span())
print(re.search("^\d{3}","a01234"))

# $
print(re.search("\d{3}$","a01234").span())

# 转义  
# \d  "\d"
print(re.search("\d","\d8").span())
print(re.search(r"\\d","\d8").span())

# split

print('a b c'.split(" "))
print('a\s+b\s+c'.split("\s+"))
# 用一种支持正则表达式的拆分
print(re.split("\s+",'a b c'))

print(re.split("\s",'a b  c'))
print("===============")
# ['a', 'b', ';', 'c']
# ['a', 'b', '', 'c']
print(re.split(";",'a;b;;;c'))
print(re.split(";+",'a;b;;;c'))

# 贪婪模式 非贪婪模式 ？
print(re.match(r'^(\d+)(0*)$', '102300').groups())
print(re.match(r'^(\d+?)(0*)$', '102300').groups())

# evel exec 
# eval --- 转义
# exec --- 解释执行 shell
# compile --- 编译

# 如果

rep = r'^(\d+)(0*)$'

web_content=""
for row in web_content:
	re.search(rep,row)

rep_cop = re.compile(rep)
print(rep_cop)

web_content=""
for row in web_content:
	re.search(rep_cop,row)
