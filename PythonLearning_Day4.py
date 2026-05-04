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

def fun():
    try:
        li = [1, 3 , 5 , 5, 7 , 8 ,]
        a = int(input("Enter index : "))
        print(li[a])
        return 1
    except:
        print("Invalid input!")
        return 0
    finally:
        print("I'm always executed!")

a = fun()
print(a)
