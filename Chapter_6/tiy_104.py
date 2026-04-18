
# Glossary 2 (6-4)
# copied 
tech_words = {'list': 'A container for multiple items',
    'variable':'changable container of info',
    'function':'a thing that allows you to modify and interact with data',
    'key': 'a variable that value is assigned to',
    '.gitignore': "a special file created to tell Git not to track specific files"
}

# here i = represents index (step number)
for i, (term, meaning) in enumerate(tech_words.items()):
    print(f"\nIndex: {i}, Term: '{term}', Meaning: {meaning}")

# Rivers (6-5)
rivers = {
    'nile' : 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
    'Mississippi': 'the usa'
}
for river, country in rivers.items():
    print(f"{river.title()} runs through {country.title()}")

# Polling (6-6)

people_taken = ['jack','Mete','Clark','James']
people = ['Maria','Alex','Jenny','Flerk','Mete','Clark','James','jack']

for person in people:
    if person in people_taken:
        print(f'You have already taken the poll {person.title()}. Thank You')
    else:
        print(f"{person.title()}, you're invited!")

