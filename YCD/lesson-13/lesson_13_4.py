#! --*--coding:utf-8--*--

# 补充定制类

# 枚举 --- 定制类



class sys1(object):
	def __init__(self,l):
		self.l = l;

	def __getitem__(self,n):   # 默认函数
		return self.l[n]


s1 = sys1([1,2,3])
print(s1.__getitem__(1))

print(s1[1])


class sys1(object):
	def __init__(self,l):
		self.l = l;


s1 = sys1([1,2,3])
#print(s1['1'])




class mydict(object):
	def __init__(self,**args):
		self.l = args

	def __getitem__(self,n):
		return self.l[n]


# l1 = mylist(1,2,3,4,5,6,7)
# print(l1[2])

# l2 = list()
# l2.append(1)
# l2.append(2)
# print(l2[1])

d1 = mydict(a=1,b="aaa",c=3)
print(d1["b"])