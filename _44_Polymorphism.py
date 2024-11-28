# Polymorphism

# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes

print(44+56)
print("abc" + "abc")
print([123]+[123])
print(12.2 + 12.5)



print(len("abcd"))
print(len(["abcd","abcd"]))



# Overriding Possbile

class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")

class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")
obj_ind = India()
obj_usa = USA()




# for country in (obj_ind, obj_usa):
#     country.capital()
#     country.language()
#     country.type()





# Overloading not Possbile
    
class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def language(self):
        print("malayalam is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")

obj =India()
obj.language()

