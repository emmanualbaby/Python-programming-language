# Python - String Methods

# Python String capitalize() Method

txt = "hello, i am emmanual ikku."
x = txt.capitalize()
print (x)


# Python String casefold() Method

txt = "Hello, I Am Emmanual Ikku"
x = txt.casefold()
print(x)

# Python String center() Method

txt = "Emmanual"
x = txt.center(20)
print(x)


# Python String count() Method

txt = "Hello, I Am Emmanual Ikku, Hello"
x = txt.count("Hello")
print(x)

# Python String endswith() Method

txt = "Hello, I Am Emmanual Ikku."
x = txt.endswith(".")
print(x)

# Python String expandtabs() Method

txt = "I\tK\tK\tU"
x =  txt.expandtabs(2)
print(x)

# Python String find() Method

txt = "Hello, I Am Emmanual Ikku."
x = txt.find("Am")
print(x)


# Python String index() Method

txt = "Hello, I Am Emmanual Ikku."
x = txt.index("Emmanual")
print(x)

# Python String isalnum() Method

txt = "HelloIAmEmmanualIkku0001"
x = txt.isalnum()
print(x)

# Python String isalpha() Method

txt = "HelloIAmEmmanualIkku"
x = txt.isalpha()
print(x)


# Python String isascii() Method

txt = "HelloIAmEmmanualIkku....."
x = txt.isascii()
print(x)


# Python String isdecimal() Method

txt = "4050"
x = txt.isdecimal()
print(x)


# Python String isdigit() Method    

txt = "405060"
x = txt.isdigit()
print(x)


# Python String isidentifier() Method

txt = "Hello_IAm_Emmanual_Ikku_0001"
x = txt.isidentifier()
print(x)

# Python String islower() Method

txt = "ikku i am here"
x = txt.islower()
print(x)

# Python String isnumeric() Method

txt = "543"
x = txt.isnumeric()
print(x)

# Python String isprintable() Method

txt = "Hello_IAm_Emmanual_Ikku_0001$@#"
x = txt.isprintable()
print(x)

# isspace()

txt = "        "
x = txt.isspace()
print(x)

# istitle()

txt = "Hello I Am Emmanual Ikku"
x = txt.istitle()
print(x)

#  isupper()

txt = "EMMANUAL BABY"
x = txt.isupper()
print(x)


# join()

myTuple = ("IKku", "Vava", "Vicky")
x = " , ".join(myTuple)
print(x)

# ljust()

txt = "EMMANUAL BABY Ikku"
x = txt.ljust(20)
print(x)

# lower()

txt = "EMMANUAL BABY Ikku"
x = txt.lower()
print(x)

# lstrip()

txt = "EMMANUAL BABY Ikku"
x = txt.lstrip()
print("hello ", x ,"i am ")

# Python String partition() 

txt = "EMMANUAL BABY Ikku"
x = txt.partition("BABY")
print(x)

# replace()

txt = "EMMANUAL BABY Ikku"
x = txt.replace("BABY" , "VAVA")
print(x)


# rfind()

txt = "EMMANUAL BABY Ikku"
x = txt.rfind("BABY")
print(x)

# rindex

txt = "EMMANUAL BABY Ikku"
x = txt.rindex("BABY")
print(x)

# rjust()

txt = "EMMANUAL BABY Ikku"
x = txt.rjust(35)
print(x,"EMMANUAL BABY")


# rpartition()

txt = "EMMANUAL BABY Ikku"
x = txt.rpartition("BABY")
print(x)

# rsplit()

txt = "EMMANUAL BABY Ikku"
x = txt.rstrip(",")
print(x)

#rstrip()

txt = "EMMANUAL BABY Ikku"
x = txt.rstrip()
print("hello ", x ,"i am ")

# split()

txt = "EMMANUAL BABY Ikku"
x = txt.rstrip(",")
print(x)

# splitlines()

txt = "EMMANUAL\nBABYIkku"
x = txt.splitlines()
print(x)

# startswith()

txt = "EMMANUAL BABY Ikku"
x = txt.startswith("EMMANUAL")
print(x)

# swapcase()

txt = "EMMANUALbabyIkku"
x = txt.swapcase()
print(x)

# title()

txt = "EMMANUAL baby Ikku"
x = txt.title()
print(x)

# upper()

txt = "emmanual baby ikku"
x = txt.upper()
print(x)

# zfill()

txt = "10"
x = txt.zfill(10)
print(x)
