#字符串---常用的类型
	字符串用来表示一段文本信息，字符串是程序中使用最多的数据类型（可以存储任意的数据）
	在python中字符串需要使用引号括起来
#简单介绍对象
#对象(object<-->class)-------面向对象设计思想(OOP)------>面向切面
	python是一门面向对象(面向过程)的开发语言
	一切皆为对象
	程序运行当中，所有的数据都是存储在内存中的，然后运行
	对象就是内存中用来存储指定数据的一块区域
	对象就是一个容器，用来存储数据
	数值型、字符串、布尔值、空值
#对象的结构
	每个对象都要保存三种结构
	id（标识）
		id用来标识对象的唯一性，每一个对象都有唯一的 id
		可以通过id函数来查看对象的id
		id是由解析器生成的，id就是对象的内存地址
		对象一旦创建，id永远不能改变
	type（类型）
		类型用来标识对象所属的类型
		int str float bool。。。
		类型决定了对象有哪些功能
		通过type函数来查看对象的类型
		python是一门强类型语言，对象一旦创建类型，便不能修改
	value（值）
		值就是对象中存储的具体数据
		对于有些对象值是可以改变的
		对象分为2大类，可变对象，不可变对象
			可变对象的值可以改变
			不可变对象的值，不能改变
	变量和对象
		对象并没有直接存储到变量中，在python中变量更像是给对象起了一个别名
		变量中存储的不是对象的值，而是对象的id（内存地址）
			当我们使用变量时，实际上就是通过id查找对象
		变量中保存的对象，只有在变量重新赋值时才会改变
		变量和变量之间是相互独立的，修改一个变量不会影响另一个变量
		课后作业，定义变量画出内存图

	渐悟  顿悟
	思想--->儒(孔子-易经(无字天书（六十四卦\八卦），批注))、道(老子)、佛（六祖慧能）
	买东西  买南北  上厕所下厨房