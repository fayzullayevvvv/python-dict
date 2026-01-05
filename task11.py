config = {}

for i in range(3):
    setting_key = input(f"Setting name {i + 1}: ")
    setting_value = input(f"Setting value {i + 1}: ")
    config[setting_key] = setting_value

print(config)