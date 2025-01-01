# Q.1

q = "Hello I Am Emmanual Ikku 0001"
w = 0
for i in q:
    if i.isupper()==True:
      w = w+1
print(w)

# Q.2

q = "Hello I Am Emmanual Ikku 0001"
e = 0
for i in q:
   if i.isspace()==True:
      e+=1
print(e)

# Q.3 

q = "Hello I Am Emmanual Ikku 0001"
x=0
for i in q:
   if i.istitle()==True:
      x = x+1 # x+=1
print(x)

# Q.4

q = "Hello I Am Emmanual Ikku 0001"
s = ''
for i in q:
   if i.isupper()==True:
      s=s+i
print(s)

# Q.5

q = "Hello I Am Emmanual Ikku 0001"
s = ''
for i in q:
   if i.isalpha()==True:
      s=s+i
print(s)

# Q.6 Find Digit

q = "Hello I Am Emmanual Ikku 0001"
s = 0
for i in q:
   if i.isdigit()==True:
      s=s+1
print(s)

# Q.7 

q = "Hello I Am Emmanual Ikku 0001 !!!!"
spc =0
for i in q:
   if (i.isalnum()==False) and (i.isspace()==False):
      spc=spc+1
print(spc)

