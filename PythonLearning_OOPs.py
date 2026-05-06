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

class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")
    
    @property
    def ten_value(self):
       return 10 * self._value
    
    @ten_value.setter
    def ten_value(self, new_val):
       self._value = new_val/5
       
    
obj = MyClass(5)
obj.ten_value = 100
obj.show()
print(obj.ten_value)

class Car:
    def __init__(self, mod):
        self.model = mod
    
    def show(self):
        print(f"Model of car is {self.model}")

    @property
    def car_model(self):
        return 5 + self.model
    
    @car_model.setter
    def car_model(self, new_model):
        self.model = new_model-2

obj1 = Car(2005)
obj1.car_model = 2008
print(obj1.car_model)
obj1.show()


class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def showDetails(self):
        print(f"{self.id} is the id of {self.name}")



class Programmer(Employee):
    def language(self):
        print(f"Default language is Python")

class Manager(Employee):
    def department(self, dep):
        self.dept = dep
        print(f"He is a manager in {self.dept} Department")

class Salary(Programmer):
    def section(self, fd, bd):
        self.front = fd
        self.back = bd
        print(f"salary of front end developer is {self.front}")
        print(f"salary of Back end developer is {self.back}")



ob = Employee(101, 'Peter')
ob.showDetails()
ob1 = Programmer(102, 'Sani')
ob1.showDetails()
ob1.language()
ob3 = Manager(103, "Tom")
ob3.department("IT")
ob2 = Salary(104, "Junaid")
print(f"The employee id is {ob2.id} and name is {ob2.name} and other details shown below")
ob2.section(100000, 150000)


class Student:
    def __init__(self):
        self.__name = "Kim"

ob = Student()
print(ob._Student__name)

class Teacher:
    def __init__(self):
        self._name = "Harry"

ob1 = Teacher()
print(ob1._name)

class Library:
    def __init__(self, no_books=0, books=[]):
        self.no_books = no_books
        self.books = books

    def addBook(self,book):
        self.no_books += 1
        self.books.append(book)
        print(self.books)
        print(f"No of Books {self.no_books}")
        
    def check(self):
        if(len(self.books) == self.no_books):
            print("Length is same!")
        else:
            print("Something wrong with programm")
ob = Library()
ob.addBook("Math")
ob.addBook("Computer")
ob.check()



# class Students:
#     def __init__(self, count=0, std=[]):
#         self.co = count
#         self.st = std
        
#     def addStudent(self,sname):
#         self.co += 1
#         self.st.append(sname)
#         print(self.st)

# oo = Students()
# oo.addStudent("Jhon")















    