
# People (6-7)
# initializing an empty list where we'll store our dicts in
people = [] 

mete = {
    'eye color' : 'brown',
    'height': 165,
    'weight': 48,
    'iq': 110,
    'first name': 'mete',
    'last name': 'tunkiz',
    'middle name': 'batir',
}
jennet = dict(mete)
jennet['eye color'] = 'green'
jennet['height'] = 163
jennet['first name'] = 'jennet'
jennet['last name'] = 'bayryyeva'
jennet.pop('middle name')
jennet['weight'] = 52

people.append(jennet)
people.append(mete)

for person in people[:]:
    for key, value in person.items():
        # checking whether value is int or not
        if isinstance(value, int):
            print(f"{key.title()}: {value}")
        else:
            print(f"{key.title()}: {value.title()}")
        
# Pets (6-8)
# initializing an empty list
pets = []

pet_0 = {
    'kind': 'dog',
    'owner': 'mete'
}

pet_1 = {
    'kind': 'cat',
    'owner': 'james'
}

pet_2 = {
    'kind': 'rat',
    'owner': 'clark'
}

pets.append(pet_0)
pets.append(pet_1)
pets.append(pet_2)

for pet in pets:
    for k,v in pet.items():
        print(k.title() + ':', v.title())

# Favorite Places (6-9)
fav_places = {
    'mete': ['home','starbucks'],
    'jennet': ['Thailand','Vietnam','Cafe Nero'],
    'james': ['cafe','burger king','kfc'],
}
for i, (name, places) in enumerate( fav_places.items()):
    print(f'\nIndex: {i}, Name: {name.title()}')
    for place in places:
        print(f"\t{place.title()}")

# Favorite Numbers (6-10)
fav_numbers = {
    'Jake': [3,10,2929],
    'Clark': [5,5774,4232],
    'Jane': [100,12919],
}
print('1st method:')
for name in fav_numbers:
    print(f"{name}'s favorite numbers are: {fav_numbers[name]}")

print('2nd method')
for name in fav_numbers.keys():
    print(f"\n{name}'s favorite numbers are: ")
    # e.g. for 3 in fav_numbers['Jake']
    #      for 10 in ....
    #      for 2929 in...
    for number in fav_numbers[name]:
        print(number)

# Cities (6-11)
cities = {
    'istanbul': {
         'country': 'Turkey',
       'population': '14 million',
       'fact': 'was renamed in 1453',
    },

      'new york': {
        'country': 'the USA',
        'population': '20 million',
        'fact': 'was originally named new Amsterdam'
      },
}
# 1st way
print('1st way')
for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    for key, value in city_info.items():
        if key == 'fact':
            print(f"{key.title()}: It {value.title()}")
        else:
            print(f"{key.title()}: {value.title()}")

# 2nd Way
print('\n2nd way')
for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    country = city_info['country']
    population = city_info['population']
    fact = f"It {city_info['fact']}"

    print(f'Country: {country.title()}')
    print(f'Population: {population.title()}')
    print(f'Fact: {fact.title()}')

# Extensions (6-12)

pc_specs = {
    'type': 'gaming',
    'ram': 32,
    'ssd': 1000,
    'gpu': 'RTX 3070 TI',
    'controllers': ['dual sense','Xbox gamepad'],
    'cpu' : 'amd ryzen 7900X3D',
}
for component, value in pc_specs.items():
    if component == 'controllers':
        print('\tControllers are: ')
        for controller in pc_specs['controllers']:
            print(f'\t{controller.title()}')

    elif isinstance(value, int) and component == 'ram':
        print(f'Component: {component.upper()} --> {value}GB ')

    elif component == 'ssd' and isinstance(value, int):
        print(f'Component: {component.upper()} --> {value}GB (tb)')

    else:
        print(f"Component: {component.upper()} --> {value}")

# More Practice
lessons = {
    'math': {
        'difficulty': 'extreme hard',
        'simplicity': 'low',
        'easy to learn': 'no',
        'mandatory things': ['pen','pencil','cell notebook','ruler']
    },

    'english': {
        'difficulty': 'medium',
        'simplicity': 'medium',
        'easy to learn': 'no',
        'mandatory things': ['pen','pencil','notebook']
    },
    
    'physics': {
        'difficulty': 'extreme hard',
        'simplicity': 'low',
        'easy to learn': 'no',
        'mandatory things': ['pen','pencil','cell notebook','ruler','pencilcase']
 
    },
}

for i, (lesson, lesson_properties) in enumerate(lessons.items()) :
    i += 1
    print(f"\nNumber: {i}")
    print(f"Lesson: {lesson.capitalize()}")
    
    for key, thing in lesson_properties.items():
        if isinstance(thing, list):
            print(f"\t{key.title()}:")

            for value in thing:
                print(f"\t{value.title()}")
        else:
             print(key.title() + ':' + " " + thing.title())
       



    