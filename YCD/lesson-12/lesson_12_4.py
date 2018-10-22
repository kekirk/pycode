#!--*--coding:utf8--*-- 

from enum import Enum


Month = Enum("Month",("Jan","Feb","Mar","Apr","May"))


for name,member in Month.__members__.items():
	#print(name,member,member.value)
	print(name,member.value)



class Weekday(Enum):
	Sun = 0;
	Mon = 1;
	Tue = 2;
	Wed = 3;
	Thu = 4;
	Fri = 5;
	Sat = 6;

for name,member in Weekday.__members__.items():
	print(name,member.value)
		


from enum import Enum

class Weekday(Enum):
    Sun = 0;
    Mon = 1;
    Tue = 2;
    


for it,meb in Weekday.__members__.items():
    print(it,meb.value)


print(Weekday(0))
print(Weekday.Mon.value)
print(Weekday.Mon)
print(Weekday["Mon"])

#Weekday["Mon"]=5

wd = Weekday(1)
print(wd.__dict__)

# Weekday.Mon  
print(type(Weekday.Mon))
# 

#
class Weekday():

	@classmethod
	def Mon(cls):
		mon = cls()
		mon.value = 1
		return mon

	@classmethod
	def Sun(cls):
		sun = cls()
		sun.value = 0
		return sun



print(Weekday.Mon().value)
print(Weekday.Sun().value)


# 
class Weekday(object):

	Mon = type("Mon",(object,Weekday,),{"value":1,"__str__":lambda self:"Weekday.Mon"})
	Sun = type("Sun",(object,Weekday,),{"value":0,"__str__":lambda self:"Weekday.Sun"})

print(Weekday.Mon)
print(Weekday.Mon.value)


# 
class Weekday():

	def __init__(self,**kv):    # 初始化函数 构造函数
		self.__iv = -1

		if "bk" in kv.keys():
			self.bk = kv["bk"]
		else:
			self.bk = False
		if "value" in kv.keys():
			self.value = kv["value"]
		if "name" in kv.keys():
			self.name = kv["name"]
		if self.bk:
			return;
		#if kv["value"] != None:
		#	self.value = kv["value"]
		#if kv["name"] != None：
		#	self.name = kv["name"]
		self.Mon = Weekday(name="Mon",value=1,bk = True)
		self.Sun = Weekday(name="Sun",value=0,bk = True)

		self.wkday= [self.Mon,self.Sun]

	def __str__(self):
		return "Weekday."+self.name


	def __iter__(self):
		return self


	def next(self):
		self.__iv += 1
		if self.__iv >= len(self.wkday):
			raise StopIteration()

		return (self.wkday[self.__iv],self.wkday[self.__iv].value)

	
weekday = Weekday()
print(weekday.Mon)
print(weekday.Sun)
print(weekday.Mon.value)


for d,v in weekday:
	print(d)
	print(v)


d = {"a":1,"b":2}

# 
class Weekday(dict):
	a = 1
	b = 2
	c = 3


week = Weekday()
#week["a"]



class Weekday():
	def __init__(self):
		self.Mon = 1
		self.Sun = 0

	def __getitem__(self,n):
		a,b,c = 1,2,3
		t = ["Sun","Mon","Tue"]
		d = {"Mon":1,"Sun":0}
		if isinstance(n,int):
			return t[n]
		elif isinstance(n,str):
			return d[n]
		elif isinstance(n,slice):
			start = n.start
			stop = n.stop
			#print(start)
			#print(stop)
			sl = []
			for x in range(start,stop):
				sl.append(t[x])
			return sl
a = list()

week = Weekday()
print(week[2])
print(week.Mon)
print(week["Mon"])
print(week[0:2])