


class iterableClass(object):
	def __init__(self,bk):
		self.bk = bk
		self.a = 0
		self.b = 1
		self.c = 0
		self.iv = 0



	def __iter__(self):
		return self


	def next(self):
		self.iv += 1
		if self.iv == 1:
			return 0
		elif self.iv == 2:
			return 1;
		else:
			self.c = self.a +self.b
			self.a = self.b
			self.b = self.c
		if self.iv > self.bk:
			raise StopIteration()
		return self.c


for n in iterableClass(20):
	print(n)