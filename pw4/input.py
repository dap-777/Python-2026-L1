import math
from domains.student import Student
from domains.course import Course

def input_students(students):
    """Input student details and append to students list."""
    try:
        n = int(input("Number of students: "))
    except ValueError:
        print("Invalid number.")
        input("\nPress Enter to continue...")
        return

    for i in range(n):
        print(f"\n--- Student {i + 1}/{n} ---")
        sid = input("Student ID: ").strip()
        sname = input("Student Name: ").strip()
        sdob = input("DOB: ").strip()
        students.append(Student(sid, sname, sdob))

    input("\nStudents added successfully! Press Enter to continue...")


def input_courses(courses):
    """Input course details and append to courses list."""
    try:
        n = int(input("Number of courses: "))
    except ValueError:
        print("Invalid number.")
        input("\nPress Enter to continue...")
        return

    for i in range(n):
        print(f"\n--- Course {i + 1}/{n} ---")
        cid = input("Course ID: ").strip()
        cname = input("Course Name: ").strip()
        try:
            credits = int(input("Credits: "))
        except ValueError:
            credits = 0
        courses.append(Course(cid, cname, credits))

    input("\nCourses added successfully! Press Enter to continue...")


def input_marks(students, courses, marks):
    """Input marks for a selected course."""
    if not courses or not students:
        print("Please input students and courses first.")
        input("\nPress Enter to continue...")
        return

    cid = input("Select Course ID: ").strip()
    course_exists = any(c.get_id() == cid for c in courses)
    if not course_exists:
        print("Invalid Course ID.")
        input("\nPress Enter to continue...")
        return

    if cid not in marks:
        marks[cid] = {}

    for student in students:
        try:
            raw_mark = float(
                input(
                    f"Mark for {student.get_name()} ({student.get_id()}): "
                )
            )
            mark = math.floor(raw_mark * 10) / 10.0
        except ValueError:
            mark = 0.0

        marks[cid][student.get_id()] = mark

    input("\nMarks recorded successfully! Press Enter to continue...")