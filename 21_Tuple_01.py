# Tuple

# Tuples are used to store multiple items in a single variable.

# Allow Duplicates 

x = ("apple", "banana", "cherry", "apple", "cherry")
print(x)

# Tuple Length

y = ("apple", "banana", "cherry")
print(len(y))



# Create Tuple With One Item

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


# Tuple Items - Data Types

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)


# type()

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))


# The tuple() Constructor

ikku = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(ikku)


# Access Tuple Items

emmanual = ("apple", "banana", "cherry")
print(emmanual[1])


# Negative Indexing

wawa = ("apple", "banana", "cherry")
print(wawa[-1])


# Range of Indexes

ji = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(ji[2:5])

# Range of Negative Indexes

hj = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(hj[-4:-1])


# Check if Item Exists

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")


# Update Tuples

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Add Items

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)


# Remove Items

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)