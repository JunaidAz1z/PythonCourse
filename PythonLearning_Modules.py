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

# a = True
# print(a:=False)

# number = [1, 2, 3, 4, 5]
# while (n := len(number)) > 0:
#     print(f"{n} Elements in list")
#     print(number.pop())


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



#8cb8e0c2ddc5442282db0cae2537962f API KEY

# import requests
# import json
# api_key = "8cb8e0c2ddc5442282db0cae2537962f"
# query = input("Which News you want to see!")
# response = requests.get(f"https://newsapi.org/v2/top-headlines?q={query}&apiKey={api_key}")

# data = response.json()
# for article in data["articles"]:
#     print(article["title"])
#     print(article["description"])

# def my_generator():
#     for i in range(50000):
#         yield i

# gen = my_generator()
# print(next(gen))
# print(next(gen))

# for j in gen:
#     print(j)

                                #Generator Exercises

#Ex1

def my_gen():
    for i in range(1,6):
        yield i

gen = my_gen()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


#Ex2

names = ["ali","tom","jhon"]
def name_gen():
    for name in names:
        yield name
n = name_gen()
for j in n:
    print(j)

#Ex3

def even_gen():
    for i in range(1,10):
        if (i%2==0):
            yield i
e = even_gen()
for j in e:
    print(j)

#Ex4

def table_gen():
    for i in range(1,11):
        yield(f"2 x {i} = {2 * i}")
        
tab = table_gen()
for j in tab:
    print(j)

#Ex5

string = "Hello World"
def ch_gen():
    for ch in string:
        yield ch
st = ch_gen()
for j in st:
    print(j)

from functools import lru_cache
import time

@lru_cache(maxsize=None)

def fun(n):
    time.sleep(3)
    return n*5

a = fun(5)
print(a)
a = fun(6)
print(a)
a = fun(7)
print(a)
a = fun(5)
print(a)
a = fun(6)
print(a)
a = fun(7)
print(a)
a = fun(8)
print(a)




