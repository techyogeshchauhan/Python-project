# # Initialize an empty dictionary to store student names and grades
# student_grades = {}

# def add_student(name, grade):
#     student_grades[name] = grade
#     print(f"Added student: {name} with grade: {grade}")

# def update_grade(name, grade):
#     if name in student_grades:
#         student_grades[name] = grade
#         print(f"Updated {name}'s grade to: {grade}")
#     else:
#         print(f"Student {name} not found.")

# def display_students():
#     if not student_grades:
#         print("No students in the dictionary.")
#     else:
#         print("Student Grades:")
#         for name, grade in student_grades.items():
#             print(f"{name}: {grade}")

# def main():
#     while True:
#         print("\nStudent Management System")
#         print("1. Add Student")
#         print("2. Update Grade")
#         print("3. Display All Students")
#         print("4. Exit")

#         choice = input("Enter your choice (1/2/3/4): ")

#         if choice == '1':
#             name = input("Enter the student's name: ")
#             grade = input("Enter the student's grade: ")
#             add_student(name, grade)
#         elif choice == '2':
#             name = input("Enter the student's name: ")
#             grade = input("Enter the new grade: ")
#             update_grade(name, grade)
#         elif choice == '3':
#             display_students()
#         elif choice == '4':
#             print("Exiting the program.")
#             break
#         else:
#             print("Invalid choice. Please enter a valid option.")

# # Run the main function
# main()

# Initialize an empty dictionary to store student names and grades
student_grades = {}

# Function to add a student and their grade
def add_student(name, grade):
    student_grades[name] = grade
    print(f"Added student: {name} with grade: {grade}")

# Function to update a student's grade
def update_grade(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"Updated {name}'s grade to: {grade}")
    else:
        print(f"Student {name} not found.")

# Function to display all students and their grades
def display_students():
    if not student_grades:
        print("No students in the dictionary.")
    else:
        print("Student Grades:")
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")

# Main function for the menu-driven student management system
def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Grade")
        print("3. Display All Students")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            name = input("Enter the student's name: ")
            grade = input("Enter the student's grade: ")
            add_student(name, grade)
        elif choice == '2':
            name = input("Enter the student's name: ")
            grade = input("Enter the new grade: ")
            update_grade(name, grade)
        elif choice == '3':
            display_students()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Run the main function
main()
