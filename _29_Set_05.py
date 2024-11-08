
# ikku = {"teilpanoramas", "kleintierdressur", "dateinamens", "vorsteherdrüse", "herunterschreibst", 
#         "tempobegrenzung", "schnittkäsebetrieb", "ingenieuranalyse", "postsynapse", "anlagenarten", 
#         "muskelfan", "funktionsmustern", "stoffgeruch", "wertverfalles", "außendienstlerin", 
#         "laufbahnrechtlichem", "postniederlassungen", "entwicklungshöhepunkten", "dazwischenplärrst", 
#         "kleinprofilnetzen", "konservieren", "blattform", "erkältungskrankheiten", "alkoholpegel", 
#         "übergeschlagen", "übertragungseinrichtung", "panegyrischem"}

# vg = int(input("enter your number: "))
# me = []
# for i in range(vg):
#     l = input("Enter a letter: ")
#     me.append(l)   
# print(f"List of entered letters: {me}")
# vava = []
# for word in ikku:
#     if any(letter in word for letter in me):
#         vava.append(word)
# print("Words containing any of the entered letters:")
# for word in vava:
#     print(word)



# ikku = {"teilpanoramas", "kleintierdressur", "dateinamens", "vorsteherdrüse", "herunterschreibst", 
#         "tempobegrenzung", "schnittkäsebetrieb", "ingenieuranalyse", "postsynapse", "anlagenarten", 
#         "muskelfan", "funktionsmustern", "stoffgeruch", "wertverfalles", "außendienstlerin", 
#         "laufbahnrechtlichem", "postniederlassungen", "entwicklungshöhepunkten", "dazwischenplärrst", 
#         "kleinprofilnetzen", "konservieren", "blattform", "erkältungskrankheiten", "alkoholpegel", 
#         "übergeschlagen", "übertragungseinrichtung", "panegyrischem"}

# vg = int(input("Enter the number of letters: "))
# me = []
# for i in range(vg):
#     l = input("Enter a letter: ")
#     me.append(l)   
# print(f"List of entered letters: {me}")
# s = ''
# for word in ikku:
#     for q in me:
#         if q in word:
#             s += q
# print(f"Letters found in the words: {s}")





ikku = {"teilpanoramas", "kleintierdressur", "dateinamens", "vorsteherdrüse", "herunterschreibst", 
        "tempobegrenzung", "schnittkäsebetrieb", "ingenieuranalyse", "postsynapse", "anlagenarten", 
        "muskelfan", "funktionsmustern", "stoffgeruch", "wertverfalles", "außendienstlerin", 
        "laufbahnrechtlichem", "postniederlassungen", "entwicklungshöhepunkten", "dazwischenplärrst", 
        "kleinprofilnetzen", "konservieren", "blattform", "erkältungskrankheiten", "alkoholpegel", 
        "übergeschlagen", "übertragungseinrichtung", "panegyrischem"}

vg = int(input("Enter the number of letters: "))
me = []
for i in range(vg):
    l = input("Enter a letter: ")
    me.append(l)   
print(f"List of entered letters: {me}")
qw=[]
for d in ikku:
    b=1
    for h in me:
        if h not in d:
            b=0
            break
    if b==1:
        qw.append(d)
print(f"{qw}")




