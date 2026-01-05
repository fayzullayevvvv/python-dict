def group_students(students: list[dict[str, str]]) -> dict[str, list[str]]:
    group = {}

    for student in students:
        group_name = student['group']
        if group_name not in group:
            group[group_name] = []
        
        group[group_name].append(student['name'])

    return group


students = [
    {
        'name':'ali',
        'group':'A'
    },
    {
        'name':'vali',
        'group':'B'
    },
    {
        'name':'sami',
        'group':'C'
    },
    {
        'name':'gani',
        'group':'A'
    },
    {
        'name':'jon',
        'group':'B'
    }
]

print(group_students(students))