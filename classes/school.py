from classes.staff import Staff
from classes.student import Student
import os
import csv

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()

    def list_students(self):
        print('\n')
        for i, student in enumerate(self.students):
            print(f'{i + 1}. {student.name} {student.school_id}')

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.school_id == student_id:
                return student

    def add_student(self, student_data):
        new_student = Student(**student_data)
        self.students.append(new_student)
        self.save_students()
    
    def save_students(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")
        with open(path, mode = 'w') as csv_file:
            fieldnames = ['name', 'age', 'role', 'school_id', 'password']
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(fieldnames)
            for student in self.students:
                csv_writer.writerow([student.name, student.age, student.role, student.school_id, student.password])

    def delete_student(self, student_id):
        for student in self.students:
            if student.school_id == student_id:
                self.students.remove(student)
        
        # Working on deleting student from CSV file
        # my_path = os.path.abspath(os.path.dirname(__file__))
        # path = os.path.join(my_path, "../data/students.csv")
        # path_two = os.path.join(my_path, "../data/students_edit.csv")
        # with open(path, mode = 'r') as inp,open(path_two, mode = 'w') as out:
        #     csv_writer = csv.writer(out)
        #     reader = csv.reader(inp)
        #     for row in reader:
        #         if row[3] == student_id:
        #             csv_writer.writerow(row)
