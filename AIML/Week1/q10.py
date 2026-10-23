# q10.py
# Dictionaries with lists

# Dictionary mapping student names to a list of marks in 3 subjects
students_data = {
    "Aarav": [85, 90, 88],
    "Diya": [92, 95, 91],
    "Rohan": [78, 82, 80],
    "Ananya": [94, 89, 96]
}

print("Student Marks & Averages:\n")

# Each student and their marks
for name, marks in students_data.items():
    # Calculate average using sum() and len()
    average_mark = sum(marks) / len(marks)
    print(f"{name:10}   Marks: {marks}      Average: {average_mark:.2f}")
