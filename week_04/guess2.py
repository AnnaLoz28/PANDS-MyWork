# guess2.py
# program that prompts the user to guess a number, the program should keep prompting the user to guess the number until the user gets the right on.
# the program tells the user if there guess is too high or too low, each time they guess (improved version of guess1.py)
# Author: Anna Lozenko

correct_number = 30

number = int(input("Please, guess the correct number: "))
while number != correct_number:
    print ("Wrong! Please, guess again!")
    if number > correct_number:
        print("Wrong! The number you've chosen is too high! Please, guess the number again: ")
    else: 
        print("Wrong! The number you've chosen is too low! Please, guess the number again: ") 
    number = int(input("Please, guess the number again: "))
print("Well done! The number was ", correct_number)    