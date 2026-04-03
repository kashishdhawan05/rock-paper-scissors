import random
'''
1 for rock
-1 for paper
0 for scissor
'''
# Computer Choice
computer = random.choice([-1,0,1])

#User Input
youstr =input("Enter your choice: ")
youDict = {"r":1,"p":-1,'s':0}
reverseDict = {1:"rock",-1:"paper",0:"scissor"}
you = youDict[youstr]

# By now we have two numbers (variables) , you and computer

print(f" you chose {reverseDict[you]}\ncomputer choose {reverseDict[computer]}")

# Game Logic
if computer == you:
  print("It's a draw!")
else:
 if computer == -1 and you == 1:
  print("you win!")
 elif computer == -1 and you == 0:
  print("you lose!")
 elif computer == 1 and you == -1:
  print("you lose!")
 elif computer == 1 and you == 0:
    print("you win!")
 elif computer == 0 and you == -1:
    print("you lose!")
 elif computer == 0 and you == 1:
    print("you win!")
 else:
    print("something went wrong")
