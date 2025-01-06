# # Q.1 Write a Python program to create a set

a = {2, 3, 4, 5, 6, 7, 8, 9}
ikku = set(a)
print(type(ikku))


# # Q.2 Write a Python program to add member(s) to a set.


ikku = {1, 2, 3}
ikku.add(4)
print(f"{ikku}")


# # Q.3 Write a Python program to find common elements from two sets

me = {"a", "b", "c"}
u = {"g", "m", "a"}
me.intersection_update(u)
print(f"{me}")

# # Q.4 Write a Python program to compain two sets.

ikku1 = {"a", "b", "c"}
ikku2 = {1, 2, 3}
ikku3 = ikku1.union(ikku2)
print(f"{ikku3}")


# # Q.5 Write a Python program to create set difference.

ikku1 = {1,2,3,4,5,6,7,8}
ikku2 = {1, 2, 3,8,9,0}
ikku3 = ikku1.difference(ikku2)
print(f"{ikku3}")


# # Q.6 Write a Python program to create a symmetric difference

ikku1 = {1,2,3,4,5,6,7,8}
ikku2 = {1, 2, 3,8,9,0}
ikku3 = ikku1.symmetric_difference(ikku2)
print(f"{ikku3}")


# # Q.7 Write a Python program to check if a set is a subset of another set.

ikku1 = {1,2,3,4,5,6,7,8}
ikku2 = {1, 2, 3,8,9,0}
ikku3 = ikku1.issubset(ikku2)
print(f"{ikku3}")


# # Q.8 Write a Python program to remove all elements from a given set.

a = {2, 3, 4, 5, 6, 7, 8, 9}
a.clear()
print(a)


# # Q.9 Write a Python program to find the maximum and minimum values in a set.

ikku1 = {1,2,3,4,5,6,7,8}
ikku2 = max(ikku1)
ikku3 = min(ikku1)
print(f"the maximum values in a set:{ikku2}")
print(f"the minimum values in a set:{ikku3}")



# # Q.10  Write a Python program to check if a given value is present in a set or not

ikku1 = {1,2,3,4,5,6,7,8}
ikku = int(input("Enter Your Digit : "))
me = ikku in ikku1
if me:
    print(f"the vaule is present in the set {ikku} ")
else:
    print(f"the vaule not present in the set {ikku}")


# # Q.11 Write a Python program to check if two given sets have no elements in common

ikku = {1,2,3,4}
ikku1 = {5,6,7,8}
if ikku.isdisjoint(ikku1):
    print(f"the set have no elements in common:")
else:
    print("the sets have some elements in common:")




# # Q.12 Write a Python program to find elements in a given set that are not in another set

ikku = {1,2,3,4}
ikku1 = {5,6,3,7,8}
ikku3 = ikku - ikku1
print(f"{ikku3}")



# # Q.13 

ikku = {"teilpanoramas","kleintierdressur","dateinamens","vorsteherdrüse","herunterschreibst","tempobegrenzung""schnittkäsebetrieb","ingenieuranalyse","postsynapse","anlagenarten","muskelfan","funktionsmustern","stoffgeruch","wertverfalles","außendienstlerin","laufbahnrechtlichem","postniederlassungen","entwicklungshöhepunkten","dazwischenplärrst","kleinprofilnetzen","konservieren","blattform","erkältungskrankheiten","alkoholpegel","übergeschlagen","übertragungseinrichtung","panegyrischem"}
vg =int(input("enter your number"))
me =[]
for i in range(vg):
    l=input("enter a letter")
    me.append(l)
print(f"{me}")
s = ''
for w in me:
    if w in ikku:
        s+=w
print(f"{s}")
