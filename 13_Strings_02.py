# Python - String Methods

# Python String capitalize() Method

txt = "hello, i am emmanual ikku."    # Converts the first character to upper case
x = txt.capitalize()
print (x)


# Python String casefold() Method

txt = "Hello, I Am Emmanual Ikku"     # Converts string into lower case
x = txt.casefold()
print(x)

# Python String center() Method

txt = "Emmanual"                      # Returns a centered string
x = txt.center(20)
print(x)


# Python String count() Method

txt = "Hello, I Am Emmanual Ikku, Hello"  # Returns the number of times a specified value occurs in a string
x = txt.count("Hello")
print(x)

# Python String endswith() Method

txt = "Hello, I Am Emmanual Ikku."       # Returns true if the string ends with the specified value
x = txt.endswith(".")
print(x)

# Python String expandtabs() Method

txt = "I\tK\tK\tU"                       # Sets the tab size of the string
x =  txt.expandtabs(2)
print(x)

# Python String find() Method

txt = "Hello, I Am Emmanual Ikku."       # 	Searches the string for a specified value and returns the position of where it was found
x = txt.find("Am")
print(x)


# Python String index() Method

txt = "Hello, I Am Emmanual Ikku."       # 	Searches the string for a specified value and returns the position of where it was found
x = txt.index("Emmanual")
print(x)

# Python String isalnum() Method

txt = "HelloIAmEmmanualIkku0001"         # Returns True if all characters in the string are alphanumeric
x = txt.isalnum()
print(x)

# Python String isalpha() Method

txt = "HelloIAmEmmanualIkku"             # Returns True if all characters in the string are in the alphabet
x = txt.isalpha()
print(x)


# Python String isascii() Method

txt = "HelloIAmEmmanualIkku....."       # Returns True if all characters in the string are ascii characters
x = txt.isascii()
print(x)


# Python String isdecimal() Method

txt = "4050"                            # Returns True if all characters in the string are decimals
x = txt.isdecimal()
print(x)


# Python String isdigit() Method    

txt = "405060"                          # Returns True if all characters in the string are digits
x = txt.isdigit()
print(x)


# Python String isidentifier() Method

txt = "Hello_IAm_Emmanual_Ikku_0001"    # Returns True if the string is an identifier
x = txt.isidentifier()
print(x)

# Python String islower() Method

txt = "ikku i am here"                  # Returns True if all characters in the string are lower case
x = txt.islower()
print(x)

# Python String isnumeric() Method

txt = "543"                             # Returns True if all characters in the string are numeric
x = txt.isnumeric()
print(x)

# Python String isprintable() Method

txt = "Hello_IAm_Emmanual_Ikku_0001$@#"  # Returns True if all characters in the string are printable
x = txt.isprintable()
print(x)

# isspace()

txt = "        "
x = txt.isspace()                        # Returns True if all characters in the string are whitespaces
print(x)

# istitle()

txt = "Hello I Am Emmanual Ikku"          # Returns True if the string follows the rules of a title
x = txt.istitle()
print(x)

#  isupper()

txt = "EMMANUAL BABY"                    # Returns True if all characters in the string are upper case
x = txt.isupper()
print(x)


# join()

myTuple = ("IKku", "Vava", "Vicky")      # 	Converts the elements of an iterable into a string
x = " , ".join(myTuple)                
print(x)

# ljust()

txt = "EMMANUAL BABY Ikku"               # 	Returns a left justified version of the string
x = txt.ljust(20)
print(x)

# lower()

txt = "EMMANUAL BABY Ikku"               # Converts a string into lower case
x = txt.lower()
print(x)

# lstrip()

txt = "EMMANUAL BABY Ikku"                # Returns a left trim version of the string
x = txt.lstrip()
print("hello ", x ,"i am ")

# Python String partition() 

txt = "EMMANUAL BABY Ikku"                # Returns a tuple where the string is parted into three parts
x = txt.partition("BABY")
print(x)

# replace()

txt = "EMMANUAL BABY Ikku"                # Returns a string where a specified value is replaced with a specified value
x = txt.replace("BABY" , "VAVA")
print(x)


# rfind()

txt = "EMMANUAL BABY Ikku"                 # Searches the string for a specified value and returns the last position of where it was found
x = txt.rfind("BABY")
print(x)

# rindex

txt = "EMMANUAL BABY Ikku"                 # Searches the string for a specified value and returns the last position of where it was found
x = txt.rindex("BABY")
print(x)

# rjust()

txt = "EMMANUAL BABY Ikku"                 # Returns a right justified version of the string
x = txt.rjust(35)
print(x,"EMMANUAL BABY")


# rpartition()

txt = "EMMANUAL BABY Ikku"                 # Returns a tuple where the string is parted into three parts
x = txt.rpartition("BABY")
print(x)

# rsplit()

txt = "EMMANUAL BABY Ikku"                 # Splits the string at the specified separator, and returns a list
x = txt.rstrip(",")
print(x)

#rstrip()

txt = "EMMANUAL BABY Ikku"                  # Returns a right trim version of the string
x = txt.rstrip()
print("hello ", x ,"i am ")

# split()

txt = "EMMANUAL BABY Ikku"                  # Splits the string at the specified separator, and returns a list
x = txt.rstrip(",")
print(x)

# splitlines()

txt = "EMMANUAL\nBABYIkku"                  # Splits the string at line breaks and returns a list
x = txt.splitlines()
print(x)

# startswith()

txt = "EMMANUAL BABY Ikku"                 # Returns true if the string starts with the specified value
x = txt.startswith("EMMANUAL")
print(x)

# swapcase()

txt = "EMMANUALbabyIkku"                   # Swaps cases, lower case becomes upper case and vice versa
x = txt.swapcase()
print(x)

# title()

txt = "EMMANUAL baby Ikku"                 # Converts the first character of each word to upper case
x = txt.title()
print(x)

# upper()

txt = "emmanual baby ikku"                 # Converts a string into upper case
x = txt.upper()
print(x)

# zfill()

txt = "10"                                 # Fills the string with a specified number of 0 values at the beginning
x = txt.zfill(10)
print(x)

