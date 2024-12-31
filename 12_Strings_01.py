# Python - Slicing Strings

# Slicing
b = "Emmanual, IKKU"
print(b[2:5])

# Slice From the Start

b = "Emmanual, IKKU"
print(b[:5])

# Slice To the End
b = "Emmanual, IKKU"
print(b[5:])

# Negative Indexing
b = "Emmanual, IKKU"
print(b[-5:-2])

# Python - Modify Strings

# Upper Case
b = "Emmanual, IKKU"
print(b.upper())

# Lower Case
b = "Emmanual, IKKU"
print(b.lower())

# Remove Whitespace
b = "     Emmanual, IKKU   "
print(b.strip())

# Replace String
b = "Emmanual, IKKU"
print(b.replace("m" , "a"))

# Split String
b = "Emmanual, IKKU"
print(b.split(","))

# String Concatenation
a = "Emmanual "
b = "Ikku"
c = a + b
print(c)

a = "Emmanual"
b = "Ikku"
c = a + " " + b
print(c)

