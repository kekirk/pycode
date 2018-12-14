t = (1,5,6,8,9,41,23)
# print(id(t))
print(t[2])

t = tuple([1,4,878,45])
print(t[2])

d = {"k1":12,"k2":"ABC","k3":345}
print(d)
d["n1"] = "GHH"
print(d)
d["n2"] = "BHH"
print(d)
print(d["n1"])

del d["n1"]
print(d)

d["n1"] = "HELLO"
print(d)

b = set([1,4,6,8,9,4])

print(b)

b.add("SUNN")
print(b)

# b.discard(4)
print(b)

c = set([1,3,4,"ERT"])
print(c)

m = b & c
print(m)

n = b | c
print(n)

l = b - c
print(l)

k = c -b
print(k)