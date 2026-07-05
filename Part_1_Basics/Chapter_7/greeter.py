
# Defining a function
def greeting():
    print('Hello user!')

greeting()

# Passing info to a Function
name = input('Enter your name: ')

def user_name(name):
    print('Hello ' + name.title())

user_name(name)

# Passing Arguments (positional)

def describe_person(first, last):
    
    full_name = f'{first.title()} {last.title()}'
    print(full_name)

# multiple function calls
describe_person('mete','tunkiz')
describe_person('clark','johnson')


# Keyword Arguments
# order doesn't matter
describe_person(first='mete',last='tunkiz')
describe_person(last='johnson',first='clark')

# Default Values (if no value is provided)
def describe_dog(first, last, nickname='honey'):
    
    
         full_name = f'{first.title()} {last.title()}, {nickname.title()}'
         print(full_name)

       
 
describe_dog(last='miller',first='willie',)

