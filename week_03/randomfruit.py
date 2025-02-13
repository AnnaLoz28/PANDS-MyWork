# randomfruit.py
# a program that prints out random fruits.
# the program uses the random module.
# Author: Anna Lozenko

import random 

fruits = ["orange", "apple", "kiwi", "cherry", "coco", "clementine", "banana"]

# create index to randomly access elements from the fruits list, i.e randomly select ints

index = random.randint(0, len(fruits)-1)
random_fruit = fruits[index]
print("A random fruit is: {}.".format(random_fruit))