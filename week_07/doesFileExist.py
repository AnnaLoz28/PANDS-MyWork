# if we are running this code on a new machine and we are not sure wether the file count.txt exists, we should check it: 
# we'll need to navigate the current folder and directory. To do that we'll use the os package.
import os 

# get the current working directory
current_dir = os.getcwd()
print(f"The current working directory is {current_dir}.")

#list all the files and folders in the current working directory:
files_wd = os.listdir(current_dir)
print(files_wd)

# check if a file or directory exists using os.path.exists(path)
file = "count.txt" #path
if os.path.exists(file):
    print("The file exists.")
else: 
    print("The file doesn't exist.")

# check if a file exists using the os.path.isfile(path)
if os.path.isfile(file):
    print("The file exists.")
else:
    print("The file doesn't exist.")

if not os.path.isfile(file):
    print("The file doesn't exist.")
    

# we can try and open a file with Try-Except:
try:
    with open ("count.txt", "r") as f:
        print("The file exists.")
        f.read()
except FileNotFoundError:
    print("File not found.")


