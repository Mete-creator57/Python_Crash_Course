
# user input
prompt = 'Type something'
prompt += ' and I will display it back: '
msg = input(prompt)
print(msg)

# using int() to accept numerical input
age = input('Enter your age: ')
age = int(age)

if age >= 18 and age % 2 == 0:
    print(f'You are {age} years old! Also, your age is an even number!')
else:
    print("You aren't old enough!")


while msg != 'quit':
    prompt = 'Type something'
    prompt += ' and I will display it back: '
    msg = input(prompt)
    if msg != 'quit':
         print(msg)

# using a flag
# using a break statement
is_active = True
while is_active:
    print("Enter 'q' so as to quit")
    msg = input('Type something: ')
    if msg == 'q':
        is_active = False
    elif msg == 'fu':
        print('It is an insult! Quiting the programm...')
        break
    if msg != 'q':
        print(f'Your input: {msg}')

# using continue in a loop
error = 'ERROR!'
is_online = True
user_info = {

}
while is_online:
    first_name = input('Enter your name: ')
    first_name.strip()

    if not first_name or first_name.isdigit():
         print(error)
         continue
        
    user_info['first name'] = first_name

    while True:
        print("Note: If you don't have one press 'n' key")
        middle_name = input('Enter your middle name: ').strip()

        if middle_name == 'n':
            print("Moving to the next step...")
            break

        elif middle_name == '' or middle_name.isdigit():
            print(error)
            continue
        
        else:
           user_info['middle_name'] = middle_name
           break
    
    while True:
        last_name = input('Enter your last name: ').strip()

        if last_name == '' or last_name.isdigit():
          print(error)
          continue

        else:
            user_info['last name'] = last_name
            break
    is_online = False


print('Info about user:')
for key, value in user_info.items():
    print(f"{key.title()}: {value.title()}")


    

# Putting a dict in a dict (nesting) 
persons = {
    
}

persons['mete'] = {
    'age': 25,
    'city': 'New York'
}

# accessing dict in a dict
persons['mete']['city'] = 'amsterdam'
print(persons['mete']['city'])

city = persons['mete'].get('city')
print(f'This is: {city}')

# Updating / adding key-value pairs
a = {'name': 'Clark'}
b = {'age': 25, 'job': 'doctor'}

print(a)
print(b)
a.update(b)
print(f'Updated version: {a}')

# Creating a new concatenated dict (merging 2 dict into a new one)
new_dict = {**a, **b} # or new_dict = a | b
print(new_dict)


