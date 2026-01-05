inventory = {
    'apple':3,
    'banana':1
}

product = input('Product: ')

if product not in inventory:
    inventory[product] = 0

print(inventory)