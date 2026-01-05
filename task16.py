student = {
    'name':'ali',
    'age':16,
    'grade':5
}

key = input('Key: ')

if key in student.keys():
    del student[key]
    print(student)
else:
    print('Bunday kalit yo\'q!')
