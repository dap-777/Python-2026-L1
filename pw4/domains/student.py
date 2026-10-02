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