                        #Class Methods as Alternative Constructors


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromString(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))
obj = Employee("Peter", 12000)
print(obj.name)
print(obj.salary)

string = "Hulk-12300"
print(string)
obj1 = Employee.fromString(string)
print(obj1.name)
print(obj1.salary)


                                        #dir, __dict__ and help method in Python

# x = [1,2,3]
# print(dir(x))
# print(x.__le__)

# x = (1,2,3)
# print(dir(x))
# print(x.__mul__)


# class Person:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
# obj = Person('Tom', 23, "male")
# print(obj.__dict__)


# print(help(Person))


                                            #Super keyword in Python

class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Child(Parent):
    def __init__(self, name, age, lang):
        super().__init__(name, age)
        self.language = lang

obj = Parent("Peter", 22)
print(obj.name)
print(obj.age)

obj1 = Child("Kim", 34, "Python")
print(obj1.name)
print(obj1.age)
print(obj1.language)
        
                                        #Magic/Dunder Methods in Python


#Call method aik object ko function ki tara behave karwata
class Student:

    def __call__(self):
        print("Object called!")

obj = Student()

obj()

#Str method k without object ko direct print krny par memory location print hoti-
#jab k agar str method use kar k object ko print karen tu data display ho jata 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
ob = Person("Ali", 22)
print(ob)


#pehle __str__ dhoondta hai
#agar na mile to __repr__ use karta hai


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):

        return f"Person('{self.name}', {self.age})"


p1 = Person("Ali", 22)

print(p1)


class Books:

    def __init__(self):
        self.items = ["Math", "Physics", "English"]

    def __len__(self):
        return len(self.items)


b = Books()

print(len(b))


#Method Overriding

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def area(self):
        return self.x * self.y
    
class Circle(Shape):
    def __init__(self, radious):
        self.radious = radious
        super().__init__(radious, radious)
    def area(self):
        return 3.14 * super().area()
    
# o = Shape(3,4)
# print(o.area())
        
ob = Circle(5)
print(ob.area())


                                #Exercise Solution

import os
from pypdf import PdfWriter


merger = PdfWriter()

files = os.listdir("Pdf_files")

for pdf in files:
    merger.append(os.path.join("Pdf_files", pdf))

merger.write("New1.pdf")

#Operator Overloading

#+ only numbers ke liye
#+ vectors, strings, objects sab ke liye custom ban jata hai
class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self, x):
        return Vector(self.i + x.i, self.j + x.j, self.k + x.k)
ob1 = Vector(3, 4, 5)
print(ob1)

ob2 = Vector(5, 2, 1)
print(ob2)

print(ob1 + ob2)


