# List Comprehension.


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


# Q.1 

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


# Q.2 

newlist = [x for x in fruits if x != "apple"]

print(newlist)


# Q.3

newlist = [x for x in fruits]

print(newlist)


# Q.4 

newlist = [x for x in range(10)]
print(newlist)


# Q.5

newlist = [x for x in range(10) if x < 5]
print(newlist)


# Q.6

newlist = [x.upper() for x in fruits]
print(newlist)


# Q.7

newlist = ['hello' for x in fruits]
print(newlist)


# Q.8


newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)


