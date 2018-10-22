from io import StringIO

f = StringIO()
f.write('HELLO')
f.write("world")
print(f.getvalue())