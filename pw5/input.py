import math
from domains.student import Student
from domains.course import Course


def write_students_to_file(students, filename="students.txt"):
    """Write student information to students.txt."""
    with open(filename, "w", encoding="utf-8") as f:
        for s in students:
            f.write(f"{s.get_id()}|{s.get_name()}|{s.get_dob()}|{s.get_gpa()}\n")


def write_courses_to_file(courses, filename="courses.txt"):
    """Write course information to courses.txt."""
    with open(filename, "w", encoding="utf-8") as f:
        for c in courses:
            f.write(f"{c.get_id()}|{c.get_name()}|{c.get_credits()}\n")


def write_marks_to_file(marks, filename="marks.txt"):
    """Write marks information to marks.txt."""
    with open(filename, "w", encoding="utf-8") as f:
        for cid, mark_map in marks.items():
            for sid, mark in mark_map.items():
                f.write(f"{cid}|{sid}|{mark}\n")


def input_students(students):
    """Input student details, append to list, and save to students.txt."""
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

    write_students_to_file(students)
    input("\nStudents added and saved to students.txt! Press Enter to continue...")


def input_courses(courses):
    """Input course details, append to list, and save to courses.txt."""
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

    write_courses_to_file(courses)
    input("\nCourses added and saved to courses.txt! Press Enter to continue...")


def input_marks(students, courses, marks):
    """Input marks for a course and save to marks.txt."""
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

    write_marks_to_file(marks)
    input("\nMarks recorded and saved to marks.txt! Press Enter to continue...")