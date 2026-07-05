
# Person (6-1)
person = {
    'first_name': 'Mete',
    'middle_name': 'Batir',
    'last_name': 'Tunkiz',
    'city': 'Istanbul'
}

first_name = person.get('first_name','No value assigned')
middle_name = person.get('middle_name','No value assigned')
last_name = person['last_name']
city = person['city']

# Storing items in a list
info = [first_name, middle_name, last_name, city]
print(info)

# i = represents index in a list
for i, piece_of_info in enumerate(info):
    print(f'Index: {i}, {piece_of_info}')

# Favorite Numbers (6-2)
fav_numbers = {
    'Jake': 3,
    'Clark': 5,
    'Jane': 100,
}

print(f"Jake's favorite number: {fav_numbers['Jake']}")
print(f"Clark's favorite number: {fav_numbers['Clark']}")
print(f"Jane's favorite number: {fav_numbers['Jane']}")

# Glossary (6-3)
tech_words = {'list': 'A container for multiple items',
    'variable':'changable container of info',
    'function':'a thing that allows you to modify and interact with data',
}

print(tech_words['function'])
print(tech_words['variable'])
print(tech_words['list'])

