print("This is my first Programm in Python")
print("This is a poem for kids...")
print("""home to my father’s ashes for thirteen years— and poured its heft into a form she made  on the potter’s wheel—a vase, damp and unfired. 
She pinched the rotating lip, and sealed the clay  
perfectly shut, a technique I haven’t yet mastered.

We planned to launch it like a football at low tide,  
but when we arrived, the beach was lined with people, 
and there was no subtle way for my brother to toss it out past  
the children kneeling in the surf, the surfers awaiting the break. 

To carry my father out, arm above my head, heavy with him— 
or hold him against my chest, side-stroking  
with one hand while the clay disintegrated into the water— 
I wasn’t dressed for it.

Instead, we dropped him in the water by the docks  
by the old Shrimp Shack, all 6’4” of him, 
and I watched the vessel slowly descend, a few bubbles  
emerging as if the last breath left in a dying lung""")


# Comments Signle line and Multi Line


#print("Hello I AM JUNAID!")  This is single line comment

# print("hello")
# print("how are you?") This is multiLine Comment

'''
print("How are you my peter")
print("This is your Friend?")
This is MultiLine Comment
'''

"""
print("This is also multi line comment")
"""


#Escape Sequence Character

print("Hello this is me junaid \nand I am Python dev")
print("Hello this is \"me junaid \nand\" I am Python dev")
print("Hello this is \'me junaid \nand\' I am Python dev")
print("Hello\tWorld!")
print("Hello\rWorld")
print("Jun\raid")


#Print statement Parameters

# seperator
# end
# flush
# file

print("Hi", 9,3, sep="&", end="00", flush="false")
print("Junaid")



# Variables

a = 34.4
b = "Hello"
c = True
d = None
e = 6
f = complex(5 + 6)
print(a + e)
print(b)
print(c)
print(d)
print(f)


#Data Types 

print("Type of a is ", type(a))
print("Type of b is ", type(b))
print("Type of c is ", type(c))
print("Type of f is ", type(f))

list1 = [2, 3.3, [5,6],["Apple", "Bnana"]]
print(list1)

tuple1 = (("peter", "jhon"), ("jack", "vance"))
print(tuple1)

dict1 =   {"name": "Junaid","age": 21}
print(dict1)

#Everything in python is object okay.



# Operators 

print(12+4)
print(12-4)
print(12*4)
print(12/4)
print(12//4)
print(12%4)
print(2**4)


# Excercise 1 

a = 5
b = 4
ans1 = a + b
print("The result of a + b is ",ans1)

ans2 = a - b 
print("The result of a - b is ",ans2)

ans3 = a * b
print("The result of a * b is ",ans3)

ans4 = a / b
print("The result of a / b is ",ans4)


#Type Casting Explicit and Implicit

a = "5"
b = "6"

print(int(a) + int(b))

s1 = "7"
s2 = 9

string_Num = int(s1)
print(string_Num + s2)

a1 = 4.5
a2 = 9
print(a1 + a2)


# Input Function

# x = input("Enter First Number :")
# y = input("Enter Second Number :")

x = 5 
y = 4

a1 = x + y
print(a1)
a1 = int(x) + int(y)
print(int(a1))

a2 = int(x) - int(y)
print(a2)


a3 = int(x) * int(y) 
print(a3)

a4 = int(x) / int(y)
print(a4)

a5 = int(x) // int(y)
print(a5)



#   Strings 

a = "peter"
b = "Hulk"
c = """Hello 
how are
you my friend!"""

print(a)
print(b)
print(c)

print(a[0])
print(a[1])
print(a[2])

print("Using For loop!")
for char in a:
    print(char)

for ch in c:
    print(ch)


num1 = 45
num2 = 23

if num1 > num2:
    for i in range(1,10):
        print(i)
else:
    print("for loop not exicuted!")


# String Slicing 

name = "Junaid"
print(len(name))
print(name[0:5])
print(name[2:5])
print(name[0:-3])
print(name[-5:-2])

print(name[-4:-2])


#   String Methods

name = "Peter!!!!!! !!!!! Peter!!!"
print(len(name))
print(name.upper())
print(name.lower())
print(name.rstrip("!"))
print(name.replace("Peter","Jhon"))
print(name.split(" "))

para = "How are you my Brother And siSter"
print(para.capitalize())

res = "Welcome to Pakistan!"
print(res.center(100))

str1 = "My name is peter and my friend name is also peter"
print(str1.count("peter"))

str1 = "My name is peter and my friend name is also peter"
print(str1.endswith("ter"))

str1 = "My name is peter and my friend name is also peter"
print(str1.endswith("er", 14, 16))

str1 = "My name is peter and my friend name is also peter"
print(str1.find("peters"))

str1 = "ThisISjUNAID"
print(str1.isalnum())

str1 = "Mynameis00"
print(str1.isalpha())

str1 = "sjkdjdksj"
print(str1.islower())

str1 = "My name is peter and my friend name is also peter"
print(str1.startswith("My"))

str1 = "My name is peter and my friend name is also peter"
print(str1.swapcase())

str1 = "My name is peter and my friend name is also peter"
print(str1.title())