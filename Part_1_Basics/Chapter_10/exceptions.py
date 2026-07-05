# using Try - Except Blocks + else
msg = 'Enter your age: '
age = input(msg)
try:
    age = int(age)
except ValueError as ve:
    print(f"The error: '{ve}' has been occured")
    print('Enter your age as an integer value...')

# execute only if try block succeeds
else:
    print(f'You are {age} years old!')

# execute anyway independent of above code blocks
finally:
    print(f"{age} is either an int or a str value")
    print(age)
