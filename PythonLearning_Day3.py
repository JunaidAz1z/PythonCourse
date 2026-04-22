#Lists

# lst = [2,4,6,8]
# print(lst)
# print(type(lst))
# lst1 = ["Red", "Green", "Blue", 4, 7, 9]
# if "Green" in lst1:
#     print("yes")
# else:
#     print("no")
# print(lst1)
# print(lst1[0])
# for i in lst1:
#     print(i)
# print(lst1)

# print(lst1[1:])
# print(lst1[0:6:2])
# print(lst1[::2])

# #List Comprension

# lst2 = [i for i in range(10)]
# print(lst2)

# lst3 = [i for i in range(10) if i%2==0]
# print(lst3)

# names = ["Peter", "Jack", "Jhon", "Matty", "Jimmy"]
# lsst = [item for item in names if "a" in item]
# print(lsst)
# names1 = ["Peter", "Jack", "Jhon", "Matty", "Jimmy"]

# lst4 = [item for item in names1 if len(item) > 4]
# print(lst4)

#List Methods

# numList = [2, 45, 3, 4, 556, 78]
# numList.append(666)
# numList.pop(2)
# numList.sort()
# numList.reverse()
# print(numList.count(4))
# print(numList.index(78))
# numList.insert(1, 22)
# m = numList.copy()
# print(m)
# m = [34, 45 ,56]
# numList.extend(m)
# print(numList)

#Tuple
# tup = (1, 4 ,7, 99, 34, 67, 55)
# if 99 in tup:
#     print("Yes")
# else:
#     print("No")
# print(tup[1])
# print(tup.count(1))
# print(tup)
# print(tup[1:7:2])
# print(tup[1:4])

# subjects = ("Math", "English", "Urdu")
# print(subjects)
# temp = list(subjects)
# temp.append("Arabic")
# temp.remove("English")
# temp[1] = "Computer"
# subjects = tuple(temp)
# print(subjects)

# city1 = ("rwp", "isb")
# city2 = ("lhr", "qta")
# city = city1 + city2
# print(city)

# tuple1 = (2, 4, 5, 6, 7, 8, 1, 4)
# print(tuple1.index(4))
# print(tuple1.index(4, 2, 8))


#Exercise 

#Question ho fir options hon aur input lena 
# answer aur correct or incorrect

# question1 = {"question":"What is the capital of Pakistan", "options": ["(a) Karachi", "(b) Lahore", "(c) Islamabad"], "answer":"c" }
# question2 = {"question":"Who is the PM of Pakistan", "options": ["(a) Ali", "(b) Peter", "(c) Jhon"], "answer":"a" }
# question3 = {"question":"When pakistan was made", "options": ["(a) 1945", "(b) 1946", "(c) 1947"], "answer":"c" }
# question4 = {"question":"How many province of Pakistan", "options": ["(a) 3", "(b) 4", "(c) 5"], "answer":"b" }
# question5 = {"question":"Pakistan Nationl sport", "options": ["(a) Cricket", "(b) Hockey", "(c) Football"], "answer":"b" }

# allques = [
#     question1,
#     question2,
#     question3,
#     question4,
#     question5,
# ]
# score = 0
# for i in allques:
#     print(i["question"])
#     for opt in i["options"]:
#         print(opt)
   
#     ans = input("chosse the option : ")
#     if ans == i["answer"]:
#         score = score + 50
#         print("Your ans is correct and your score is :", score)
#     else:
#         score = score + 0
#         print("Incorrect your score is :", score)
# print("Game Over!!!")
# print("Your total score is ", score)


#F-String

sentence = "Hello my name is {0} and my age is {1}"
name = "Peter"
age = 21
print(sentence.format(name, age))

fstr = f"My name is {name} and my age is {age}"
print(fstr)

weight = 83.3433
print(f"The weight is {weight:.2f} grams")

print(f"{4*10}")

#Docstring

def square(n):
    '''This method takes number and returns the square
    '''
    print(n**2)
square(9)
print(square.__doc__)