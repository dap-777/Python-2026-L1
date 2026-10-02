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