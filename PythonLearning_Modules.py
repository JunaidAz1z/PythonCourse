import time

# def whileLoop():
#     i =0
#     while i<5000:
#         print(i)
#         i = i +1

# def forLoop():
#     for i in range(5000):
#         print(i)
#         i = i +1

# t = time.time() 
# whileLoop()
# ct = time.time() - t
# t = time.time() 
# forLoop()
# print(time.time() - t)
# print(ct)


# print("Hello")
# time.sleep(3)
# print("Program finished after 3 seconds!")

# t = time.localtime()
# formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
# print(formatted_time)

a = True
print(a:=False)

number = [1, 2, 3, 4, 5]
while (n := len(number)) > 0:
    print(f"{n} Elements in list")
    print(number.pop())


# food = list()
# while True:
#     f = input("Which food do  you like : ")
#     if f == "quit":
#         break
#     food.append(f)

#     print(food)

# food = list()
# while (f := input("Which food do you like : ")) != "quit":
#     food.append(f)


import shutil
import os
# shutil.copy("peter.py", "D:/")
# shutil.copytree("pics", "pictures")
# shutil.move("pictures/1.jpg", "1.jpg")
# shutil.rmtree("pictures")
# os.rmdir("pictures")

# import requests

# response = requests.get("https://www.google.com")
# html = response.text
# print(html)

# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify())
# for head in soup.find_all("h3"):
#     print(head.text)


# url = 'https://jsonplaceholder.typicode.com/posts'

# data = {
#     "title": 'foo',
#     "body": 'bar',
#     "userId": 3,
 
# }
# headers = {
#     'Content-type': 'application/json; charset=UTF-8'
#   }

# response = requests.post(url, headers=headers, json=data)
# print(response.json())
