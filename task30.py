def filter_non_zero(d: dict[str, int]) -> dict[str, int]:
    not_zero = {}

    for i, j in d.items():
        if j != 0:
            not_zero[i] = j

    return not_zero

d = {
    'ali':0,
    'vali':2,
    'sami':1
}
print(filter_non_zero(d))