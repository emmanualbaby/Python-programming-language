# Unpack Tuples
names = ("emmanual", "ikku", "emmanu")
(green, yellow, red) = names
print(f"{yellow},{green},{red}")

# Using Asterisk*

names = ("emmanual", "ikku", "emmanu","manu","wawa")
(green, yellow, *red) = names
print(f"{yellow},{green},{red}")

# Python - Loop Tuples

ikku = ("apple", "banana", "cherry")
for x in ikku:
  print(f"{x}")


# Loop Through the Index Numbers
  
ikku = ("apple", "banana", "cherry")
for i in range(len(ikku)):
 print(f"{ikku[i]}")


# While Loop
ikku = ("apple", "banana", "cherry")
i = 0
while i < len(ikku):
  print(f"{ikku[i]}")
  i = i+1 

# Join Tuples

ikku = ("emmanual","emmanu")
vava = (1,4,6)
wawa = ikku+vava
print(f"{wawa}")

# Multiply Tuples

ikku = ("emmanual","emmanu")
vava = ikku * 2
print(f"{vava}")



# Tuple count() Method
ikku = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = ikku.count(5)
print(f"{x}")


# Tuple index() Method

ikku = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = ikku.index(8)
print(f"{x}")