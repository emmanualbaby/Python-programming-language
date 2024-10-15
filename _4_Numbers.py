# int
# float
# complex

# int 
x = 1 

#float
z = 20.3

# complex
s = 1j

print(x,z,s)

#type() function

x = 55
print(x,type(x))

s = 20.3
print(s,type(s))

z = 1j
print(z,type(z))



#nt, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

x = -4
print(x,type(x))
s = -6.2
print(s,type(s))
z = -5j
print(z,type(z))


#Type Conversion
x = 1 
z = 20.3
s = 1j

#convert from int to float:
x=float(x)
print(x,type(x))

#convert from float to int:
z=int(z)
print(z,type(z))

#convert from int to complex:
s = complex(s)
print(s,type(s))

#Random Number

import random
print(random.randrange(20,50))


