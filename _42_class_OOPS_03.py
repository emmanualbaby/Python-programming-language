# Q.1

class car():
    def __init__(self):
        self.year =2018
        self.type = "auto"
        self.engine = "pet"

    def details(self,a,b,c):
        print("model",a)
        print("brand",b)
        print("year",c)

    # def display(self):
    #     print(self.year)


obj = car()
obj.details("eco","ford",2018)




# Q.2

class car():
    def __init__(self,a,b,c):
        self.year = a
        self.type = b
        self.engine = c

    def display(self):
        print(f"{self.year},{self.type},{self.engine}")



w =car(2018,"auto","petrol")
w.display()

r = car(2044,"auto","petrol")
r.display()




    