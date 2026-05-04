#Recursion 

#Factorial of 5

def fac(n):
    if (n ==0 or n ==1):
        return 1
    else:
        return n * fac(n-1)
print(fac(5))

# 5 * fac(4)
# 5 * 4 * fac(3)
# 5 * 4 * 3 * fac(2)
# 5 * 4 * 3 * 2 * fac(1)
# 5 * 4 * 3 * 2 * 1


# F(0) = 0 
# F(1) = 1
# F(2) = F(1) + F(0)
# F(n) = F(n-1) + F(n-2)

def f(n):
    if (n == 0):
        return 0
    elif (n ==1):
        return 1
    else:
        return f(n-1) + f(n-2)

print(f(6))
# for i in range(6):
#     print(f(i))
# 0 1 1 2 3 5 8

#Count Down

def count(n):
    if n == 0:
        print("Done!")
    else:
        print(n)
        count(n-1)
print(count(4))

#Sets 

numb = {3, 43, 5, 6, 3}
print(type(numb))
print(numb)

set1 = set()
print(type(set1))

for i in numb:
    print(i)

#Sets Functions 

setA = {3, 34, 5, 6, 8, 3}
setB = {5, 6, 7, 4}

# print(setA.union(setB))
# print(setA.update(setB))
# print(setA)

# print(setA.intersection(setB))
# print(setA)

# 

setC = {"Lhr", "Rwp", "Pes"}
setD = {"Krachi", "Qta"}

print(setC.isdisjoint(setD))

setE = {"Lhr", "Rwp", "Pes"}
setF = {"Rwp", "Lhr"}

print(setE.issuperset(setF))


cities = {"Rwp", "Isb", "Pes", "Lhr"}
cities.add("Karachi")
print(cities)
cities.remove("Pes")
print(cities)

cities.pop()
print(cities)

cities.clear()
print(cities)


dic = {
    "Peter": "Human",
    "Dog": "Animal",
    "Chiar": "Object"
}

print(dic)
print(dic["Peter"])
print(dic.keys())
print(dic.values())

for key in dic.keys():
    print(f"The key is {dic[key]}")

emp = {1: 69, 2: 34, 3: 89, 4: 78}
emp1 = {5: 45, 6: 82}

# emp.update(emp1)
# emp.pop(4)
# emp.clear()
# emp.popitem()
del emp[2]
print(emp)

#Else with loops

for i in range(7):
    print(i)
    if i == 4:
        break
else:
    print("Out of loop!")


# a = input("Enter a number: ")

# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i} = {int(a) * i}")
# except:
#     print("Invalid Input!")
# print("This is important code!")
# print("End of this code!")


# try:
#     a = int(input("Enter a number"))
#     num = [2, 4]
#     print(num[a])

# except ValueError:
#     print("Invalid input")

# except IndexError:
#     print("Index error")


#Finlly works with function 

# def fun():
#     try:
#         li = [1, 3 , 5 , 5, 7 , 8 ,]
#         a = int(input("Enter index : "))
#         print(li[a])
#         return 1
#     except:
#         print("Invalid input!")
#         return 0
#     finally:
#         print("I'm always executed!")

# a = fun()
# print(a)

# a = input("Enter a number between 5 and 9 !")
# if ( a == "quit"):
#     print("Stopped!")
#     exit()
# # else:
# #     raise TypeError("Invalid String")
# b = int(a)
# if(b<5 or b>9):
#     raise ValueError("Invalid value sssss!")
# else:
#     print(f"Your input is {a}")


# questions = [
#     ["What language is used for making FB ? ", "Java", "Python", "React", "Php", None, 4],
#     ["What language is used for making FB ? ", "Java", "Python", "React", "Php", None, 4],
#     ["What language is used for making FB ? ", "Java", "Python", "React", "Php", None, 4],
#     ["What language is used for making FB ? ", "Java", "Python", "React", "Php", None, 4],
#     ["What language is used for making FB ? ", "Java", "Python", "React", "Php", None, 4],
#     ["What language is used for making FB ? ", "Java", "Python", "React", "Php", None, 4],
#     ["What language is used for making FB ? ", "Java", "Python", "React", "Php", None, 4],
#     ["What language is used for making FB ? ", "Java", "Python", "React", "Php", None, 4],
#     ["What language is used for making FB ? ", "Java", "Python", "React", "Php", None, 4],
 
   
# ]

# levels = [1000, 2000, 3000, 10000, 20000, 60000, 120000, 240000, 350000]
# money = 0
# for i in range(0, len(questions)):
#     question = questions[i]
#     print(f"Question for Rs. {levels[i]}")
#     print(f"a. {question[1]}       b. {question[2]}")
#     print(f"c. {question[3]}       d. {question[4]}")
#     reply = int(input("Enter answer between (1 to 4) : "))
#     if(reply == question[-1]):
#         print(f"Correct answer you won Rs {levels[i]}")
#         if(i == 4):
#             money = 10000
#         elif( i == 9):
#             money = 350000
#     else:
#         print("Wrong answer!")
#         break
# print(f"Your take home money is {money}")   

# questions = [
#     ["What language is used for making FB ? ", "Java", "Python", "React", "Php", None, 4],
#     ["What language is used for making FB ? ", "Java", "Python", "React", "Php", None, 4],
#     ["What language is used for making FB ? ", "Java", "Python", "React", "Php", None, 4],
#     ["What language is used for making FB ? ", "Java", "Python", "React", "Php", None, 4],
#     ["What language is used for making FB ? ", "Java", "Python", "React", "Php", None, 4],
#     ["What language is used for making FB ? ", "Java", "Python", "React", "Php", None, 4],
#     ["What language is used for making FB ? ", "Java", "Python", "React", "Php", None, 4],
#     ["What language is used for making FB ? ", "Java", "Python", "React", "Php", None, 4],
#     ["What language is used for making FB ? ", "Java", "Python", "React", "Php", None, 4],
 
   
# ]

# levels = [10, 200, 300, 600, 1200, 2400, 4800, 9600, 19200]
# money = 0

# for i in range(0, len(questions)):
#     question = questions[i]
#     print(question[0])
#     print(f"Question for Rs. {levels[i]}")
#     print(f"a. {question[1] }       b. {question[2]}")
#     print(f"c. {question[3]}        d. {question[4]}")
#     reply = int(input("Enter answer between (1 to 4) : "))
#     if (reply == question[-1]):
#         print(f"Correct answer {levels[i]}")
#         if (i == 3):
#             money = 600
#         elif(i == 6):
#             money = 4800
#         elif(i == 8):
#             money = 19200
#     else:
#         print("Wrong answer!")
#         break
# print(f"Your total earned money is {money}")

# import random
# word = input("Enter word : ")
# if (len(word) < 3):
#     print(word[::-1])
# else:
#    mword = word[1:] + word[0]
#    print("abc" + mword + "xyz")

# sentence = "Hello who is this"
# word = sentence.split()
# print(word)

# for i in range(len(word)):
#     if(len(word[i]) < 3):
#         print(word[i][::-1])
#     else:
#         mword = word[i][1:] + word[i][0]
#         print("abc" + mword + "xyz") 

a = 349
b = 55
print("A") if a > b else print("=") if a == b else print("B")

c = 9 if a < b else 0
print(c)

# marks = [34, 45, 45, 76, 98, 54]
# index = 0
# for mark in marks:
#     if (index == 3):
#         print("Awesome junaid")
#     index +=1

marks = [23, 45, 56, 76, 32]
for index, mark in enumerate(marks):
    print(mark)
    if(index == 2):
        print("Awesome Dear Uswa")

fruits = ["apple", "bnana", "mango"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
