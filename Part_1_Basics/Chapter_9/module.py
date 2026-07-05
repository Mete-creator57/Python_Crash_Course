# old method of using typing module (3.8 or older)
# NOTE: starting from the latest version of Python, Collections(Dict, List...)
# have been moved to built-in types (list, dict...)
from typing import Optional, List, Dict, Union, Any

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


# NOTE: Annotation for **kwargs indicates a type of values in arguments
# in this case, in dict values are specified as int values. 
# if any other value type than int is provided, py. raises an error
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

# Optional = int / None (default value = 0)
# NOTE: int | None -> Optional[int]. The modern way of writing this
# in this case, int | None is more intuitive since we know 
# that 2 diff values can be equal to budget. 
# == 0 is a default value of budget, if not argument is given on a function call
# -> None indicates that method returns None (nothing)
def upgrade_pc(components: list[str], budget: int | None = 0) -> None:
    """Upgrading user's pc"""
    if budget is None or budget == 0:
        print("You don't have money to upgrade...")
        return
    
    print('Your current specs: ')
    for component in components:
        print(component.title())

    print(f'Your budget ready to be spent for an upgrade: {budget} USD')
    if budget <= 100:
        print('You can upgrade' \
        ' your pc case or buy used a GPU in that range...')
        components.append('gpu_1050_ti')
    elif budget > 100 and budget < 200:
        print('You can buy a used CPU in that range or buy 8 GB of DDR4 RAM')
    elif budget == 0 or budget < 0:
        print('You are broke...')
        return

components = ['rx 750', 'intel pentium', 'ddr3 4 GB RAM']
upgrade_pc(components, 100)
upgrade_pc(components, None)
upgrade_pc(components)
    

# NOTE: Optional[value type] is the same as Union [value type, None]
# using Union here to accept both str and int value as argument
def get_user_data(user_id: Union[str, int], random_value: Any):
    """Getting user's id"""
    if isinstance(user_id, int):
        user_id = int(user_id)

    print(f'Searching for a user with ID: {user_id}...')
    print(random_value)

get_user_data('213213238', True)

