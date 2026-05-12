
                            #Data Types and Variables
##Ex1
# name = "Hello"
# age = 2
# city = "abcd"
# print(name)
# print(age)
# print(city)

# #Ex2
# a = 14
# b = 7.5
# name = "Peter"
# result1 = a + b
# print(result1)
# result2 = a * b
# print(result2)
# print(type(name))
# print(type(a))

# #Ex3
# name = input("What is your name : ")
# age = int(input("What is your age : "))
# color = input("What is your Favourite color : ")

# print(f"Hello {name}! Apki age {age} hai Apka favorite color {color} hai Aap agle saal {age+1} saal ke ho jayenge.")




                                    #Strings

#Ex1

# name = "Kim Peter"
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(len(name))
# print(name.replace("Peter", "Ahmed"))

#Ex2

# name = input("What is your name : ")
# city = input("What is your city : ")
# food = input("What is your fav food : ")
# print(f"Hello {name} app {city} sy hain aur apka favorite food {food} hai.")

#Ex3

# string = "Programing"
# print(string[:3])
# print(string[3:6])
# print(string[6:10])
# print(string[::-1])

#Ex4

# sentence = input("Enter a sentence :")
# word =sentence.split()
# print(len(word))
# print(sentence.upper())
# print(sentence.count("python"))


#If-Else

#Ex1

# age = int(input("What is your age : "))
# if (age > 0 and age < 13):
#     print("Child")
# elif (age >= 13 and age <= 19):
#     print("Teenager")
# elif (age >= 20 and age <= 35):
#     print("Young Adult")
# elif (age >= 36 and age <= 50):
#     print("Adult")
# else:
#     print("Senior Citizen")

# #Ex2

import random

# comp = random.randint(1,1000)
# count = 1
# while True:
#     user = int(input("Guess the correct number"))
#     if (user == comp):
#         print("Congratulations! You gessed correct number")
#         break
#     elif (user < comp):
#         print("Guess big number")
#     else:
#         print("Guess small number")
#     count = count + 1

# print(f"You guessed Number in {count} Times")

#Ex3

# num1 = int(input("Enter first Number!"))
# num2 = int(input("Enter second Number!"))
# opr = input("Enter operator /,*,+,-")

# if (opr == "+"):
#     print(num1 + num2)
# elif (opr == "-"):
#     print(num1 - num2)
# elif (opr == "*"):
#     print(num1 * num2)
# elif (opr == "/"):
#     if (num1 > 0 and num2 == 0):
#         print(num1 / num2)
#         print("Division by zero not Allowed")
# else:
#     print("Wrong Input")

#Ex4 
#Age < 5 → Free
# Age 5-12 → 300 Rs
# Age 13-18 → 500 Rs
# Age 19-60 → 800 Rs
# Age > 60 → 400 Rs (Senior Discount)

# Extra: Agar user "Student" hai to 20% discount do.

# age = int(input("Enter your age : "))

# if (age < 5):
#     price = 0
#     print("Free entry")
# elif (age >= 5 and age <= 12):
#     price = 300
#     print("300 ticket")
# elif (age >= 5 and age <= 12):
#     price = 500
#     print("500 ticket")
# elif (age >= 13 and age <= 18):
#     price = 800
#     print("800 ticket")
# else:
#     price = 400
#     print("400 ticket")

# s = input("Are you student :").lower()

# if (s == "yes" or s == "y"):
#     discount = price * 0.20
#     final_price = price - discount
#     print(f"Student Discount Applied! 20% off : {final_price}")
# else:
#     final_price = price
#     print(f"Your ticket price is {final_price}")

#Ex5

# password = input("Enter Password ")
# has_number = False
# has_letter = False
# has_special = False

# for character in password:
#     if character.isalpha():
#         has_letter = True
#     elif character.isdigit():
#         has_number = True
#     else:
#         has_special = True
# if (len(password) < 8):
#     print("Weak password")
# elif(has_letter and has_number):
#     print("Medium Password")
# elif(has_letter and has_number and has_special):
#     print("Strong Password")
# else:
#     print("Weak Password")

#Loops

#Ex1

# for i in range(1,51):
#     print(i)
# for i in range(1,21):
#     if(i%2==0):
#         print(i)
# for i in range(1,11):
#     print(f"5 X {i} = {5 * i}")

#Ex2

# total = 0
# number = int(input("Enter a number : "))
# for i in range(1, number+1):
#     total = total + i
# print(total)

#Ex3

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()

#Ex4

# total = 0
# count = 0
# while True:
#     number = int(input("Enter a number : "))
#     if (number == -1):
#         break
#     total = total + number
#     count = count + 1
 
# avg = (total/count)
# print(avg)

#Functions

#Ex1

# def welcome():
#     print("Welcome to python learning!")
# welcome()

#Ex2

# def add():
#     a = int(input("Enter 1st number :"))
#     b = int(input("Enter 2nd number :"))
#     c = a + b
#     return c
# print(add())

