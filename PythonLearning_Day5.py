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