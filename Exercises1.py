                                #Exception Handling

#Ex1

# try:
#     num1 = int(input("Enter 1st number"))
#     num2 = int(input("Enter 2nd number"))

#     result = num1 / num2
#     print(result)
# except ZeroDivisionError:
#     print("You divided the number with zero")

#Ex2

# try:
#     filename = input("Enter file name!")
#     with open(filename, 'r') as f:
#         f.read(filename)
# except FileNotFoundError:
#     print("File is not found in directory")
    
#Ex3

# try:
#     age = int(input("Enter Your age : "))
# except ValueError:
#     print("Please enter valid number!")

#Ex4

# while True:
#     try:
#         num1 = int(input("Enter first number : "))
#         num2 = int(input("Enter Second number : "))
#         operator = input("Enter operator for operation (+, -, *, /) : ")
#         if operator == "+":
#             res = num1 + num2
#         elif operator == "-":
#             res = num1 - num2
#         elif operator == "*":
#             res = num1 * num2
#         elif operator == "/":
#             res = num1 / num2
#         else:
#             print("Invalid Operator")
#             continue
#         print(f"Result is : {res}")
#         break

#     except ValueError:
#         print("Enter Valid number")
#     except ZeroDivisionError:
#         print("Cannot divide by zero!")
#     except Exception as e:
#         print(f"Some error occurred: {e}")

#Ex5

# try:
#     file = "text.txt"
#     with open(file, 'r') as f:
#         print(f.read())
#         print("File content readed")
# except FileNotFoundError:
#     with open(file, "w") as f:
#         f.write("Hello this is new file")
#         print("File created successfully!")

#Ex1

# import random
# def generate_password(length=12):
#     if length < 8:
#         print("Minimum length should be 8. Setting length to 8.")
#         length = 8

    
#     lower = "abcdefghijklmnopqrstuvwxyz"
#     upper =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     number = "0123456789"
#     special = "!@#$%6&*?/"

#     password = [
#         random.choice(lower),
#         random.choice(upper),
#         random.choice(number),
#         random.choice(special)
#     ]
#     new_character = lower + upper + number + special
#     for _ in range(length - 4):
#         password.append(random.choice(new_character))

#     random.shuffle(password)
#     return "".join(password)

# print(generate_password(3))

#Ex2

# from datetime import datetime

# def show_current_dateTime():
#     now = datetime.now()
#     print("Current Date and Time : ", now)
#     print("Current date : ", now.strftime("%d-%m-%y"))
#     print("Current time : ", now.strftime("%H-%M-%S"))

# def age_calculator():
#     try:
#         birth_year = int(input("Enter birth year!"))
#         current_year = datetime.now().year
#         age = current_year - birth_year
#         if age < 0:
#             print("You are not born yet!")
#         elif age > 150:
#             print("Enter a valid birth year.")
#         else:
#             print(f"You are {age} years old")
#     except ValueError:
#         print("Enter a valid year (numbers only)")

# age_calculator()

#Ex3

# import os 
# cwd = os.getcwd()
# print(f"Current Directory {cwd}")

# folder_name = "myfolder"
# file_name = "notes.txt"

# os.makedirs(folder_name, exist_ok=True)
# file_path = os.path.join(folder_name,file_name)
# with open(file_path, 'w') as f:
#     f.write("Hello i'm here")

#Ex4

import json
# student_data = {
#     "student_id": "CS2025001",
#     "name": "Junaid Ahmed",
#     "age": 22,
#     "city": "Gujar Khan",
#     "course": "AI & Python",
#     "marks": {
#         "Python": 85,
#         "OOP": 78,
#         "English": 92
#     },
#     "active": True,
#     "graduation_year": 2027
# }
# print("Student Data Created\n")
# json.dump()
# def save_data(data, filename="student.json"):
#     try:
#         with open(filename, 'w') as f:
#             json.dump(data, f, indent=4)
#             print(f"Data successfully saved in {filename}")
#     except Exception as e:
#         print(e)
# save_data(student_data)

# def read_data(filename="student.json"):
#     try:
#         with open(filename, 'r') as f:
#             data = json.load(f)
#         return data
#     except FileNotFoundError:
#         print("File not found")
#     except Exception as e:
#         return None
# loaded_data = read_data()
# if loaded_data:
#     print("Data Loaded from JSON File:")
#     print(f"Name            : {loaded_data['name']}"),
#     print(f"Student ID      : {loaded_data['student_id']}"),
#     print(f"Age             : {loaded_data['age']}")
#     print(f"City            : {loaded_data['city']}")
#     print(f"Course          : {loaded_data['course']}")
#     print(f"Python Marks    : {loaded_data['marks']['Python']}")
#     print(f"Graduation Year : {loaded_data['graduation_year']}")





