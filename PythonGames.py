# import random
# rules = {
#     1 : 2,
#     2 : 3,
#     3 : 1
# }
# print("Lets play a game!")
# print("1 for Snake      2 for Water         3 for Gun")
# num = random.randint(1,3)
# select = int(input("Your answer is : "))
# print(f"Computer answer is : {num}")

# if (select == num):
#     print("Draw")
# elif (rules[select] == num):
#     print("User wins!")
# else:
#     print("Computer wins!")

# 2nd Method 
# import random 

# def game(u, c):
    
#     if(u == c):
#         return 0

#     elif(u == 1 and c == 3):
#         return -1
#     elif(u == 2 and c == 1):
#         return -1
#     elif(u == 3 and c == 2):
#         return -1
#     else:
#         return 1
    
# print("1 for Snake      2 for Water         3 for Gun")
# u = int(input("User Choice : "))
# c = random.randint(1,3)
# print(f"Computer Choice : {c}")
# score = game(u, c)
# if (score == 0):
#     print('Draw')
# elif(score == -1):
#     print("Loss")
# else:
#     print("You won")

                                #Quiz Game
# questions = [ 
#              {"question":"What is the capital of Pakitan", "Option":"(a) Karachi (b) Lahore (c) Islamabad", "answer": 3}, 
#              {"question":"How many rivers in Punjab", "Option":"(a) 3 (b) 5 (c) 7", "answer": 2}, 
#              {"question":"What is the name of founder of Pakistan", "Option":"(a) Sir syed (b) Allama Iqbal (c) Quaid-e-Azam", "answer": 3, } 
# ]
# marks = 0
# for q in questions:
#      print(q["question"])
#      print(q["Option"])
#      reply = int(input("Choose the correct option!"))
#      if(reply == q["answer"]):
#           marks = marks + 10
#           print("Correct Answer!")
#           print(f"Your current marks are {marks}")
#      else:
#         print("Wrong Answer.")
# print(f"Your total marks are {marks}")