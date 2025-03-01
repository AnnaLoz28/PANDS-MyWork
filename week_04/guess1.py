# guess1.py
# program that prompts the user to guess a number, the program should keep prompting the user to guess the number until the user gets the right on.
# Author: Anna Lozenko


correct_number = 5

number = int(input("Please, guess the number: "))
while number != correct_number:
    print("Wrong! Please, guess again!") 
    number = int(input("Please, guess again: "))
print ("Well done! Yes, the number was", correct_number)
    
   
    
    
