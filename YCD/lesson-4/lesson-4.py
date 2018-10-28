s = 'hello' #定义一个字符串 char=‘a’char = ‘b’
# s = hello #把hello当成一个变量来使用了
#引号可以单引号也可以是双引号,引号不能混合使用
s = 'hello'
s = "hello"

# s = 'hello"  引号不能混合使用
#相同的引号之间不能嵌套
s = '子曰："学而时习之，不亦乐呼"'
#长字符串
#单引号或双引号不能进行跨行使用
#非要使用单引号或双引号进行跨行使用，需在每行的末尾添加     \
s = '锄禾日当午，\
汗滴禾下土，\
谁知盘中餐，\
粒粒皆辛苦'

#使用三重引号表示一个字符串'''   '''    """    """
#三重引号可以换行，并且保留字符串中的格式
s = '''锄禾日当午
汗滴禾下土
谁知盘中餐
粒粒皆辛苦
'''
#转义字符
#可以使用\作为转义字符，通过转义字符可以在字符串中使用一些特殊的内容
#例子：
#	\'  表示  '   *
#  \"	表示  "   *
#  \t 表示制表符
#  \n 表示换行
#  \\ 表示  \     *
#  \uxxxx    表示unicode编码
s = "子曰：\"学而时习之，不亦乐呼\""
s = '子曰：学而时\u2C77习之，不\n亦乐呼'
#unicode -->  utf-8(万能编码)
s = '\u2C77'
print(s)

print("Unicode: 5073 is"+" \u5073")
#课后练习：熟练使用字符串