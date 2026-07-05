
# Returning a Simple Value

def get_formatted_name(first, last):
    """ Returning a full name """
    full_name = f'{first.title()} {last.title()}'
    return full_name

president = get_formatted_name('donald','trump')
print(president)


# Making an Argument Optional
# making parameter middle empty --> ''
def get_formatted_person(first, last, middle=''):
    """ Returning a full name """
    # if a string is not empty
    if middle:
        full_name = f'{first.title()} {middle.title()} {last.title()}'
    else:
        full_name = f'{first.title()} {last.title()}'

    return full_name

me = get_formatted_person(last='tunkiz',first='mete',middle='batir')
print(me)

# Returning a dictionary
def person(first_name,last_name,middle_name=''):
    person = {
        'first name': first_name.title(),
        'last name': last_name.title(),
    }
    if middle_name:
        person['middle name'] = middle_name.title()
    
    return person

maria = person(last_name='clark',first_name='maria',middle_name='batir')
print(maria)

for key, value in maria.items():
    print(f'{key.title()}: {value.title()}')