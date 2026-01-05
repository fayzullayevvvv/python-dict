def count_letters(text: str) -> dict[str, int]:
    group = {}
    
    for i in text:
        if i not in group:
            group[i] = 1
        else:
            group[i] += 1

    return group

text = 'assalomu alaykum'
print(count_letters(text))