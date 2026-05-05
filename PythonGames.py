import random
rules = {
    1 : 2,
    2 : 3,
    3 : 1
}
print("Lets play a game!")
print("1 for Snake      2 for Water         3 for Gun")
num = random.randint(1,3)
select = int(input("Your answer is : "))
print(f"Computer answer is : {num}")

if (select == num):
    print("Draw")
elif (rules[select] == num):
    print("User wins!")
else:
    print("Computer wins!")