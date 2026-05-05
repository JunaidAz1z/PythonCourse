# class Person:
#     name = "Peter"
#     occupation = "Software Dev"
#     age = 34

#     def info(self):
#         print(f"{self.name} is a {self.occupation}")

# obj = Person()
# obj1 = Person()
# obj2 = Person()
# obj.name = "Tom"
# obj.occupation = "Web Dev"
# obj.info()

# obj1.name = "Roman"
# obj1.age = 24
# obj1.info()

# obj2.name = "Jhon"
# obj2.age = 21
# obj2.info()

class Person:
    def __init__(self, name, occ):
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is a {self.occ}")

ob = Person("Tom", "HR")
ob1 = Person("Junaid", "Python Developer")
# ob.name = "Ali"
# ob.occ = "Developer"
# ob1.name = "Ali"
# ob1.occ = "Developer"
ob.info()
ob1.info()

def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("Hello world!")

hello()