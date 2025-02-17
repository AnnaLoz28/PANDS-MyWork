# normalize.py
# a program that reads in a string and strips any leading or trailing spaces, the program should also convert the string to lower case. The program should also output the length of the input and output strings.
# Author: Anna Lozenko

def normalize (string):
    normalized = string.strip().lower()
    original_length = len(string)
    reduced_length = len(normalized)
    print("That string normalized is {}.".format(normalized))
    print("We reduced the input string from {} to {} characters".format(original_length, reduced_length))

string = str(input(f"Please enter a string: "))

normalize(string)