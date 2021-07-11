# id function

a = 1
b = 1.0
l = ['123']

type(l)
print(id(l), type(l))

l.append(a)
type(l)
print(id(l), type(l))