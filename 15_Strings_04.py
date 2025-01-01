
# Q.1 find even numbers and odd numbers


q = "Hello I Am 651651651Emmanual Ikku 0001 !!!!"
ec=0
oc=0
os=''
es=''
for i in q:
    if i .isnumeric():
        i = int(i)
        if i%2==0:
            ec=ec+1
            os=os+str(i)
        else:
            oc=oc+1
            es=es+str(i)

print(ec,oc)
print(os,es)
    

# Q.2 find odd then add total sum of odd sum 


a = "Hello I Am 651651651Emmanual Ikku 0001211 !!!!"
tc=0
for i in a:
    if i.isnumeric():
        i=int(i)
        if i%2!=0:
            tc=tc+i
print(tc)
if tc %2==0:
    print("sum of odd numbers is even ")
else:
    print("sum of odd numbers is odd")



# for loop

a = "Hello I Am 651651651Emmanual Ikku 0001211 !!!!"
for i in range(len(a)):
    print(a[i],end=' ')


# while loop  

a = "Hello I Am 651651651Emmanual Ikku 0001211 !!!!"
i=0
while i<len(a):
    print(a[i],end=" ")
    i=i+1


# Q.3        # A,B,C =1,2,3
             # A=1
             # B=2
             # C=3                                        # Changing the numbers to A to B

a=10
b=20
a,b=b,a
print(a,b)


# Q.1 find even numbers and odd numbers using while loop

q = "Hello I Am 651651651Emmanual Ikku 0001 !!!!"
ec = 0
oc = 0
os = ''
es = ''

i = 0
while i < len(q):
    if q[i].isnumeric():
        ikku = int(q[i])
        if ikku % 2 == 0:
            ec+=1
            os+=str(ikku)
        else:
            oc+=1
            es+=str(ikku)
    i=i+1      
print(ec, oc)
print(os, es)
