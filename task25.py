from pprint import pprint

def group_by_age(people: list[dict[str, int | str]]) -> dict[int, list[str]]:
    group = {}

    for i in people:
        for name, age in i.items():
            if int(age) not in group.keys():
                group[int(age)] = []
            
            group[int(age)].append(name)

    return group

people = [
    {
        'ali': 13,
        'vali': 14,
        'sami': 13,
        'laziz': '14',
        'umid': 15,
        'said': '15',
        'bobur': 17,
        'yusuf': '16'
    }
]

pprint(group_by_age(people=people))