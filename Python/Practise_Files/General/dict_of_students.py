class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def print_students(self):
        for student in self.students:
            print(student)

# Example usage
if __name__ == "__main__":
    classroom = Classroom()
    classroom.add_student(Student("Alice", 14, "8th"))
    classroom.add_student(Student("Bob", 15, "9th"))
    classroom.add_student(Student("Charlie", 13, "7th"))

    classroom.print_students()