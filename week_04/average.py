# average.py
# that keeps reading numbers until the user enters a 0. (the program should append each of them into a list)
# The program should then print out each of the numbers entered and the average of them. (Use a list)
# Author: Anna Lozenko

numbers = []


while True:
    number = int(input("Enter a number (0 to quit): "))
    if number == 0:
        break 
    numbers.append(number)

sum = 0.0 

for n in numbers:
    print(n)
    sum = sum + n 

print("the average is ", sum/len(numbers))  
           
    
