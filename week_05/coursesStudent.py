# coursesStudent.py
# program that stores a student name and a list of her courses and grades in a dict, the program should then print out her data. The number of course she has could change.




student = {
    "name" : "Mary",
    "surname" : "Smith",
    "courses" : [
        {
            "courseName" : "programming",
            "mark" : 45
        },
        {
            "courseName" : "history",
            "mark" : 99
        }
    ]
}

print("Student: {}".format(student["name"]))
for courses in student ["courses"]:
    print("\t {} \t: {}".format(courses["courseName"], courses["mark"]))
