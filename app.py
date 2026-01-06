class User():
    def __init__(self, name):
        self.name = name
    def __str__(self):
        status = "Logged in" if getattr(self, "logged_in", False) else "Logged out"
        return f"Hello {self.name} Status {status}"

    def log_in(self):
        self.logged_in =  True

class Student(User):
    def __init__(self,name,grade):
        super().__init__(name)

        print("Student.log_in() called.")
        self.name = name
        self.grade = grade
    def __str__(self):
        return f"Student {self.name}, {self.grade}"

student_1 = Student("Grace", "A")
print(student_1)



