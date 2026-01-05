def most_common_char(text: str) -> str:
    text = text.lower()
    most_char = text[0]

    for i in text:
        if text.count(i) > text.count(most_char):
            most_char = i
        
    return most_char

text = 'Ali Valiyev'
print(most_common_char(text=text))