# # Conditional Statements - if,elif,else

x = 10
if x<10:
    print(f"{x} is less than 10 ")
elif x==10:
    print(f"Both are {x}")
else:
    print(f"{x} is not less than 10")



x = int(input("Enter Your Digit : "))
if x==10:
    print(f"Both are same")
elif x<10:
    print(f"{x} is less than 10 ")
else:
    print(f"{x} is greater than 10")





# # Q. Check whether the digit is even or not
num = int(input("Enter your digit : "))
if num%2==0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")




# # Q. Print all even numbers upto 10

for i in range(1,11):
    if i%2==0:
        print(i,end=" ")



# # Q.Print all odd numbers upto 10

for q in range(1,11):
    if q%2==1:
        print(q,end=" ")



# # Q. Check whether the digit is a divisble of 3

b = int(input("Enter your digit : "))
if b%3==0:
    print(f"{b} is a diviable of 3")
else:
    print(f"{b} is a not diviable of 3")





# # Q.Check whether the digit is a divisble of 5
    
c = int(input("Enter your digit : "))
if c%5==0:
        print(f"{c} is a diviable of 5")
else:
    print(f"{c} is a not diviable of 5")
    
    
# # Check whether the digit is a divisble of both 3 and 5
    

y = int(input("Enter Your Digit : "))
if y%3==0 and y%5==0:
    print(f"{y} divisble of both 3 and 5")
else:
    print(f"{y} not divisble of both 3 and 5")

      
# # check whether the digit is a divisible of either 3 or 5
    

y = int(input("Enter Your Digit : "))
if y%3==0 and y%5==0:
     print(f"{y} both are same" )
elif y%3==0:
     print(f"{y} is a diviable of 3")
else:
     print(f"{y} is a diviable of 5")





     
     