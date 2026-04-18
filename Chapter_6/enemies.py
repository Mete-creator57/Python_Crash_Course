
# A list of Dicts
enemy_0 = {
    'color' : 'green',
    'power': 100,
    'points': 10,
}

enemy_1 = {
    'color' : 'green',
    'power': 100,
    'points': 10,
}

enemy_2 = {
    'color' : 'green',
    'power': 100,
    'points': 10,
}

enemies = [enemy_0, enemy_1, enemy_2]

for enemy in enemies:
    print(enemy)

del enemies

# initializing an empty list
enemies = []

for counter in range(31):
    enemy = {'color': 'red', 'name': 'duke', 'power': 100}
    enemies.append(enemy)

for enemy in enemies[:4]:
    if enemy['color'] == 'red':
        enemy['color'] = 'yellow'
    print(enemy)
print("...")

# a list in dicts
car = {
    'type' : 'hybrid',
    'max_speed' : 225,
    'drawbacks': ['not certified','no insurance','broken seat']
}

for category, value in car.items():
    if category == 'max_speed':
        print(f'{category.title()}: {value}')
    elif category == 'drawbacks':
        print('DRAWBACKS:')
        for drawback in car['drawbacks']:
            print(drawback)
    else:
        print(f'{category.title()}: {value.upper()}')


for feature in car['drawbacks']:
    print(f'\n{feature}')
