# Q.1 Write a Python program to sum all the items in a dictionary.

ikku = {"q" : 1,"w" : 2,"e" : 3}
emmanual = sum(ikku.values())
print(f"sum all the items in a dictionary : {emmanual}")


# Q.2 Write a Python program to multiply all the items in a dictionary.


ikku = {"q" : 1,"w" : 2,"e" : 3}
S = 1  
for i in ikku.values():
    S*=i
print(f"all the items in a dictionary : {S}")

# Q.3 Write a Python program to remove a key from a dictionary.

ikku = {"q" : 1,"w" : 2,"e" : 3}
w ="w"
emmanual =ikku.pop(w)
print(f"New Dictionary :{ikku}")



