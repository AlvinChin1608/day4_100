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

#Write your code below this line 
import random

game_options = [rock, paper, scissors]

#Get user input for their choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))

#Display their choice 
print("You chose: ")
print(game_options[user_choice])

random_picker = random.randint(0,2)
# print(random_picker) ..just checking if it is working

print("Computer chose: ")
print(game_options[random_picker])

if random_picker == user_choice:
  print("You Win!")
else:
  print("You lose")
