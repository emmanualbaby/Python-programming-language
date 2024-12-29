# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# Arithmetic Operators

a = 6
b = 3

sum = a+b
# # print('sum of ',a,'and',b,'is',sum)
print(f"sum of {a} and {b} is {sum}")

subtract = a-b
print(f"difference : {subtract}")

mult = a*b
print(f'Product : {mult}')

div = a//b
print(f"div : {div}")

divfloat = a/b
print(f"divfloat : {divfloat}")

rem = a%b
print(f"remainder : {rem}")

pow = a**2
print(f"sqr : {pow}")


# Comparison operators

a = 10
b = 7

print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)

# Logical operators

print(b>5 and b<10)
print(b>8 or b<10)

print(not b>5)

# Identity operators

a = 10
b = 7

print( a is b)
print( a is not b)


# Membership operators

stri = 'Emmanual'
print('E' in stri)
print('e' in stri)
print('a' not in stri)
print('b' not in stri)

# Bitwise operators
# AND
             # 16  8   4  2  1
x = 2        # 0   0   0  1  0  
y = 3        # 0   0   0  1  1
             # 0   0   0  1  0
print(x&y)

# OR
             # 16  8   4  2  1
x = 2        # 0   0   0  1  0  
y = 3        # 0   0   0  1  1
             # 0   0   0  1  1
print(x|y)

#XOR

             # 16  8   4  2  1
x = 2        # 0   0   0  1  0  
y = 3        # 0   0   0  1  1
             # 0   0   0  0  1
print(x^y)

#NOT
             # 16  8   4  2  1
x = 2        # 0   0   0  1  0  
             # 1   1   1  0  1
print(~x)


# left shift
             # 16  8   4  2  1
x = 2        # 0   0   0  1  0 
             # 0   1   0  0  0
print(x<<2)

# left shift
             # 16  8   4  2  1
x = 8        # 0   1   0  0  0 
             # 0   0   0  1  0
print(x>>2)



#Todo
# x = 4
# y = 5

# sum =x+y
# print(sum)
# subtract =x-y
# print(subtract)
# mult = x*y
# print(mult)
# div =x/y
# print(div)
# divfloat =x//y
# print(divfloat)
# rem =x%y
# print(rem)
# pow =x**y
# print(pow)