#Ex3

# def even_odd(number):
   
#     if (number%2==0):
#         print("number is even")
#     else:
#         print("number is odd")

# even_odd(5)

#Ex4

# def grade(marks):
#     if marks == 90:
#         return "A+"
#     elif marks == 80:
#         return "B"
#     elif marks == 70:
#         return "C"
#     else:
#         return "D"

# print(grade(80))

#Ex5

# opr = input("Enter the operator : ")
# def calculator(n1, n2):
#     if opr == "+":
#         return n1 + n2
#     elif opr == "-":
#         return n1 - n2
#     elif opr == "*":
#         return n1 * n2
#     elif opr == "/":
#         return n1 / n2
#     else:
#         return "Invalid input"
# print(calculator(3,5))

#Ex6

# def temp_converter(temp, unit):
#     if unit == 'c' or unit =="C":
#         f = (temp * 1.8) + 32
#         return f
#     elif unit == 'f' or unit == 'F':
#         c = (9/5) * (temp - 32)
#         return c
# print(temp_converter(45, "f"))

#Ex7

# def student_result(name, marks=[]):
#     s_total= 0
#     m_total =500
#     per = 0
#     for mark in marks:
#         s_total = s_total + mark 
#     print(f"{name} and marks are {s_total}")
#     print(f"Total marks are : {m_total}")
    
#     per = (s_total/m_total) * 100
#     print(per)
#     if per >= 80:
#         print("A Grade")
#     elif per >= 70 and per <80:
#         print("B Grade")
#     elif per >=60 and per < 70:
#         print("C Grade")
#     else:
#         print('Fail')
# student_result("tom",[60,56,98,78,89])

#Ex8

# def gen_password(length=12):
#     if length < 8 :
#         print("Warning! Your password is weak.")
#     length = 8

#     lowercase = "abcdefghijklmnopqrstuvwxyz"
#     uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     numbers = "0123456789"
#     special = "!@#$%^&*()_+-=[]{}|;:,.<>/?"

#     all_character = lowercase + uppercase + numbers + special
#     password = [
#         random.choice(lowercase),
#         random.choice(uppercase),
#         random.choice(numbers),
#         random.choice(special)
#     ]
#     for _ in range(length - 4):
#         random.choice(password.append(all_character))

#     random.shuffle(password),
#     final_password = "".join(password)
#     return final_password

# if __name__ == "__main__":
#     print("Generated Password:", gen_password(12))
#     print("Generated Password:", gen_password(16))


#Ex1

# foods = ["chicken", "pizza", "burger", "kheer", "chicken pulao", "beef", "biryani", "bbq"]
# foods.insert(1, "tiqqa kabab")
# foods.append("nehari")
# foods.remove("chicken")
# foods.sort()
# print(foods)

#Ex2

# students = []
# for std in range(5):
#     name = input("Enter new student in list : ")
#     students.append(name)
# for st in students:
#     print(f"Name is {st} and letters in name {len(st)}")

#Ex3

# Ek dictionary banao jisme 4 students ka data ho (name, age, marks).
# Phir saare students ka naam aur percentage print karo.

# students = {
#     "std101": {
#         "name": "Ali Khan",
#         "age": 20,
#         "marks": 85
#     },
#     "std102": {
#         "name": "Sara Ahmed",
#         "age": 19,
#         "marks": 92
#     },
#     "std103": {
#         "name": "Usman Tariq",
#         "age": 21,
#         "marks": 78
#     },
#     "std104": {
#         "name": "Fatima Noor",
#         "age": 20,
#         "marks": 88
#     }
# }

# for j, i in students.items():
#     name = i["name"]
#     mark = i["marks"]
#     percentage = (mark/100) * 100
#     print(name)
#     print(percentage)

#Ex4

# cart = []
# total_bill = 0

# for i in range(4):
#     product_name = input("Enter name of product : ")
#     price = int(input("Enter price of product : "))
#     product = {
#     "name": product_name,
#     "price": price,
# }
#     cart.append(product)
# for bill in cart:
#     print(f"Product name: {bill["name"]} - Price: {bill["price"]}")
#     items = len(cart)
#     price = bill["price"]
#     total_bill = total_bill + price
# print(f"Total items : {items}")
# print(f"Total bill : {total_bill}")

#Ex5

# Ek list banao [23, 45, 12, 67, 34, 89, 10]
# Phir is list se:
# Sabse chhota number
# Sabse bara number
# Total sum
# Even numbers ki list
# print karo.

# numbers = [34, 45, 65, 34, 23, 42, 435]
# sa = 0
# even = []
# print(numbers.pop(4))
# print(numbers.pop(-1))
# for s in numbers:
#     sa = sa + s
#     if s%2==0:
#         even.append(s)

# print(sa)
# print(even)
# print(numbers)


#Ex1 

