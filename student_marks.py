# Task 1: Dictionary of Student Marks

students = {
    "Amit": 85,
    "Riya": 90,
    "Sahil": 78,
    "Neha": 92
}

name = input("Enter student name: ")

if name in students:
    print("Marks of", name, "are:", students[name])
else:
    print("Student not found in the dictionary.")
