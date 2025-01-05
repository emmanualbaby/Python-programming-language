# Python Sets
thisset = {"apple", "banana", "cherry"}
print(type(thisset))


# Duplicates Not Allowed
thisset = {"apple", "banana", "cherry", "apple","ikku"}
print(thisset)


# True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)



# False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)


# len() function
thisset = {"apple", "banana", "cherry","ikku"}
print(len(thisset))


# Set Items - Data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(f"{set1},{set2},{set3}")


# Access Set Items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(f"{x}")



# Check if "banana" is present in the set
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)


# Check if "banana" is NOT present in the set
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)



# Add Set Items

# add() method
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)



# update() method
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)



# Add Any Iterable update() method
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)


