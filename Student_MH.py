# Marcos Hernandez
# Module 8 Assignment

import json

# Function to print student list
def print_students(student_list):
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : "
              f"ID = {student['Student_ID']} , "
              f"Email = {student['Email']}")

# Open and load JSON file
with open(r"C:\Users\Obliv\CSD---325\Student.json", "r") as file:
    students = json.load(file)

# Display original list
print("Original Student List\n")
print_students(students)

# Add new student
new_student = {
    "F_Name": "Marcos",
    "L_Name": "Hernandez",
    "Student_ID": 1577,
    "Email": "mhernandez@gmail.com"
}

students.append(new_student)

# Display updated list
print("\nUpdated Student List\n")
print_students(students)

# Write updated list back to JSON file
with open(r"C:\Users\Obliv\CSD---325\Student.json", "w") as file:
    json.dump(students, file, indent=4)

print("\nThe Student.json file has been updated.")