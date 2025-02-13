# absolute.py
# A program that takes in number and give its absolute value.
# Author: Anna Lozenko

a = float(input("Enter a number: ")) # it is important to specify that a is a number, in this case a float is more relevant to the purpose. We can't apply abs() to a string!
b = abs(a)
print("The absolute number of {} is {}.".format(a, b))