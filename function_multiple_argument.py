

# Arbitrary number of arguments
def students(*students_name):
    print(students_name, type(students_name))
    for student in students_name:
        print(student)

students('Kamal', 'Dhamal', 'Bill', "Gate")
students()
students('Jack')

# Arbitrary number of arguments
def captain_and_students(captain, *other_students):
    print('Captain', captain)
    print('Others', other_students)
    for student in other_students:
        print(student)

captain_and_students('Kamal', 'Dhamal', 'Bill', "Gate")
captain_and_students('Jack')

# Arbitrary number of arguments with key and dictionary
def student_captain(captain, **other_students):
    print('Captain', captain)
    print('Others', other_students)
    for key, value in other_students.items():
        print(key, value, sep='->')

student_captain(captain='Kamal', second_captain='Dhamal', third_captain='Bill', forth_captain="Gate")
student_captain('Jack')