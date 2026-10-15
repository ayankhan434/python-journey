
import json
import os

FILE_NAME = "students.json"


# adding studebt
def load_students():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Error: Could not read student file.")
        return []


# saving studen
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# CREATE: Add a student
def add_student():
    students = load_students()

    try:
        roll_no = int(input("Enter roll number: "))

        for student in students:
            if student["roll_no"] == roll_no:
                print("Roll number already exists!")
                return

        name = input("Enter student name: ").strip()
        if not name:
            print("Name cannot be empty!")
            return

        marks = float(input("Enter marks (0-100): "))
        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100!")
            return

        student = {
            "roll_no": roll_no,
            "name": name,
            "marks": marks
        }

        students.append(student)
        save_students(students)
        print("Student added successfully!")

    except ValueError:
        print("Please enter valid numeric values.")


# READ: showing  all students
def view_students():
    students = load_students()

    if not students:
        print("No student records found.")
        return

    print("\n--- STUDENT RECORDS ---")
    for student in students:
        print(
            f"Roll No: {student['roll_no']} | "
            f"Name: {student['name']} | "
            f"Marks: {student['marks']}"
        )


# SEARCH: Finding any  student by roll number
def search_student():
    students = load_students()

    try:
        roll_no = int(input("Enter roll number to search: "))

        for student in students:
            if student["roll_no"] == roll_no:
                print("\nStudent found!")
                print(student)
                return

        print("Student not found.")

    except ValueError:
        print("Roll number must be an integer.")


# UPDATE: adding somthing to allready available student
def update_student():
    students = load_students()

    try:
        roll_no = int(input("Enter roll number to update: "))

        for student in students:
            if student["roll_no"] == roll_no:
                print("1. Update name")
                print("2. Update marks")

                choice = input("Choose an option: ")

                if choice == "1":
                    name = input("Enter new name: ").strip()
                    if not name:
                        print("Name cannot be empty!")
                        return
                    student["name"] = name

                elif choice == "2":
                    marks = float(input("Enter new marks (0-100): "))
                    if not 0 <= marks <= 100:
                        print("Marks must be between 0 and 100!")
                        return
                    student["marks"] = marks

                else:
                    print("Invalid choice.")
                    return

                save_students(students)
                print("Student updated successfully!")
                return

        print("Student not found.")

    except ValueError:
        print("Please enter valid numeric values.")


# DELETE: Removing a student from records file
def delete_student():
    students = load_students()

    try:
        roll_no = int(input("Enter roll number to delete: "))

        for student in students:
            if student["roll_no"] == roll_no:
                students.remove(student)
                save_students(students)
                print("Student deleted successfully!")
                return

        print("Student not found.")

    except ValueError:
        print("Roll number must be an integer.")


# ANALYTICS: Calculate student statistics
def student_analytics():
    students = load_students()

    if not students:
        print("No records available for analysis.")
        return

    marks_list = [student["marks"] for student in students]

    average = sum(marks_list) / len(marks_list)
    topper = max(students, key=lambda student: student["marks"])

    print("\n--- STUDENT ANALYTICS ---")
    print("Total students:", len(students))
    print(f"Average marks: {average:.2f}")
    print("Highest scorer:", topper["name"])
    print("Highest marks:", topper["marks"])


# Main menu
def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Student Analytics")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            student_analytics()
        elif choice == "7":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
