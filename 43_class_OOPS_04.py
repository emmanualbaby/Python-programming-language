# Q.1 

class car():
    def read(self ,y ,b ,m):
        self.year = y
        self.brand = b 
        self.model = m

    def display(self):
        print(f"{self.year},{self.brand},{self.model}")

obj = car()
brand = input("enter the brand name : ")
model = input("enter the model : ")
year = int(input("enter the year :"))

obj.read(m=model,b=brand,y=year)
obj.display()


# Q.2

class car():
    def __init__(self ,a, b):
        self.me = a
        self.mee =b




    def read(self):
        self.year = int(input("enter the year :"))
        self.brand = input("enter the brand name : ")
        self.model = input("enter the model : ")

    def display(self):
        print(f"{self.brand},{self.brand},{self.year}")
        print(f"{self.me},{self.mee}")


obj =car("ikku","ikkuu")
obj.read()
obj.display()


print(f"{obj},Obj view")