# with open("myinfo.txt", "w") as f:
#     f.write("Peter, 23, Rwp, CS")

#Ex2

# with open("myinfo.txt", "r") as f:
#     print(f.read())

#Ex3

# products = []
# for i in range(4):
#     name = input("Enter name of product: ")
#     price = int(input("Enter price of product: "))
#     product = {
#         "name": name,
#         "price": price
#     }
    
#     products.append(product)

# with open("bill.txt", 'w') as f:
#     f.write("=== Shopping Bill ===\n\n")
    
#     total = 0
#     for p in products:
#         f.write(f"Product: {p['name']} - Price: {p['price']} Rs\n")
#         total += p['price']
    
#     f.write("\n" + "-"*30 + "\n")
#     f.write(f"Total Bill = {total} Rs")

#Ex4

# students = []
# for i in range(3):
#     name = input("Enter name of student : ")
#     marks = int(input("Enter marks of student : "))
#     details = {
#           "name": name,
#           "marks": marks
#     }
#     students.append(details)
# print(students)
# with open("student.txt", "w") as f:
#       f.write(" === Students Details === \n\n")
#       for s in students:  
#             f.write(f"{s['name']} - {s['marks']}\n")
        
#Ex5

# with open("student.txt", "r") as f:
#     content = f.read()

#     lines = content.splitlines()
#     lines_count = len(lines)
#     print(lines_count)

#     word = content.split()
#     word_count = len(word)
#     print(word_count)

#     longest_line = max(lines, key=len)
#     longest_len = len(longest_line)
#     print(longest_len)

                                                    #OOP

# Ek class Person banao jisme name aur age ho.
# Method banao introduce() jo naam aur age print kare.

#Ex1

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         print(f"Name is {self.name} and age is {self.age}")

# obj = Person("Tom",23)
# obj.introduce()

#Ex2

# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self, amount):
#         self.amount = amount
#         amount= int(input("Enter amount you want to deposit :"))
#         self.balance = self.balance + amount
#         print(f"Rs {amount} deposited successfully!")


#     def withdraw(self, amount):
#         self.amount = amount
#         amount = int(input("Enter amount you want to withdraw :"))
#         if amount > self.amount:
#             print("Insufficent Balance!")
#         else:
#             self.balance = self.balance - amount
#             print(f"Rs {amount} withdrawn successfully!")
    
#     def check_balance(self):
#         print(self.account_holder)
#         print(self.balance)

# obj = BankAccount("ali",10000)
# obj.check_balance() 
# obj.deposit(5000)   
# obj.check_balance() 
# obj.withdraw(2000)
# obj.check_balance()

#Ex3

# Class Student
# Attributes: name, roll_no, marks (list)
# Methods:
# add_marks()
# get_average()
# get_grade()    

# class Student:
#     def __init__(self, name, roll_no):
#         self.name = name
#         self.roll_no = roll_no
#         self.marks = []
    
#     def add_marks(self, subject_marks):
#         self.marks.append(subject_marks)
#         print(f"{subject_marks} marks added | Current Marks: {self.marks}")
    
#     def get_average(self):
#         if len(self.marks) == 0:
#             return 0
#         total = sum(self.marks)
#         avg = total / len(self.marks)
#         return avg

#     def get_grade(self):
#         avg = self.get_average()          
        
#         if avg >= 90:
#             return "A+"
#         elif avg >= 80:
#             return "A"
#         elif avg >= 70:
#             return "B"
#         elif avg >= 60:
#             return "C"
#         else:
#             return "Fail"

    
#     def show_result(self):
#         avg = self.get_average()
#         grade = self.get_grade()
#         print("="*40)
#         print(f"Student Name : {self.name}")
#         print(f"Roll No      : {self.roll_no}")
#         print(f"Marks        : {self.marks}")
#         print(f"Average      : {avg:.2f}")
#         print(f"Grade        : {grade}")
#         print("="*40)



# obj = Student("Tom", 899)

# obj.add_marks(85)
# obj.add_marks(78)
# obj.add_marks(92)
# obj.add_marks(65)

# obj.show_result()

#Ex4

# Ek class Vehicle banao (brand, model)
# Usse inherit karke Car aur Bike class banao with extra features.

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, price):
        self.price = price
        super().__init__(brand, model)
    def Car_Details(self):
        print(f"{self.brand} and model is {self.model} and price is {self.price}")
class Bike(Vehicle):
    def __init__(self, brand, model, price, color):
        self.price = price
        self.color = color
        super().__init__(brand, model)
    def Bike_Details(self):
        print(f"{self.brand} and model is {self.model} and price is {self.price} and the color is {self.color}")
obj1 = Car("BMW","A600",34000000)
obj1.Car_Details()
ob = Bike("Honda", "CG125", "350000", "Black")
ob.Bike_Details()



# Exercise 5: Library Management System (Mini Project)

# Class Book
# Class Library
# Methods: add book, issue book, return book, show available books


