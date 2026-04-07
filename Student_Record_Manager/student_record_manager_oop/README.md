# Student Record Manager - OOP Version

A beginner-friendly Python project built using Object-Oriented Programming (OOP).

## What this project does

This project helps manage student records from the terminal.

You can:
- add a student
- view all students
- search for a student

This version is built using Python classes.

## Concepts used

This project practices:
- classes
- objects
- `__init__`
- instance variables
- methods
- lists of objects
- basic exception handling

## Files in this project

- `main.py` → menu and program execution
- `models.py` → class definitions for `Student` and `StudentManager`

## Class structure

### `Student`
Represents one student.

Stores:
- name
- marks

Methods:
- `calculate_average()`

### `StudentManager`
Manages all students.

Methods:
- `add_student()`
- `view_students()`
- `search_student()`

## How to run

1. Open the project folder in terminal
2. Run:

```bash
python main.py