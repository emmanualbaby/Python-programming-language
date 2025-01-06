# Python Dictionaries

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)




list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = ["emmanual", "ikku", "anu", "ann", "wawa", "don", "me", "you", "vava"]
dictionary = {}
for i in range(len(list1)):
    dictionary[list1[i]] = list2[i]
print(dictionary)

# Q.1

s = "hteruerhbdyiggd45764₹_73##+8)_-))"
ikku = {
    'alphabets': 0,
    'numericals': 0,
    'specialcharacters': 0
}
for i in s:
    if i.isalpha():
        ikku['alphabets'] += 1
    elif i.isdigit():
        ikku['numericals'] += 1
    else:
        ikku['specialcharacters'] += 1
print(f"{ikku}")


#Q.2

ikku = int(input("enter the number of elements: "))

