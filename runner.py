from classes.school import School 

school = School('Ridgemont High') 

while True:
    mode = input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")

    if mode == '1':
        school.list_students()
    elif mode == '2':
        student_id = input('Enter student id:')
        student_string = str(school.find_student_by_id(student_id))
        print(student_string)
    elif mode == '3':
        student_data = {'role' : 'student'}
        student_data['name'] = input('Enter student name: ')
        student_data['age'] = input('Enter student age: ')
        student_data['school_id'] = input('Enter school id: ')
        student_data['password'] = input('Enter student password: ')
        school.add_student(student_data)
    elif mode == '4':
        student_id = input('Enter student id:')
        school.delete_student(student_id)
        print(f'Student id: {student_id} has been removed.')
    elif mode == '5':
        break
