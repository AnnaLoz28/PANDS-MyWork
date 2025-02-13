# testTypes.py
# A program that checks the type of the variables.
# Author: Anna Lozenko

i = int(input("Enter an integer number: "))
fl = float(input("Enter a float number: "))
bl = bool(input("Enter a boolean value: "))
s = str(input("Enter a string: "))
list = list(input("Enter a list of elements: "))
print("Variable {} is of {} type and value: {}.".format("i", type(i), i))
print("Variable {} is of {} type and value: {}.".format("fl", type(fl), fl))
print("Variable {} is of {} type and value: {}.".format("bl", type(bl), bl))
print("Variable {} is of {} type and value: {}.".format("s", type(s), s))
print("Variable {} is of {} type and value: {}.".format("list", type(list), list))