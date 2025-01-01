# Q.1 Write a Python  script that takes input from the user and displays that input back in upper and lower cases.

a = input("Enter a string: ")
print("Upper case:", a.upper())
print("Lower case:", a.lower())


# Q.2 Write a Python program to reverse a string.


a = "emmanual ikku"
vava = a[::-1]
print(vava)


# Q.3 Write a  Python program to remove characters that have odd index values in a given string.

q = "123456789987654321 emmanual"
vava =''
i = 0
while i < len(q):
    if i%2==0:
        vava+=q[i]
    i+=1
print("Modified string:", vava)




# Q.4  Write a Python program to count repeated characters in a string.
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2


q='thequickbrownfoxjumpsoverthelazydog'
x=q.count("o")
w=q.count("e")
r=q.count("u")
y=q.count("h")
f=q.count("r")
k=q.count("t")
print("o",x)
print("e",w)
print("u",r)
print("h",y)
print("r",f)
print("t",k)



# Q.5 Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restartes'
# Expected Result : 'resta$te$'


Q = 'restartes'
q = Q[0],Q[1:].replace(Q[1],"$")
print(q)






# Q.6 Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'










# Q.7 Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'








# Q.8 Write a Python program to count occurrences of a substring in a string