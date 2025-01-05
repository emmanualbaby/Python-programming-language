# Remove Item

# remove(), or the discard() method.
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)


# pop() method
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)


# clear() method 
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)


# del keyword 
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) #this will raise an error because the set no longer exists


# Loop Sets
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
  