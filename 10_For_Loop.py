
#c++ computer program model

# for(i=10;i<21;i+2)
# {
#     print(i)
# }


for i in range(10,21,3):
    print(i)

# 	Multiplication of numbers

y = int(input("Enter Your Digit : "))
for i in range(1,11):
    r=i*y
    print(i,"x",y,"=",r)
    # print(i,"x",y,"=",i*y)

# Q Multiplication of numbers todo

z = int(input("Enter Your Digit : "))
for h in range(1,11):
    u=z*h
    print(f"{h}*{z}={u}")

#working of sum

z = int(input("Enter Your Digit : "))
sum=0
for i in range(1,z+1): 
    sum=sum+i  
print(sum)

#sum of n natural numbers

sum=0
s=""
z = int(input("Enter Your Digit : "))
for i in range(1,11): 
    sum=sum+i
    s=s+str(i)+"+"
print(s,end="")
print("=",sum)


# Q.1

# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

z = int(input("Enter Your Digit : "))
for q in range(1,z+1):
    for w in range(1,q+1):
        print(w,end=" ")
    print()

# Q.2

# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

z = int(input("Enter Your Digit : "))
for w in range(1,z+1):
    for q in range(1,w+1):
        print(w,end=" ")
    print()

# Q.3 

# 5 5 5 5 5 
# 4 4 4 4
# 3 3 3
# 2 2
# 1


z = int(input("Enter Your Digit : "))
for q in range(z,0,-1):  
    for w in range(q,0,-1): 
        print(q,end=" ")  
    print()


# for loop -ve 

# for i in range(10,0,-1):
#     print(i)



# for i in range(10):
#     print(i)

# i=0
# while i<10:
#     print(i)


# Q.4

# 5
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

n = int(input("Enter Your Digit : "))
for q in range(n, 1, -1):  
    for w in range(q, 1. -1): 
        print(w,end=" ")  
    print()



# Q.5

# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

n = int(input("Enter Your Digit : "))
for q in range(1, n + 1):  
    for w in range(n -q + 1): 
        print(q,end=" ")  
    print()

