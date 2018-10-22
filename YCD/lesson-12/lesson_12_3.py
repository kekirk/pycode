



#range

class myRange(object):
	def __init__(self,n):
		self.bk = n
		self.iv = -1

	def __iter__(self):
		return self

	def next(self):
		self.iv += 1
		if self.iv >= self.bk:
			raise StopIteration()
		return self.iv


for n in myRange(10):
	print(n)


