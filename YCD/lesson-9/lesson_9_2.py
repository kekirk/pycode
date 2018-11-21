#! --*--coding:utf-8--*--
#可变序列，不可变序列 

# 数据结构：  有序 vs 无序

# 有序数据结构: 可变 vs 不可变

# 可变 list 列表
# 不可变 tuple 元组



# 字符串也是一种不可变的有序数据结构
# 
a = "12234"

print(a[0])

# 字符串不能进行更改操做
#a[0]=4


# print max("12345")
print(max(a))

print(len(a))

print(a.index("1"))


# 字符串的序列操作的应用：
# 文本解析 ------   爬虫 

# 搜索引擎----  百度 谷歌
# 搜索引擎的核心技术是什么？  ------  爬虫

# 什么是爬虫  ---  通过"计算机的程序"去抓取其他网站上的内容  ---- 抓来的内容就是文本

web_context = "aasldfjlsajdflaslk;fjasl;k compute lasjdflajsdlfa;"

web_context.index("compute") # 返回结果大于0，说明字符串当中包含这个关键词

if web_context.index("compute") > 0:
	print web_context


# 后面的课程会讲到的异常处理的问题
try:         #    测试
	web_context.index("phone")
except:      #    异常
	print "not found"