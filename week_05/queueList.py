# queueList.py
# program that puts 10 random numbers into a queue(list), the program should then output all the values in the queue, then take the numbers from the queue one at a time, print it and the current numbers still in the queue.
# author: Anna Lozenko

import random

queue = []

# create a list of 10 random integers into a queue [] list
while len(queue) < 10:
    q = random.randint (0, 100)
    queue.append(q)
   
print(queue)
for q in range(len(queue)):        #output all (remaining) values in the queue
    a = queue.pop(0)  #takes the first element out of a list
    print(f"current number is {a} and the queue is {queue} ")        #output the number that has been taken out
print("the queue is now empty")    
   

