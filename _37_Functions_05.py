# Arbitrary Arguments, *args

# If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


# Arbitrary Keyword Arguments, **kwargs

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


#  Positional-Only Arguments

def my_function(x, /):
  print(x)

my_function(3)


# Keyword-Only Arguments

def my_function(*, x):
  print(x)

my_function(x = 3)


# Combine Positional-Only and Keyword-Only

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

