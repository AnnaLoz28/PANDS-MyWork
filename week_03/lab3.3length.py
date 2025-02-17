# length.py
# program that reads in a string and outputs how long it is.
# Author: Anna Lozenko

def string_length (word):
    print("The length of {} is {}.".format(word,len(word)))

word = str(input("Please enter a string: "))

string_length(word)