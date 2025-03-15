#
#
#

# create a new file called count.txt and insert "0" into it


with open("count.txt","w") as f: 
    f.write("0")


# function that reads the number in the count.txt file
def readNumber():
    with open ("count.txt" , "r") as f:
        number = int(f.read())
        return number


# function that takes in a number and overwrites a file with that number
def writeNumber(number):
    with open("count.txt", "wt") as f:
        f.write(str(number)) #we can only write strings, so we need to convert the int number we'll be inputting when calling the function to a str


# program that, uses the two above functions, to count how many times the program has been run. The number is saved in a separate file (count.txt) and is overwritten everytime.
num = readNumber()
num += 1
print("This program has been run {} times.".format(num))
writeNumber(num)