# Python Functions



# calling a function

def my_function():
  q = "Hello from a function"
  print(q)

my_function()

# arguments in function

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# passing a list as an argument

def my_function(food):
  for x in food:
    print(f"{x}")

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# return values

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


# find the largest number in the given numbers

def my_function(x,y,z):
  if x>y and x>z:
    return x
  elif y>x and y>z:
    return y
  else:
    return z
print(my_function(3,6,2))
    



def sum(a, b, c):
    totalsum = a + b + c
    ikku = a * b * c  
    if totalsum % 2 == 0:
        print(f"{totalsum},even")
    else:
        print(f"{totalsum}, odd")
    if ikku % 2 == 0:
       print(f"{ikku},even")
    else:
       print(f"{ikku},odd")
(sum(5,7,8))


  
def my_function(a):
   print(a)





l =["q,w,e,r,t","wretwet","fssgrjgf"]
my_function(l)

   
   












   