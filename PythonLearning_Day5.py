# import peter

# peter.welcome()

import os 
# if (not os.path.exists):
#     os.mkdir("data")
# for i in range(0,100):
#     os.rename(f"data/Day {i+1}", f"data/Tutorial {i+1}")
    # os.mkdir(f"data/Day {i+1}")
# folder = os.listdir("data")

# for folders in folder:
#     print(folders)
# print(os.getcwd())

# x = 2
# def fun():
#     y = 5
#     global x
#     x = 7
#     print(y)
    
# fun()
# print(x)

# f = open('textfile.txt', 'r')
# text = f.read()
# print(text)
# f.close()

# f = open('textfile1.txt', 'a')
# text = f.write("Hello JUNAID")
# print(text)
# f.close()

# with open('textfile.txt','a') as f:
#     f.write("Hello i am junaid!")

# f = open("textfile.txt", 'r')
# i = 0
# while True:
#     i +=1
#     text = f.readline()
#     if not text:
#         break
#     s1 = text.split(",")[0]
#     s2 = text.split(",")[1]
#     s3 = text.split(",")[2]
#     print(f"Marks of student {i} in math {s1}")
#     print(f"Marks of student {i} in math {s2}")
#     print(f"Marks of student {i} in math {s3}")
#     print(text)

# f= open('textfile1.txt','w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']

# text = f.writelines(lines)
# print(text)
# f.close()

# with open('textfile.txt', 'r') as f:
#     print(type(f))

#     f.seek(10)

#     print(f.tell())
#     data = f.read(10)
#     print(data)

# with open('textfile.txt', 'w') as f:
#     f.write("Hello world!")
#     f.truncate(3)

# with open('textfile.txt', 'r') as f:
#     print(f.read())


# square = lambda x: x*x
# print(square(2))

# cube = lambda x: x*x*x
# print(cube(3))

# sum = lambda x,y,z: x + y + z
# print(sum(2,3,4))

# avg = lambda x,y: (x + y) / 2
# print(avg(7,5))

# def fun(fx, val1, val2):
#     return 2 * fx(val1,val2)
# print(fun(lambda x,y: (x + y) / 2 ,44, 4))

# def cube(x):
#     return x*x*x

# def filter_fun(x):
#     return x>3

# from functools import reduce
# def red(x,y):
#     return x + y

# l = [2, 4, 5, 6]
# newl = [] 
# for i in l:
#     newl.append(cube(i))

# newl = list(map(cube, l))
# print(newl)
# newl = list(filter(filter_fun, l))
# print(newl)

# newl = reduce(lambda x,y: x * y , l)
# print(newl)

# a = [1, 2, 3]
# b = [1, 2, 3]

# a = 3
# b = 3

# a = "Peter"
# b = "Peter"

# a = (1, 4)
# b = (1, 4)

# print( a is b)
# print(a == b)

