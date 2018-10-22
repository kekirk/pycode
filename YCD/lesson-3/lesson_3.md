#标识符---变量、函数、类
	1、规则
	2、规范
		在python中注意命名规范
		1、下划线命名法(多单词组成时，用下划线链接)
			age name max_length page_size
			课后练习：多练下划线命名法
		2、帕斯卡命名法（大驼峰命令法---多单词组成时，首字母大写）
			MaxLength PageSize
#变量
	解释：内存中的一个存户区域，这个区域有自己名称和类型、数据。可以方便使用，还可以随意更改
	python中的变量是不要声明，直接为变量赋值即可
	python是一个动态类型的语言，可以为变量赋值任意类型的值，也可以任意修改
	在python中数值分为3种：整数、小数（浮点）、复数
	整数：
		在python中所有的整合都为int类型
		在python中，整数的大小没有限制
		如果数字长度太长，可以使用下划线作为分隔符
		十进制的整数，不能以0开头
		二进制  0b开头
		八进制 0o
		十六进制 0x
	小数：
		小数（浮点数） 在python中所有的小数都为float类型
		注意：对浮点数进行计算时，可能会得到一个不精确的结果
	几个概念
		1、表达式 10 + 10
			=号，赋值符号---一定先计算右边，然后把值给左边
		2、语句
			用来完成某种功能
		3、程序
			就是由一条一条语句和一条一条表达式构成的
		4、函数
			函数就是一种语句，专门来完成特定功能的
			xxx()
			(1)内置函数

			(2)自定义函数*****
#python和sublime整合
	1、在sublime中执行python ctrl+b 自动运行
		缺点：1、中文支持不好		2、不能使用input函数
	2、使用sublimeREPL插件来运行python代码  package-control
		设置快捷键: { "keys": ["f5"], "caption": "SublimeREPL:Python", "command": "run_existing_window_command", "args":{"id": "repl_python_run","file": "config/Python/Main.sublime-menu"} },
		课后练习：安装sublimeREPL,并设置f5快捷键

#运算符
	1、算术运算符
		+ -  + - * / %(取模--取余数) **( 2 ** 3) //(整除--返回整数部分，舍弃小数部分)
	2、比较运算符
		特点：值都为布尔型  True False
		== 比较左右两边是否相等，相等返回True 否则返回False
		!=  比较左右两边是否不等，不等返回True 否则返回False
		>   左边大于右边，返回True，否则返回False
		<	 左边小于右边，返回True，否则返回False
		>= 左边大于或等于右边，返回True，否则返回False
		<= 左边小于或等于右边，返回True，否则返回False
	3、赋值运算符
		特点：先计算=号右边，然后把值给左边
		=、+=、-=、*=、/=、%=、**=、//=
	4、逻辑运算符
		特点：值都是布尔型 True False,可以链接多个布尔表达式
		and(与/并且)    True and True = True       True and False = False     False and True = False     False and False = False
		or(或/或者)       True or True = True         True or False = True         False or True = True        False or False = False
		not(非/取反)     not(True) = False   not(False) = True
		课后练习：https://yiqixie.com/d/home/fcACk-Qs-UpC7Fq-b9XNIwLRH
						 自己整理函数，写成文档，或微博
	5、身份运算符
	6、成员运算符
