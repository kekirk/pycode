#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def f(x):
    return x**2

for a in range(10):
    print(f(a))

r = map(f,[0,1,2,3,4,5,6,7,8,9])
print(list(r))

dt = {"a":1,"b":2,"c":3}
dt1 = {"a":4,"b":5,"c":6,"d":10}
dt2 = {"c":3,"f":12}

a = list()
b = list()
c = list()
d = list()
e = list()
f = list()

def m(dt):
    print (dt.keys())
    for k in dt.keys():
        if k == "a":
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
m(dt1)
print(a)
print(b)
print("-------------")
r = map(m,[dt,dt1,dt2])
print(a)
print(b)


words = "hello cat world am book dog start cat hello cat dog"

ws = words.split(" ")

print(ws)

def mp(ws):
    res = dict()
    for w in ws:
        ld = locals()
        if w in ld.keys():
            code = str(w) + ".append(1)"
            exec(code)
        else:
            code = str(w) + " = list()"
            exec(code)
            res[w]=eval(w)
            code = str(w) + ".append(1)"
            exec(code)
    return res

rl = mp(ws)

print(rl)     