#! --*--coding:utf-8--*--

# 枚举


# 定制类

# map

def f(x):
	return x**2


for a in range(10):
	print(f(a))


r = map(f,[0,2,3,4,5,6,7,8,9])

l = list(r)








# reduce

from functools import reduce


def f1(x,y):
	return x+y


s = reduce(f1,[1,2,3,4])
print(s)

## mapreduce


dt={"a":1,"b":2,"c":3}
dt1 = {"a":3,"b":5,"c":8,"d":10}
dt2 = {"c":13,"f":12}


a=list()
b=list()
c=list()
d=list()
e=list()
f=list()

def m(dt):
	for k in dt.keys():
		if k =="a":
			a.append(dt["a"])
		elif k == "b":
			b.append(dt[k])
		elif k == "c":
			c.append(dt[k])
		elif k == "d":
			d.append(dt[k])
		elif k == "e":
			e.append(dt[k])
		else:
			f.append(dt[k])

r = map(m,[dt,dt1,dt2])
print(a)
print(b)


def r(x,y):
	return x+y

ar = reduce(r,a)
br = reduce(r,b)
cr = reduce(r,c)
dr = reduce(r,d)
#er = reduce(r,e)
fr = reduce(r,f)


print(ar)
print(br)



# mapreduce
# wordcount


#
words = "hello math I am a teacher I hello have I am a students cat dog apple";
words1 = "hello world I am a english I hello world I am a students cat dog apple";
words2 = "hello world I am a teacher I hello to I am a students cat dog apple";
words3 = "hello engish I am a teacher I hello world I am fom cat dog apple";

def mp(lines):
	ws = lines.split(" ")
	res = dict()
	for w in ws:
		#a = list()
		ld = locals()
		if w in ld.keys():
			code = str(w)+".append(1)"
			exec(code)
		else:

			code = str(w) + " = list()"
			exec(code)
			res[w]=eval(w)
			code = str(w)+".append(1)"
			exec(code)

	return res

mr = map(mp,[words,words1,words2,words3])


ks = set()
for m in mr:
	for k in m.keys():
		ks.add(k)


for k in ks:
	exec(str(k)+"=list()")



def mp2(me):
	for m in me.keys():
		v = me[m]
		exec(str(m)+".extend("+str(v)+")")

map(mp2,mr)


# for k in ks:
# 	reduce(r,eval(k))

wcount = dict()

def rt(k):
	rd = reduce(r,eval(k))
	wcount[k]=rd


r = map(rt,ks)

print(wcount)




#{'a': 7, 'apple': 4, 'world': 4, 'I': 12, 'am': 8, 'dog': 4, 'cat': 4, 'to': 1, 'teacher': 3, 'students': 3, 'have': 1, 'english': 1, 'fom': 1, 'engish': 1, 'hello': 8, 'math': 1}





# def cot(x,y):
# 	return x+y

# for m in mr:
# 	print(m)



# for m in mr:
# 	reduce(cot,m)













