
from typing import Optional, List, Dict

# can be either str or None
# specifing that name argument 
# might store a reference to either a string value or None
def greet_users(name: Optional[str], friends: Optional[List[str]]):
    """Greeting users"""
    # Always check for None
    print()
    if name is None:
        print('Hi, stranger!')
    else:
        print(f'Hello, {name.upper()}')

    print("It's time to greet your friends!")
    if friends is None:
        print('It seems you have no friends...')
        return
    
    for friend in friends:
        print(f"Hello, {friend.upper()}")

friends = ['Clark', 'Mary', 'Frank']

# function calls
greet_users('Mete', friends)
greet_users(None, None)


def dict_loop(**data: int):
    if not data: # if data dict wasn't provided any key-value pairs
        print("No data provided") 
        return # return nothing as the main purpose of a method is to print
               # all key-value pairs (in this case, just exit the method itself)
    
    # otherwise, looping through dict's all key-value pairs
    for k, v in data.items():
        print(f"{k.title()}: {v} dollars")

# no need to put ** in front of arguments if a dict doesn't exist yet
dict_loop(apple=56, orange=35)

# putting ** in front of an existing dict. in this case, ** symbols
# are necessary according to Python syntax rules 
my_fruits = {'orange': 50, 'lemon': 20}
dict_loop(**my_fruits)
