permissions = {"read": True, "write": False, "delete": True}

result = {}

for i, j in permissions.items():
    if j == True:
        result[i] = j

print(result)