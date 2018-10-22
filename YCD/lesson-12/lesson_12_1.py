#!--*--coding:utf8--*-- 
class Fib(object):
    def __init__(self):
        self.a=0
        self.b=1 # 初始化两个计数器a，b

    def __iter__(self):   # iteration
        return self # 实例本身就是迭代对象，故返回自己

    def next(self):
    	#print("==============enter next")
        self.a=self.b
        #print(self.a)
        self.b = self.a + self.b # 计算下一个值
        #print(self.b)
        if self.a > 20: # 退出循环的条件
            raise StopIteration();   # raise 
        return self.a # 返回下一个值


fib = Fib()

for n in fib:
	print(n)



class iterableClass(object):
    def __init__(self,bk):
		self.a = 0
		self.b = 1
		self.c = 0
        self.iv = 0


	def __iter__(self):
		return self

    def next(self):
        return self.c






    # def next(self):
    #     self.c=0
    #     self.c = self.a+self.b
    #     self.a = self.b
    #     self.b = self.c
    #     if self.iv > self.bk:
    #         raise StopIteration()
    #     return self.c



for i in iterableClass(20):
	print(i)