import math
from IPython.display import clear_output
import numpy as np


class Student:

    """Class representing a student with private attributes and polymorphic methods."""

    def __init__(self, student_id="", name="", dob=""):
        self.__id = student_id
        self.__name = name
        self.__dob = dob
        self.__gpa = 0.0

    def get_id(self):
        return self.__id

    def set_id(self, student_id):
        self.__id = student_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_dob(self):
        return self.__dob

    def set_dob(self, dob):
        self.__dob = dob

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, gpa):
        self.__gpa = gpa

    def list(self):
        return f"ID: {self.__id:<10} | Name: {self.__name:<20} | DoB: {self.__dob:<12} | GPA: {self.__gpa:.2f}"


class Course:

    """Class representing a course with private attributes and polymorphic methods."""

    def __init__(self, course_id="", name="", credits=0):
        self.__id = course_id
        self.__name = name
        self.__credits = credits

    def get_id(self):
        return self.__id

    def set_id(self, course_id):
        self.__id = course_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_credits(self):
        return self.__credits

    def set_credits(self, credits):
        self.__credits = credits

    def list(self):
        return f"ID: {self.__id:<10} | Course Name: {self.__name:<25} | Credits: {self.__credits}"


class StudentMarkManagement:

    """Manager class handling student records, courses, marks, and GPA logic."""

    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}

    def input_students(self):
        clear_output(wait=True)
        print("=== INPUT STUDENTS ===")
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
            self.__students.append(Student(sid, sname, sdob))

        input("\nStudents added successfully! Press Enter to continue...")

    def input_courses(self):
        clear_output(wait=True)
        print("=== INPUT COURSES ===")
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
            self.__courses.append(Course(cid, cname, credits))

        input("\nCourses added successfully! Press Enter to continue...")

    def input_marks(self):
        clear_output(wait=True)
        print("=== INPUT MARKS ===")
        if not self.__courses or not self.__students:
            print("Please input students and courses first.")
            input("\nPress Enter to continue...")
            return

        cid = input("Select Course ID: ").strip()
        course_exists = any(c.get_id() == cid for c in self.__courses)
        if not course_exists:
            print("Invalid Course ID.")
            input("\nPress Enter to continue...")
            return

        if cid not in self.__marks:
            self.__marks[cid] = {}

        for student in self.__students:
            try:
                raw_mark = float(
                    input(
                        f"Mark for {student.get_name()} ({student.get_id()}): "
                    )
                )
                # Requirement: Use math.floor() to round down student scores to 1-digit decimal
                mark = math.floor(raw_mark * 10) / 10.0
            except ValueError:
                mark = 0.0

            self.__marks[cid][student.get_id()] = mark

        input("\nMarks recorded successfully! Press Enter to continue...")

    def calculate_gpas(self):
        """Calculate weighted average GPA using numpy arrays."""
        course_dict = {c.get_id(): c.get_credits() for c in self.__courses}

        for student in self.__students:
            sid = student.get_id()
            s_marks = []
            s_credits = []

            for cid, mark_map in self.__marks.items():
                if sid in mark_map and cid in course_dict:
                    s_marks.append(mark_map[sid])
                    s_credits.append(course_dict[cid])

            if s_credits and sum(s_credits) > 0:
                marks_arr = np.array(s_marks)
                credits_arr = np.array(s_credits)

                gpa = np.sum(marks_arr * credits_arr) / np.sum(credits_arr)
                student.set_gpa(gpa)
            else:
                student.set_gpa(0.0)

    def sort_students_by_gpa(self):
        """Sort students descending by GPA using numpy.argsort."""
        clear_output(wait=True)
        print("=== CALCULATE & SORT GPAS ===")
        if not self.__students:
            print("No students found.")
            input("\nPress Enter to continue...")
            return

        self.calculate_gpas()

        gpas = np.array([s.get_gpa() for s in self.__students])
        sorted_indices = np.argsort(-gpas)
        self.__students = [self.__students[i] for i in sorted_indices]

        print("GPAs calculated and students sorted successfully!")
        input("\nPress Enter to continue...")

    def list_courses(self):
        clear_output(wait=True)
        print("=== COURSE LIST ===")
        if not self.__courses:
            print("No courses available.")
        else:
            for course in self.__courses:
                print(course.list())
        input("\nPress Enter to continue...")

    def list_students(self):
        clear_output(wait=True)
        print("=== STUDENT LIST (Sorted by GPA Descending) ===")
        if not self.__students:
            print("No students available.")
        else:
            for student in self.__students:
                print(student.list())
        input("\nPress Enter to continue...")

    def show_marks(self):
        clear_output(wait=True)
        print("=== SHOW MARKS FOR COURSE ===")
        cid = input("Enter Course ID: ").strip()

        if cid not in self.__marks or not self.__marks[cid]:
            print(f"No marks recorded for course '{cid}'.")
        else:
            print(f"\n--- Marks for Course {cid} ---")
            for sid, mark in self.__marks[cid].items():
                sname = next(
                    (s.get_name() for s in self.__students if s.get_id() == sid),
                    sid,
                )
                print(
                    f"Student: {sname:<20} (ID: {sid:<10}) | Mark: {mark:.1f}"
                )

        input("\nPress Enter to continue...")


def main():
    system = StudentMarkManagement()

    while True:
        clear_output(wait=True)
        print("=======================================")
        print("   STUDENT MARK MANAGEMENT SYSTEM      ")
        print("=======================================")
        print("1. Input Students")
        print("2. Input Courses")
        print("3. Input Marks")
        print("4. Calculate & Sort Students by GPA")
        print("5. List Courses")
        print("6. List Students")
        print("7. Show Marks for a Course")
        print("8. Exit")
        print("=======================================")

        choice = input("Select an option (1-8): ").strip()

        if choice == "1":
            system.input_students()
        elif choice == "2":
            system.input_courses()
        elif choice == "3":
            system.input_marks()
        elif choice == "4":
            system.sort_students_by_gpa()
        elif choice == "5":
            system.list_courses()
        elif choice == "6":
            system.list_students()
        elif choice == "7":
            system.show_marks()
        elif choice == "8":
            clear_output(wait=True)
            print("Exiting program. Goodbye!")
            break


if __name__ == "__main__":
    main()