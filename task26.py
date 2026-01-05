def merge_dicts(a: dict, b: dict) -> dict:
    ab = a

    ab.update(b)

    return ab

a = {
    'name':'ali',
    'age':15,
    'grade':'A'
}
b = {
    'name':'vali',
    'age':16
}

print(merge_dicts(a, b))