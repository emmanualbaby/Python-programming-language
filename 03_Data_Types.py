# Data Types in Python
# 1. String 
# 2. Integer
# 3. Float
# 4. Complex Numbers
# 5. list
# 6. Tuple 
# 7. Range
# 8. dictionary
# 9. set
# 10.Frozenset
# 11. boolean
# 12. byte
# 13. bytearrays
# 14. memoryview
# 15. NoneType

x =10
y = 'Emmanual'

# Float
a = 2.5
print(a,type(a))

# Complex Numbers
b = 2+3j
print(b,type(b))

# List
lst = [2,3,4,5,6]
print(lst,type(lst))

# Tuple
tup = (2,3,4,5,6)
print(tup,type(tup))

# Range
r = range(5,10)
print(r,type(r))


# Dictionary
dic = {1:'one',2:'two',3:'three'}
print(dic,type(dic))

# Set
st = {2,3,7,5}
print(st,type(st))

# frozenset
frst = frozenset((4,5,6,7))
print(frst,type(frst))

# Boolean
x = True
print(x,type(x))

# Bytes
x = bytes(st)
print(x,type(x))

# bytearray
x = bytearray(st)
print(x,type(x))

# Memoryview
x = memoryview(bytes(frst))
print(x)

# NoneType  
x = None
print(x,type(x))


# Todo

q = 1.5
print(q)
e = 2 + 5j
print(e,type(e))
t = [2,3,5,6,7,8]
print(t)
j = (2,3,4,5,6)
print(j,type(j))
y = range(5,12)
print(y,type(y))
k = {6:'ikku',4:'vava'}
print(k,type(k))
m = {4,6,7,8}
print(m,type(m))
n = frozenset((4,5,6,7,8))
print(n,type(n))
r = True
print(r,type(r))
x = bytes(k)
print(x,type(x))
x = bytearray(k)
print(x,type(x))
x = memoryview(x)
print(x,type(x))
x = None
print(x,type(x))

