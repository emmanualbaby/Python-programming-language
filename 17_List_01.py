# Python Lists

ikku = ["apple", "banana", "cherry"]
print(ikku)

# Allow Duplicates

vava = ["apple", "banana", "cherry", "apple", "cherry"]
print(vava)


# List Length

ivan = ["apple", "banana", "cherry"]
print(len(ivan))


# list Items - Data Types

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)


# type()

ikku = ["apple", "banana", "cherry"]
print(type(ikku))

# The list() Constructor

godu = list(("apple", "banana", "cherry"))
print(godu)


# Access Items

emmanual = ["apple", "banana", "cherry"]
print(emmanual[1])

# Negative Indexing

emmanual = ["apple", "banana", "cherry"]
print(emmanual[-1])

# Range of Indexes

god = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(god[2:5])

# step range

god = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(god[2:5:2])

# By leaving out the start value, the range will start at the first item

god = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(god[:2])

# By leaving out the end value, the range will go on to the end of the list

god = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(god[2:])

# Range of Negative Indexe

god = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(god[-2:-4])

# Check if Item Exists

vava = ["apple", "banana", "cherry"]
if "apple" in vava:
  print("Yes, 'apple' is in the fruits list")
else:
  print("No, 'apple' is in the fruits list")

