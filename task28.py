def group_by_length(words: list[str]) -> dict[int, list[str]]:
    group = {}
    
    for i in words:
        length = len(i)
        if length not in group:
            group[length] = []
        group[length].append(i)
    
    return group

words = ["Ali", "Vali", "Sara", "Sami", "Olim", "Bobur", "Zarina"]
grouped = group_by_length(words)
print(grouped)