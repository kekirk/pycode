

def log(fun):
	def func(a,b):
		return fun(a,b)
	return func;


@log
def test(a,b):
	return a+b


print(test(1,2))

def handler(fun):
	def action(request):
		return fun(request)
	return action


def fun1():
	return "must_login"



def login(arg):
	def handler(fun):
		def action(request):
			if arg =="must_login1":
				return fun(request)
			else:
				return fun1();
		return action
	return handler



@login("must_login1")
def action1(request):
	return "response"


print(action1(7777))



def login(arg):
	def handler(fun):
		def action(*args,**kv):
			if arg =="must_login":
				return fun(*args,**kv)
			else:
				return fun1();
		return action
	return handler


@login("must_login")
def f1(slkdfkjl,sldjfl,jdskl,aslkdf=999):
	return 404;



