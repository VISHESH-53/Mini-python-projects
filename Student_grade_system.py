import array

from requests import delete
student={'Paras': 85, 'Rahul': 92, 'Sneha': 78, 'Anjali': 88, 'Vikram': 95}
def add_student(name, grade):
    student[name] = grade
    print(f"Added student: {name} with grade: {grade}")

def update_student(name, grade):
    if name in student:
        student[name] = grade
        print(f"Updated student: {name} with new grade: {grade}")
    else:
        print(f"Student {name} not found.")
def delete_student(name):
    if name in student:
        del student[name]
        print(f"Deleted student: {name}")
    else:
        print(f"Student {name} not found.")
def view_students():
    if student:
        print("Student Grades:")
        for name, grade in student.items():
            print(f"{name}: {grade}")
    else:
        print("No students found.")
while True:
    print("\nStudent Grade System")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. View Students")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        name = input("Enter student name: ")
        grade = int(input("Enter student marks: "))
        add_student(name, grade)
    elif choice == '2':
        name = input("Enter student name to update: ")
        grade = int(input("Enter new grade: "))
        update_student(name, grade)
    elif choice == '3':
        name = input("Enter student name to delete: ")
        delete_student(name)
    elif choice == '4':
        view_students()
    elif choice == '5':
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please try again.")


