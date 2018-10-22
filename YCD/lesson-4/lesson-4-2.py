#格式化字符串
a = 'hello'
#字符串的加法计算
a = 'abc'+'hhh'+'kkk'

a = 123
#字符串不能和其他类型进行加法运算，否则报错
#print("a = "+a)#在python中，报错  a = 123
print('a = ',a)

#在创建字符串时，可以在字符串中指定占位符
# %s 在字符串中表示任意字符
b = 'Hello %s'%'李白'
b = 'hello %s 您好 %s'%('李白','杜甫')
b = 'hello %1.9s'%'abcdefghijk'
b = 'hello %5s'%123.45
b = 'hello %s'%123.456
# %f 浮点数占位符
b = 'hello %.2f'%123.456
# %d 整数占位符(舍弃小数)
b = 'hello %d'%123.567
# print(b)
print('a = %s'%a)

#格式化字符串，可以通过在字符串前添加一个f来创建一个格式化字符串
#在格式化字符串中可以直接嵌入变量
c = f'hello {a} {b}'
print(c)
print(f'a={a}')

#课后练习：熟练练习以下内容
#练习：
name = 'tom'
#使用四种方式输出     欢迎  xxx 光临
#拼接
print('欢迎'+name+'光临')
#多参
print('欢迎',name,'光临')
#占位符
print('欢迎 %s 光临'%name)
#格式化
print(f'欢迎 {name} 光临')

#字符串复制(字符串和数字相乘)
a = 'abc'
a  = a * 20
print(a)

#总结：1、+ 字符串的拼接   2、 * 字符串的复制