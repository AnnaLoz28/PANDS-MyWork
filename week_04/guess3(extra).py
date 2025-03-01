# guess3.py
# program that prompts the user to guess a number, the program should keep prompting the user to guess the number until the user gets the right on.
# the program tells the user if there guess is too high or too low, each time they guess 
# the program generates a random number between 0 and 100 to guess (improved version of guess1.py and guess2.py)
# Author: Anna Lozenko

import random

correct_number = random.randint(0, 101)

number = int(input("Please, guess the number: "))
while number != correct_number:
    if number > correct_number:
        print("Wrong! The number is too high! Please, enter a new number: ")
    else: 
        print("Wrong! The number is too low! Please, enter a new number: ")
    number = int(input ("Please, enter a new number: "))
print("Well done! The correct number was ", correct_number)
