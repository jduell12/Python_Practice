"""
Script for a teacher to send to students reminding them of their missing assignments
Input: asks user for a list of names separated by a comma, list of grades separated
       by a comma, list of missing assignments separated by a comma.  List of names,
       grades and missing assignments should be in order with each other
Output: prints a message with the student's name, grades and number of missing assignments
"""

message = "Hi {}, \n\nThis is a reminder that you have {} assginments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date. \n\n"

names = input("Enter a list of names separated by a comma: ").title().split(",")
assignments = input("Enter a list of missing assignments separated by a comma: ").split(",")
grades = input("Enter a list of grades separated by a comma: ").split(",")

"""
for loop that prints the message to each student with the correct values
the potential grade is the current grade + 2 * number of missing assignments
"""

for name, assignment, grade in zip(names, assignments, grades):
    potential_grade = int(grade) + int(assignment)*2
    print(message.format(name, assignment, grade, potential_grade))
