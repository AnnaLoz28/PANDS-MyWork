# evens.py
# Prints out all the even numbers from 2 to 100 
# Author: Anna Lozenko

number = range(2, 101)

index = 0
while index < len(number):
    if number[index] % 2 == 0:
        print(number[index])
    index = index + 1
