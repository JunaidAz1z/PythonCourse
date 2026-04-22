# If Else 

#age = int(input("Enter value of num : "))
# if(age > 18 ):
#     print("Your are adult!")
# else:
#     print("Your are kid!")

# marks = int(input("Enter your markes : "))
# if(marks > 80):
#     print("Your grade is A")
# elif(marks > 70):
#     print("Your garde is B")
# elif(marks > 60):
#     print("Your grade is C")
# elif(marks > 50): 
#     print("Your grade is D")
# else:
#     print("You are fail!")


# num = int(input("Enter a number : "))
# if(num > 50):
#     print("Number is greater than 50")
# elif(num < 50):
#     if(num >= 40):
#         print("Number between 40 to 50 ")
#     elif(num <=40 and num > 30):
#         print("Number between 30 to 40 ")
#     else:
#         print("Number less than 30 ")
# else:
#     print("Number is zero!")


# Exercise 2 

import time

print(time.strftime("%H:%M"))
timeStamp = int(time.strftime("%H"))

if(timeStamp > 6 and timeStamp <=10):
    print("Good Morning!")
elif(timeStamp > 12 and timeStamp < 15):
    print("Good Afternoon!")
elif(timeStamp > 15 and timeStamp < 18):
    print("Good Evening!")
else:
    print("Good Night!")
# time = int(input("Enter the time : "))

# if(time > 6 and time <= 10):
#     print("Good Morning dear!")
# elif(time > 12 and time <= 15):
#     print("Good After Noon!")
# else:
#     print("Good night!")

#   Match Case


# a = int(input("Enter a number : "))

# match a:
#     case 1:
#         print("Value is 1")
#     case 3: 
#         print("Value is 3")
#     case _ if a==10:
#         print(a, "is equal to 10")
#     case _ if a== 50:
#         print(a, "is equal to 50")
#     case _:
#         print(a)

#For Loop

# name = "Peter"
# for i in name:
#     print(i)

# list = ["Jhon", "Kim", "Jack", "Bruce"]

# for name in list:
#     print(name)
#     first = list[1]
#     for i in first:
#         print(i)

# for num in range(1, 100, 5):
#     print(num)

# num = int(input("Enter number : "))

# for i in range(1,11):
#     print( num, " * ",i,  "=", num * i)


#While Loop

# i = 0 
# while(i<4):
#     print(i)
#     i = i +1

# x = int(input('Enter the number'))
# while(x<=50):
#     x = int(input('Enter the number'))
#     print(x)
# else:
#     print("While loop completed!")

# num = int(input('Enter number : '))
# x = 1
# while(x<=10): 
#     print( num, " * ",x,  "=", num * x)
#     x = x + 1


# i = 0
# while True:
#     print(i)
#     i = i +1
#     if(i%100 == 0):
#         break

#Break Continue Statement

# for i in range (20):
#     print (i)
#     if (i == 12):
#         break
# print("Loop completed!")

# for x in range (12):
#     if(x == 6):
#         print("iteration skiped")
#         continue
#     print(x)

#Functions 

def calculateMean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if(a > b):
        print("a is greater than b ")
    else:
        print("b is equal and greater")
def isLesser(a,b):
    if(a < b):
        print("a is less than b ")
    else:
        print("a is equal and greater")

a = 9 
b = 14
isLesser(a,b)
isGreater(a,b)
calculateMean(a,b)
# print(calculateMean)

c = 5
d = 6
isGreater(c,d)
calculateMean(c,d)

#Function Arguments

#Not Require Args
def avg(a=5, b= 8):
    print("Average of number is ", (a + b)/2)

avg()

#Keyword Args
def avg1(a=6, b=9):
    print("Average of number is", (a+b)/2)

avg1(a=9)

def avg2(a=6, b=9):
    print("Average of number is", (a+b)/2)

avg2(9, 11)

#Optional Args
def avg3(a=6, b=9):
    print("Average of number is", (a+b)/2)

avg3(b=50)

#Required Args
def avg4(a, b, c=5):
    print("Average of number is", (a+b+c)/3)

avg4(a=3, b = 7)


#Arbitrary Args

def average(*numb):
    sum = 0
    for i in numb:
        sum = sum + i
        return sum / len(numb)

av = average(3,4)
print(av)

def  sum11(*num):
    sum = 0
    for i in num:
        sum = sum + i
        print("Sum is : ", sum / len(num))

sum11(1,2)

def names(*name):
    print("Hello",name[0], name[1])
names("Jhon", "Peter")

#Keyword Arbitrary 
def name(**nam):
    print("Hi", nam["fname"], nam["lname"])

name(fname = "Peter", lname ="Jack")