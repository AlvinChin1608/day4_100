import random
import my_module

#specifying the range of integer from 1-10
random_integer = random.randint(1,10)
print(random_integer)

print(my_module.pi)

random_float = random.random()
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

#Understanding the Offset and Appending items to list
state_of_america = ["Delaware", "Pennsylvania", "New York, Georgia"]
print(state_of_america[0])
print(state_of_america[-1])

state_of_america[2] = "Pencil"

#Append will add a single item to the end of the list
state_of_america.append("Singapore")

#To add more into the list we can extend
state_of_america.extend(["Bristol", "Jakarta"])
print(state_of_america)

#Have a look on Data Structure on the Python Documentation
# Exercise Challenge - Random
"""
write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails"
Important, the first letter should be capitalised and spelt exactly, cuz it is case-sensitive

Generate a random number, either 0 or 1. Then use that number to print out "Heads" or "Tails"
"""
import random

Random_generator = random.randint(0,1)
if Random_generator == 0:
  print("Heads")
else:
  print("Tails")

#Exercise - Challenge
"""
Write a program that will select a random name froma list of names. The person selected will have to pay for everybody's food bill. 

Important: you are not allowed to use the choice() functions

Line 1 splits the string names _string into individual names and puts them inside a List called names. For this to work, you must enter all the names as names followed by comma then space. Eg. name, name, name

Note: Dont worry about getting hold of the input()

"""

import random 

names_string = input("Please insert your names separated by commas: ")
names = names_string.split(", ")
rand_picker = random.choice(names)
print(rand_picker, "is going to pay for the meal today")

#Method 2 - without using choice() function

import random 

names_string = input("Please insert your names separated by commas: ")
names = names_string.split(", ")
#lets count the number of input using the len function
size = len(names)

random_picker = random.randint(0 ,size - 1)
print(names[random_picker], "is going to pay for the meal today")

#How to create List inside of a List? - Nested Listed 
fruits = ["strawberries", "Apples", "Durian", "Rambutan"]
vegetables = ["Spinach", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

#Challenge - Marking the map on the treasure map
"""
Write a program that will mark a spot on a map with an X
In the code, you will find a variable called map
This map contains a nested list. When map is printed this is what it looks like, notice the nesting:

[['▩','▩','▩'],['▩','▩','▩'],['▩','▩','▩']]

for ex, B3 to mark, X is the treature

also we want to print 3 x 3 instead of a line
"""
line1 = ["▩","▩","▩"]
line2 = ["▩","▩","▩"]
line3 = ["▩","▩","▩"]

map = [line1, line2, line3]
position = input()
#lets turn just the first input 
#which is the alphabet to lower case, to make it uniform
letter = position[0].lower()
abc = ["a","b","c"]

#if the letter was b, then index would give us the number 1, c = 2..
letter_index = abc.index(letter)

#now, we are looking at he second index, which is the number. 
#because user type 1 to 3 instead of 0 to 2, we need to sub 1
number_index = int(position[1]) - 1

#Change the map box to "X" as user type in the spot
map[letter_index][number_index] = "X"

print(f"{line1}\n{line2}\n{line3}")


