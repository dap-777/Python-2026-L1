import os


def clear_screen():
    """Clear terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def list_courses(courses):
    """Display list of courses."""
    clear_screen()
    print("=== COURSE LIST ===")
    if not courses:
        print("No courses available.")
    else:
        for course in courses:
            print(course.list())
    input("\nPress Enter to continue...")


def list_students(students):
    """Display list of students."""
    clear_screen()
    print("=== STUDENT LIST (Sorted by GPA Descending) ===")
    if not students:
        print("No students available.")
    else:
        for student in students:
            print(student.list())
    input("\nPress Enter to continue...")


def show_marks(students, marks):
    """Display marks for a selected course."""
    clear_screen()
    print("=== SHOW MARKS FOR COURSE ===")
    cid = input("Enter Course ID: ").strip()

    if cid not in marks or not marks[cid]:
        print(f"No marks recorded for course '{cid}'.")
    else:
        print(f"\n--- Marks for Course {cid} ---")
        for sid, mark in marks[cid].items():
            sname = next(
                (s.get_name() for s in students if s.get_id() == sid),
                sid,
            )
            print(
                f"Student: {sname:<20} (ID: {sid:<10}) | Mark: {mark:.1f}"
            )

    input("\nPress Enter to continue...")


def display_menu():
    """Display main user interface menu."""
    clear_screen()
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