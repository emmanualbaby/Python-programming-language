# vowels


z = ["Hello", "Ikku"," python","victus"]
vowels =["a","e","i","o","u","I"]
ol=[]
for i in z:
    s=''
    for j in vowels:
        if j in i:
            s=s+j
    ol.append(s)
print(ol)


# vowels count

z = ["Heellooooo", "Ikkuuuuuu"," python","victus"]
vowels =["a","e","i","o","u","I"]
vowels1 = []
for i in z:
    count = 0
    for ikku in i:
        if ikku in vowels:
            count+=1
    vowels1.append(count)
print(vowels1)




