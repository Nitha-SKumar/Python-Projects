from models import StudentManager

manager = StudentManager()

while True:
    print("\nStudent Record Manager - OOP Version")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        manager.add_student()

    elif choice == "2":
        manager.view_students()

    elif choice == "3":
        manager.search_student()

    elif choice == "4":
        manager.update_student_marks()

    elif choice == "5":
        manager.delete_student()

    elif choice == "6":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")