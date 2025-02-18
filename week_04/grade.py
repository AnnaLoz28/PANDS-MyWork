# grade.py
# program that reads in a student’s percentage mark and prints out corresponding the grade (the program should check that the percentage is valid):
#   Under 40% => Fail
#   Between 40% and 49% => Pass
#   Between 50% and 59% => Merit 2
#   Between 60% and 69% => Merit 1
#   Over 70% => Distinction

# author: Anna Lozenko

mark = float(input( "Please enter the mark percentage: "))

if mark < 0 or mark > 100:
    print("Error! Please enter a number between 0 and 100.")
elif mark < 40:
    print("Fail")
elif mark < 50:
    print("Pass")
elif mark < 60:
    print("Merit2")
elif mark < 70:
    print("Merit1")
else:
    print("Distinction")