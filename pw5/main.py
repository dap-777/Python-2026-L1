import os
import zipfile
import numpy as np
import input as in_mod
import output as out_mod
from domains.student import Student
from domains.course import Course


class StudentMarkManagement:
    """Manager class handling data persistence and business logic."""

    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}
        self.load_data()

    def load_data(self):
        """Check if students.dat exists, extract files, and load data."""
        dat_file = "students.dat"
        if os.path.exists(dat_file):
            print(f"Found '{dat_file}'. Extracting files...")
            try:
                with zipfile.ZipFile(dat_file, 'r') as zip_ref:
                    zip_ref.extractall()
            except Exception as e:
                print(f"Error decompressing {dat_file}: {e}")

        # Load Students
        if os.path.exists("students.txt"):
            with open("students.txt", "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split("|")
                    if len(parts) >= 3:
                        s = Student(parts[0], parts[1], parts[2])
                        if len(parts) >= 4:
                            try:
                                s.set_gpa(float(parts[3]))
                            except ValueError:
                                pass
                        self.__students.append(s)

        # Load Courses
        if os.path.exists("courses.txt"):
            with open("courses.txt", "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split("|")
                    if len(parts) >= 3:
                        try:
                            c = Course(parts[0], parts[1], int(parts[2]))
                            self.__courses.append(c)
                        except ValueError:
                            pass

        # Load Marks
        if os.path.exists("marks.txt"):
            with open("marks.txt", "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split("|")
                    if len(parts) >= 3:
                        cid, sid, mark_str = parts[0], parts[1], parts[2]
                        try:
                            mark = float(mark_str)
                            if cid not in self.__marks:
                                self.__marks[cid] = {}
                            self.__marks[cid][sid] = mark
                        except ValueError:
                            pass

    def save_and_compress(self):
        """Compress text files into students.dat using ZIP compression."""
        in_mod.write_students_to_file(self.__students)
        in_mod.write_courses_to_file(self.__courses)
        in_mod.write_marks_to_file(self.__marks)

        files_to_compress = ["students.txt", "courses.txt", "marks.txt"]
        print("\nCompressing files into 'students.dat'...")
        with zipfile.ZipFile("students.dat", "w", zipfile.ZIP_DEFLATED) as zip_ref:
            for file_name in files_to_compress:
                if os.path.exists(file_name):
                    zip_ref.write(file_name)
                else:
                    open(file_name, "w").close()
                    zip_ref.write(file_name)
        print("Data saved and compressed to 'students.dat'!")

    def input_students(self):
        out_mod.clear_screen()
        print("=== INPUT STUDENTS ===")
        in_mod.input_students(self.__students)

    def input_courses(self):
        out_mod.clear_screen()
        print("=== INPUT COURSES ===")
        in_mod.input_courses(self.__courses)

    def input_marks(self):
        out_mod.clear_screen()
        print("=== INPUT MARKS ===")
        in_mod.input_marks(self.__students, self.__courses, self.__marks)

    def calculate_gpas(self):
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
        out_mod.clear_screen()
        print("=== CALCULATE & SORT GPAS ===")
        if not self.__students:
            print("No students found.")
            input("\nPress Enter to continue...")
            return

        self.calculate_gpas()

        gpas = np.array([s.get_gpa() for s in self.__students])
        sorted_indices = np.argsort(-gpas)
        self.__students = [self.__students[i] for i in sorted_indices]
        in_mod.write_students_to_file(self.__students)

        print("GPAs calculated and students sorted successfully!")
        input("\nPress Enter to continue...")

    def list_courses(self):
        out_mod.list_courses(self.__courses)

    def list_students(self):
        out_mod.list_students(self.__students)

    def show_marks(self):
        out_mod.show_marks(self.__students, self.__marks)


def main():
    system = StudentMarkManagement()

    while True:
        out_mod.display_menu()
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
            system.save_and_compress()
            print("Exiting program. Goodbye!")
            break


if __name__ == "__main__":
    main()