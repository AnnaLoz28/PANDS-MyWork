# div.py
# a program (div.py) that reads in two numbers and divides the first one by the second and give the integer result and the remainder.
# Author: Anna Lozenko

a = int(input("Enter the first number: "))
b  = int(input("Enter the second number: "))
res1 = int(a//b)
res2 = a%b 
print("{} divided by {} is {} with the remainder {}.".format(a, b, res1, res2))
