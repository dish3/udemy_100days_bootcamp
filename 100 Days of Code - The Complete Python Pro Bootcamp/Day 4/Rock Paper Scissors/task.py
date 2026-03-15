rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
a=input("enter your choice : (rock, paper, scissor) : ").lower()
if a == "rock":
    a = rock
elif a == "paper":
    a = paper
elif a == "scissor" or a == "scissors":
    a = scissors
else:
    print("invalid input")
    exit()

import random
comp=[rock,paper,scissors]
i=random.choice(comp)

print("You chose:")
print(a)
print("Computer chose:")
print(i)

if a==i:
    print("draw")
elif i==rock and a==scissors:
    print("you loss")
elif i==scissors and a==rock:
    print("you won")
elif i==paper and a==rock:
    print("you lose")
elif i==scissors and a==paper:
    print("you lose")
elif i==rock and a==paper:
    print("you won")
elif i==paper and a==scissors:
    print("you won")
else:
    print("invalid input")