# # Q.1 Write a Python program to sum all the items in a list

ikku=[4,6,8,9]
sum=0
for i in ikku:
  sum+=i
print("sum all the items in a list",sum)

# # Q.2 Write a Python program to multiply all the items in a list


ikku = [4, 6, 8, 9]
multiply = 1
for i in ikku:
    multiply*=i
print("multiply all the items in a list", multiply)

# # Q.3 Write a Python program to get the largest number from a list.


ikku = [4, 6, 8, 9,10,110]
largestnumber = ikku[0]
for i in ikku:
    if i > largestnumber:
        largestnumber = i
print("The largest number in the list is:", largestnumber)

# # Q.4 Write a Python program to get the smallest number from a list.


ikku = [4, 6, 8, 9,10,110]
smallestnumber = ikku[1]
for i in ikku:
    if i < smallestnumber:
        smallestnumber = i
print("The smallest number in the list is:", smallestnumber)



# # Q.5 Write a Python program to remove duplicates from a list

ikku = [1,2,3,4,5,6,7,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,5,5,1]
newikku = [ ]
for i in ikku:
    if i not in (newikku):
        newikku.append(i)
print("new list",newikku)


# # Q.6 Write a Python program to check if a list is empty or not.

ikku = [1,2,3,4,5,6,7,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,5,5,1]
# if len(ikku)==0:
if ikku == []:
    print("ilst is empty")
else:
    print("list is not empty ")




# # Q.7 Write a Python program to find the list of words that are longer than n from a given list of words.


z=["ikku","python","victus","hello"]
n=int(input("Enter Your number : ")) 
word=[ ]
for i in z:
    if len(i) > n:
      word.append(i)
print(word)



# # Q.8 Write a Python program to create a list by concatenating a given list with a range from 1 to n.
# # Sample list : ['p', 'q']
# # n =5
# # Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']


ikku = ['p', 'q']
n = 5
output = []
for i in range(1, n + 1):
  for vava in ikku:
    output.append(f"{vava}{i}")
print("Output list:", output)


# # Q.9 Write a Python program to compute the difference between two lists.
# # Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
# # Expected Output:
# # Color1-Color2: ['white', 'orange', 'red']
# # Color2-Color1: ['black', 'yellow']

e = ["red", "orange", "green", "blue", "white"]
w = ["black", "yellow", "green", "blue"]
s=[]
d=[]
for i in e:
    if i not in w:
        s.append(i)
for i in w:
    if i not in e:
        d.append(i)
print(s)
print(d)




# # Q.10 Write a Python program to insert a given string at the beginning of all items in a list.
# # Sample list : [1,2,3,4], string : emp
# # Expected output : ['emp1', 'emp2', 'emp3', 'emp4']

ikku=[1,2,3,4]
ikku1=["emp{}".format(i) for i in ikku]
print(ikku1)



