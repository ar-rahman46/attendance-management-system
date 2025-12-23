# Attendance Management System (Python)

def add_student():
    name = input("Enter student name: ")
    with open("attendance.txt", "a") as file:
        file.write(f"{name},Not Marked\n")
    print("Student added successfully.\n")


def mark_attendance():
    name = input("Enter student name: ")
    status = input("Enter attendance (Present/Absent): ")

    lines = []
    found = False

    with open("attendance.txt", "r") as file:
        lines = file.readlines()

    with open("attendance.txt", "w") as file:
        for line in lines:
            student, _ = line.strip().split(",")
            if student.lower() == name.lower():
                file.write(f"{student},{status}\n")
                found = True
            else:
                file.write(line)

    if found:
        print("Attendance marked successfully.\n")
    else:
        print("Student not found.\n")


def view_attendance():
    print("\n--- Attendance Records ---")
    with open("attendance.txt", "r") as file:
        for line in file:
            student, status = line.strip().split(",")
            print(f"{student} : {status}")
    print()


while True:
    print("Attendance Management System")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        mark_attendance()
    elif choice == "3":
        view_attendance()
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.\n")
