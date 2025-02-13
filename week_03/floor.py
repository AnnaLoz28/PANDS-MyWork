# floor.py
# A program (floor.py), that takes in a float and outputs an int rounded dow.
# The program uses the math module.
# Author: Anna Lozenko

import math 
a = float(input("Enter a float that you want to round down: "))
round_floor= math.floor(a)
print("{} floored is {}.".format(a, round_floor))