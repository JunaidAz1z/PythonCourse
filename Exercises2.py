# def greet():
#     print("Hello")

# # greet()

# my_fun = greet
# my_fun()

# def func(f1):
#     f1()

# func(greet)

# def outer():
#     def inner():
#         print("Im inner method")
#     inner()
# outer()


# def decorator(func):
#     def wrapper():
#         print("Phely")
#         func()
#         print("Baad ma")
#         print("Nisha pume")
#     return wrapper

# def greet():
#     print("Hello dear")

# greet = decorator(greet)
# greet()

# def my_decorator(func):
#     def wrapper():
#         print("Hi jack")
#         func()
#         print("bye jack")
#     return wrapper

# @my_decorator
# def greet1():
#     print("Oo my yes")

# greet1()        


# def login(func):
#     def wrapper(user):
#         if user == "admin":
#             func(user)
#         else:
#             print("You need to login first")
#     return wrapper

# @login
# def dashboard(user):
#     print(f"Welcome to dashboard {user}")

# dashboard("guest")


# import time

# def timer(func):
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print(f"Time used {end - start:.2f} secnods")
#     return wrapper

# @timer
# def slow_func():
#     time.sleep(2)
#     print("Task completed!")

# slow_func()

# def info(func):
#     def wrapper(*args, **kwargs):
#         print("This is checking user details")
#         func(*args, **kwargs)
#         print("Information is okay")
#     return wrapper

# @info
# def user(name, age):
#     print(f"Hi {name} your age is {age}")

# user("Peter", 16)

#Ex1

# def shout(func):
#     def wrapper():
#         res = func()
#         print(res.upper())
#     return wrapper

# @shout
# def say():
#     return "Hello world"

# say()

#Ex2

# def repeat(func):
#     def wrapper():
#         for _ in range(3):
#             func()
#     return wrapper

# @repeat
# def say_hi():
#     print("hi")

# say_hi()  

#Ex3

# def logger(func):
#     def wrapper():
#         print(f"Function is running : {func.__name__}")
#         func()
#         print("Done")
#     return wrapper


# @logger
# def download_file():
#     print("File is downloading...")

# download_file()

#Ex4

# def validate(func):
#     def wrapper(*args, **kwargs):
#         age = args[0]
#         if age < 18:
#             print("Access denied!")
#         else:
#             func(*args, **kwargs)
#     return wrapper


# @validate
# def enter_site(age):
#     print(f"Welcome! Your age is {age}.")

# enter_site(30)  


                                                        #Async/Await

# import time
# def Tea():
#     print("Start making tea")
#     time.sleep(3)
#     print("Tea is ready")

# def chicken():
#     print("Chicken is ready")
#     time.sleep(2)
#     print("Serve to customer")

# Tea()
# chicken()

# import asyncio

# async def Tea():
#     print("Start making tea")
#     await asyncio.sleep(3)
#     print("Tea is ready")

# async def chicken():
#     print("Chicken is ready")
#     await asyncio.sleep(2)
#     print("Serve to customer")

# async def main():
#    await Tea()
#    await chicken()

# asyncio.run(main())



# import asyncio

# async def Tea():
#     print("Start making tea")
#     await asyncio.sleep(3)
#     print("Tea is ready")

# async def chicken():
#     print("Chicken is ready")
#     await asyncio.sleep(2)
#     print("Serve to customer")

# async def main():
#     await asyncio.gather(
#     Tea(),
#     chicken()
#     )
# asyncio.run(main())


# import asyncio

# async def weather_api():
#     print("Weather data is loading...")
#     await asyncio.sleep(2)
#     return "Lahore 35°C"
# async def news_api():
#     print("News data is loading...")
#     await asyncio.sleep(3)
#     return "Pakistan wins!"
# async def stock_api():
#     print("Stocks data is loading...")
#     await asyncio.sleep(1)
#     return "PSX 50000"

# async def main():
#     results = await asyncio.gather(
#         weather_api(),
#         news_api(),
#         stock_api()
#     )
#     for result in results:
#         print(result)

# asyncio.run(main())


# import asyncio

# def async_logger(func):
#     async def wraper(*args, **kwargs):
#         print(f"Function is running {func.__name__}")
#         result = await func(*args, **kwargs)
#         print("Completed!")
#         return result
#     return wraper

# @async_logger
# async def fetch_data(url):
#     await asyncio.sleep(2)
#     return f"Data from {url}"

# async def main():
#    result = await fetch_data("google.com")
#    print(result)

# asyncio.run(main())

#Ex1

# import time
# import asyncio
# async def say_hello():
#     print("Hello")
#     await asyncio.sleep(2)
#     print("Goodbye!")

# asyncio.run(say_hello())

#Ex2

# import asyncio

# async def make_pizza():
#     print("Pizza is in oven!")
#     await asyncio.sleep(3)      
#     print("Pizza is ready")

# async def make_juice():
#     print("Juice is making")
#     await asyncio.sleep(2)
#     print("Juice is ready")

# async def main():
#     await asyncio.gather(
#         make_pizza(),
#         make_juice()
#     )
# asyncio.run(main())

#Ex3

# import asyncio
# import time 
# async def get_weather():
#     print("Weather data is loading...")
#     await asyncio.sleep(2)
#     return "Karachi: 32C"
# async def get_news():
#     print("News data is loading...")
#     await asyncio.sleep(3)
#     return "Pakistan wins"
# async def gold_price():
#     print("Gold data is loading...")
#     await asyncio.sleep(1)
#     return "Gold: 490000"

# async def main():
#     start = time.time()
#     results = await asyncio.gather(
#         get_weather(),
#         get_news(),
#         gold_price()
#     )
#     for result in results:
#         print(result)
#     end = time.time()
#     print(f"Total wait {end - start} seconds")
# asyncio.run(main())

#Ex4

# import asyncio
# import time
# def timer(func):
#     async def wrapper(*args, **kwargs):
#         start = time.time()
#         print("download started!")
#         # file = args[0]
#         result = await func(*args, **kwargs)
#         end = time.time()
#         print(f"Total time {end - start:.2f} seconds")
#         return result
#     return wrapper

# @timer
# async def download(file):
#     await asyncio.sleep(2)
#     print(f"{file}downloaded")

# asyncio.run(download("csv."))

                                        #Requests

# import requests

# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# print(response.status_code)
# data = response.json()
# print(data["userId"])
# print(data["title"])



