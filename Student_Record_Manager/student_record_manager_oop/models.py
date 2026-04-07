import json

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        total_marks = sum(self.marks)
        average_marks = total_marks / len(self.marks)
        return round(average_marks, 2)

    def to_dict(self):
        return {
            "name": self.name,
            "marks": self.marks
        }


class StudentManager:
    def __init__(self):
        self.students = []
        self.load_data()

    def save_data(self):
        student_data = []

        for student in self.students:
            student_data.append(student.to_dict())

        with open("students.json", "w") as file:
            json.dump(student_data, file, indent=4)

    def load_data(self):
        try:
            with open("students.json", "r") as file:
                student_data = json.load(file)

            for item in student_data:
                student = Student(item["name"], item["marks"])
                self.students.append(student)

        except (FileNotFoundError, json.JSONDecodeError):
            self.students = []

    def add_student(self):
        name = input("Enter student name: ")

        if not name.strip():
            print("Student name cannot be empty.")
            return

        for student in self.students:
            if student.name.lower() == name.lower():
                print("Student already exists.")
                return

        try:
            m1 = int(input("Enter mark 1: "))
            m2 = int(input("Enter mark 2: "))
            m3 = int(input("Enter mark 3: "))
        except ValueError:
            print("Please enter only numbers for marks.")
            return

        if m1 < 0 or m1 > 100 or m2 < 0 or m2 > 100 or m3 < 0 or m3 > 100:
            print("Marks must be between 0 and 100.")
            return

        student = Student(name, [m1, m2, m3])
        self.students.append(student)
        self.save_data()

        print("Student added successfully.")

    def view_students(self):
        if not self.students:
            print("No student data available.")
            return

        highest_average = 0
        topper_name = ""

        for student in self.students:
            average_marks = student.calculate_average()
            total_marks = sum(student.marks)

            if average_marks > highest_average:
                highest_average = average_marks
                topper_name = student.name

            print("Name:", student.name)
            print("Marks:", student.marks)
            print("Total marks:", total_marks)
            print("Average:", average_marks)
            print()

        print("-----------------------------")
        print("Topper:", topper_name)
        print("Highest Average:", highest_average)
        print("-----------------------------")

    def search_student(self):
        search_name = input("Enter student name to search: ")

        if not search_name.strip():
            print("Student name cannot be empty.")
            return

        found = False

        for student in self.students:
            if student.name.lower() == search_name.lower():
                found = True
                print("Student found")
                print("Name:", student.name)
                print("Marks:", student.marks)
                print("Average:", student.calculate_average())
                break

        if not found:
            print("Student not found.")

    def update_student_marks(self):
        update_name = input("Enter student name to update marks: ")

        if not update_name.strip():
            print("Student name cannot be empty.")
            return

        found = False

        for student in self.students:
            if student.name.lower() == update_name.lower():
                found = True

                print("Current details")
                print("Name:", student.name)
                print("Marks:", student.marks)

                try:
                    m1 = int(input("Enter mark 1: "))
                    m2 = int(input("Enter mark 2: "))
                    m3 = int(input("Enter mark 3: "))
                except ValueError:
                    print("Please enter only numbers for marks.")
                    return

                if m1 < 0 or m1 > 100 or m2 < 0 or m2 > 100 or m3 < 0 or m3 > 100:
                    print("Marks must be between 0 and 100.")
                    return

                student.marks = [m1, m2, m3]
                self.save_data()

                print("Updated details")
                print("Name:", student.name)
                print("Marks:", student.marks)
                print("Average:", student.calculate_average())
                break

        if not found:
            print("Student not found.")

    def delete_student(self):
        delete_name = input("Enter student name to delete: ")

        if not delete_name.strip():
            print("Student name cannot be empty.")
            return

        found = False

        for student in self.students:
            if student.name.lower() == delete_name.lower():
                found = True

                print("Deleting student")
                print("Name:", student.name)
                print("Marks:", student.marks)

                self.students.remove(student)
                self.save_data()
                print("Student deleted successfully.")
                break

        if not found:
            print("Student not found.")