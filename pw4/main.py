import numpy as np
import input as in_mod
import output as out_mod


class StudentMarkManagement:
    """Manager class coordinating data and logic."""

    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}

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
            out_mod.clear_screen()
            print("Exiting program. Goodbye!")
            break


if __name__ == "__main__":
    main()