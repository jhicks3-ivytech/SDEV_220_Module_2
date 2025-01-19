'''
John Hicks
Module 2 - deans_list.py 

This program takes the name and GPA of a student from user input and decides 
if the student is on the Dean's list or Honor Roll. Once the user enters 'ZZZ' 
to quit, the names that made the lists are printed.
'''
deansList = [] #collects each name of students that make the Dean's List
honorRoll = [] #collects each name of students that make the Honor Roll
while True:
    lastName = input("Enter student's last name or 'ZZZ' to quit: ")
    if lastName.lower() == "zzz":
        break
    firstName = input("Enter student's first name: ")
    gpa = float(input("Enter student's GPA: "))
    if gpa >= 3.5:
        print(f"{firstName} {lastName} has made the Dean's List")
        deansList.append(f"{firstName} {lastName}")
    elif gpa >= 3.25:
        print(f"{firstName} {lastName} has made the Honor Roll")
        honorRoll.append(f"{firstName} {lastName}")
    else:
        print("This student did not make either list")

print("These students made the Dean's List!")
for i in deansList:
    print(i)

print("These students made the Honor Roll List!")
for i in honorRoll:
    print(i)

# Test results with five names:

# Enter student's last name or 'ZZZ' to quit: Hicks
# Enter student's first name: John
# Enter student's GPA: 4
# John Hicks has made the Dean's List
# Enter student's last name or 'ZZZ' to quit: Smith
# Enter student's first name: Jeremy
# Enter student's GPA: 3.5
# Jeremy Smith has made the Dean's List
# Enter student's last name or 'ZZZ' to quit: Weesner
# Enter student's first name: Josh
# Enter student's GPA: 2.7
# This student did not make either list
# Enter student's last name or 'ZZZ' to quit: Hernandez
# Enter student's first name: Bobby
# Enter student's GPA: 3.4
# Bobby Hernandez has made the Honor Roll
# Enter student's last name or 'ZZZ' to quit: Steproe
# Enter student's first name: Erin
# Enter student's GPA: 3.25
# Erin Steproe has made the Honor Roll
# Enter student's last name or 'ZZZ' to quit: zzz
# These students made the Dean's List!
# John Hicks
# Jeremy Smith
# These students made the Honor Roll List!
# Bobby Hernandez
# Erin Steproe