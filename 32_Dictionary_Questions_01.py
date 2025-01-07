# Q.4 Write a Python program to sort a given dictionary by key.

ikku = {"q": 1, "w": 2, "e": 3}
q = sorted(ikku.items())
print(f"{q}")




# Q.5 Write a Python program to get the maximum and minimum values of a dictionary

ikku = {"q": 1, "w": 2, "e": 3}
max = max(ikku.values())
min = min(ikku.values())
print(f"The maximum value is: {max}")
print(f"The minimum value is: {min}")



# Q.6 Write a Python program to remove duplicates from the dictionary.

ikku = {"q": 1, "w": 2, "e": 3, "r": 2, "t": 1}
me = {}
w = set()
for key, value in ikku.items():
    if value not in w:
        me[key] = value
        w.add(value)
print(f"Original dictionary: {ikku}")
print(f"Dictionary after removing duplicates: {me}")



# Q.7 Write a Python program to check if a dictionary is empty or not.

ikku = {"ONE":1}
if not ikku:
    print("The dictionary is empty.")
else:
    print("The dictionary is not empty.")


# Q.8 Write a Python program to combine two dictionary by adding values for common keys.
      # d1 = {'a': 100, 'b': 200, 'c':300}
      # d2 = {'a': 300, 'b': 200, 'd':400}
      # Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})


q1 = {'a': 100, 'b': 200, 'c': 300}
w1 = {'a': 300, 'b': 200, 'd': 400}
ikku = {}
for key, value in q1.items():
    ikku[key] = value
for key, value in w1.items():
    if key in ikku:
        ikku[key] += value
    else:
        ikku[key] = value
print(ikku)



# Q.9 Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
      # Sample data : {'1':['a','b'], '2':['c','d']}
      # Expected Output:
      # ac
      # ad
      # bc
      # bd


sample_data = {'1': ['a', 'b'], '2': ['c', 'd']}
list1 = sample_data['1']
list2 = sample_data['2']
combinations = []
for first in list1:
    for second in list2:
        combinations.append(first + second)
for combination in combinations:
    print(combination)




# Q.10 10) Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'malayalam'
# Expected output: {"m':2,'a':4,'l':2,'y':1}
                  

sample_string = 'malayalam'
letter_count = {}
for I in sample_string:
    if I in letter_count:
        letter_count[I] += 1
    else:
        letter_count[I] = 1
print(letter_count)




