class Person():
    name = "Peter"
    occupation = "Software Dev"
    age = 34

    def info(self):
        print(f"{self.name} is a {self.occupation}")

obj = Person()
obj1 = Person()
obj2 = Person()
obj.name = "Tom"
obj.occupation = "Web Dev"
obj.info()

obj1.name = "Roman"
obj1.age = 24
obj1.info()

obj2.name = "Jhon"
obj2.age = 21
obj2.info()