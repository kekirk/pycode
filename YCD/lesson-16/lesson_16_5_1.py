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