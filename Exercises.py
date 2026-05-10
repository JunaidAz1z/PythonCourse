
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

