class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade


class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.student_id] = student

    def get_student(self, student_id):
        return self.students.get(student_id)

    def display_students(self):
        for student in self.students.values():
            print(student.student_id, student.name, student.grade)


# Example usage
manager = StudentManager()
s1 = Student(1, "Menna", "A")
s2 = Student(2, "Mohmmed", "B")

manager.add_student(s1)
manager.add_student(s2)

manager.display_students()