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

# def my_gen():
#     for i in range(1,6):
#         yield i

# gen = my_gen()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


# #Ex2

# names = ["ali","tom","jhon"]
# def name_gen():
#     for name in names:
#         yield name
# n = name_gen()
# for j in n:
#     print(j)

# #Ex3

# def even_gen():
#     for i in range(1,10):
#         if (i%2==0):
#             yield i
# e = even_gen()
# for j in e:
#     print(j)

# #Ex4

# def table_gen():
#     for i in range(1,11):
#         yield(f"2 x {i} = {2 * i}")
        
# tab = table_gen()
# for j in tab:
#     print(j)

# #Ex5

# string = "Hello World"
# def ch_gen():
#     for ch in string:
#         yield ch
# st = ch_gen()
# for j in st:
#     print(j)

# from functools import lru_cache
# import time

# @lru_cache(maxsize=None)

# def fun(n):
#     time.sleep(3)
#     return n*5

# a = fun(5)
# print(a)
# a = fun(6)
# print(a)
# a = fun(7)
# print(a)
# a = fun(5)
# print(a)
# a = fun(6)
# print(a)
# a = fun(7)
# print(a)
# a = fun(8)
# print(a)
                        
                        #Water Drink Reminder Window task Shedular 
# from plyer import notification
# while True:
#     time.sleep(3600)
#     notification.notify(
#         title="Reminder",
#         message= "Drink Water 'This is good for you health'"

# )
    
# from tkinter import messagebox
# while True:
#     time.sleep(5)
#     messagebox.showinfo(
#         title="Reminder",
#         message= "Drink Water"

# )
    
# import re

# pattern = r"[A-Z]+ews"
# text = '''
# News is information about current events. This may be provided through many different media: word of mouth, printing, postal systems, broadcasting, electronic communication, or through the testimony of observers and witnesses to events. News is sometimes called "hard news" to differentiate it from soft media.

# Subject matters for news reports include war, government, politics, education, health, economy, business, fashion, sport, entertainment, and the environment, as well as quirky or unusual events. Government proclamations, concerning royal ceremonies, laws, taxes, public health, and criminals, have been dubbed news since ancient times. Technological and social developments, often driven by government communication and espionage networks, have increased the speed with which news can spread, as well as influenced its content.

# Throughout history, people have transported new information through oral means. Having developed in China over centuries, newspapers became established in Europe during the early modern period. In the 20th century, radio and television became an important means of transmitting news. Whilst in the 21st century, the internet has also begun to play a similar role.
# '''

# match  = re.finditer(pattern, text)
# for matches in match:
#     print(matches)
#     print(matches.span())
#     print(text[matches.span()[0]:matches.span()[1]])


# import asyncio

# async def fun1():
#    await asyncio.sleep(2)
#    print("func 1")
#    return "Peter"
# async def fun2():
#     await asyncio.sleep(1)
#     print("func 2")
# async def fun3():
#     await asyncio.sleep(4)
#     print("func 3")

# async def main():
#     l = await asyncio.gather(
#     fun1(),
#     fun2(),
#     fun3()
# )
#     print(l)
    
# asyncio.run(main())

# from concurrent.futures import ThreadPoolExecutor
# import threading
# def func(seconds):
#     print(f"Sleeping for {seconds} seconds")
#     time.sleep(seconds)
#     return seconds

# time1 = time.perf_counter()
# # func(2)
# # func(3)
# # func(1)

# t1 = threading.Thread(target=func, args=[2])
# t2 = threading.Thread(target=func, args=[3])
# t3 = threading.Thread(target=func, args=[1])
# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()
# time2 = time.perf_counter()
# print(time2 - time1)

# def poolingDemo():
#     with ThreadPoolExecutor() as executor:
#         l = [1, 2, 6, 3, 4]
#         results = executor.map(func, l)
#         for result in results:
#             print(result)
# poolingDemo()

import multiprocessing
import requests
import concurrent.futures

def downloadFile(url, name):
    response = requests.get(url)
    print(f"Started downloading {name}")
    open(f"pics/file{name}.jpg", "wb").write(response.content)
    print(f"Finished downloading {name}")
if __name__ == '__main__':
    url = "https://picsum.photos/200/300"
    # pros = []
    # for i in range(5):
    #     # downloadFile(url, i)
    #     p = multiprocessing.Process(target=downloadFile, args=[url, i])
    #     p.start()
    #     pros.append(p)
    # for p in pros:
    #     p.join()
with concurrent.futures.ProcessPoolExecutor() as executor:
    l1 = [url for i in range(5)]
    l2 = [i for i in range(5)]
    results = executor.map(downloadFile, l1, l2 )
    for r in results:
        print(r)