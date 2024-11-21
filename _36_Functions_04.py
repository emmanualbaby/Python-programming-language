# Number of Arguments

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


# Arbitrary Arguments, *args

def my_function(*kids):
  print("The youngest child is " + kids[0])

my_function("Emil", "Tobias", "Linus")


# Keyword Arguments

def my_function(child3, child2, child1):
  print("The youngest child is " + child1,child2,child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")



# Arbitrary Keyword Arguments, **kwargs

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")