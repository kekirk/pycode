#! --*--coding:utf-8--*--

import sys

# sys ---- systerm
print(sys.__dict__)


sys

#sys['defaultencoding']

# __getitem__

#ascii
print(sys.getdefaultencoding())
reload(sys)
sys.setdefaultencoding("utf-8")

#元类


'中文'.encode('utf-8')

b = "ggggg"

b.encode("utf-8")

a = b'\xe4\xb8\xad\xe5\x8d\x88'
print(type(a))
# object1 type(object1) ---- object1 的类
b = a.encode('utf-8')
print(b)