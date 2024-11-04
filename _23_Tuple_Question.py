# Q.1 write a python program to convert a tuple to a string.

names = ("emmanual", "ikku", "emmanu", "manu", "wawa",)
vava = ", ".join(names)
print(f"convert a tuple to a string{vava}")

# Q.2 write a python program to find repeated items in a tuple.

names = ("emmanual", "ikku", "emmanu", "manu", "wawa", "emmanual","wawa",)
x = []
for i in names:
    if names.count(i)>1:
        if i not in x:
            x.append(i)
print(f"repeated {x}")

# write a python program to check whether an element exists within a tuple.

names = ("emmanual", "ikku", "emmanu", "manu", "wawa", "emmanual")
wawa = (input("Enter Your element : "))
if wawa in names:
    print(f"yes",{wawa})
else:
    print(f"No",{wawa})



