
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


