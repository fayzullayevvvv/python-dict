def get_value(dict: dict):
    key = input('Key: ')

    return dict.get(key, 'Topilmadi')

student = {
        'name': 'ali',
        'age': 13,
        'email': 'ali@gmail.com',
        'phone': '+998991231299'
    }

print(get_value(student))