# Polymorphism (overriding __dunders__)
from typing import Optional, Any


class Player:
    def __init__(self, username: str, online: bool, play_hours: int, register_date: str,
    birth_date: Optional[str], friends: Optional[list[str]] = None) -> None:
        self.username = username
        self.online = online
        self.play_hours = play_hours
        self.register_date = register_date
        self.birth_date = birth_date
        self.friends = friends or []

    # polymorphism (will work only with print() func) 
    def __str__(self) -> str:
        greeting = f'Hello, {self.username.title()}'
        return greeting

 
    # useful while debugging
    def __repr__(self) -> str:
        return (f"Player(username='{self.username}', online={self.online}, "
                f"play_hours={self.play_hours}, register_date='{self.register_date}')")

    def __len__(self) -> int:
        return len(self.friends)


    def describe_user(self) -> None:
        print(f'Hello, {self.username.title()}!')
        if self.online is True:
           print(f'Current state: ONLINE') 
        else:
            print(f'Current state: OFFLINE')
        
        if isinstance (self.play_hours, int):
            pass
        else:
            print('The value of total play hours must be entered in a numerical value')
            return

        print(f'Total Hours of Play: {self.play_hours} hours')
        if self.birth_date:
            print(f'Birth Date: {self.birth_date}')
        else:
            print('Birth Day was not provided')


        print(F'Registered date DD/MM/YY : {self.register_date.upper()}')
        
    
player = Player(username='Mete', online=True, play_hours=20, 
register_date='09/12/2021', birth_date='09/12/2010')


print(f'Length of a friends list: {len(player)}')

#  analog of print(player.__str__(self))
print(player)
print(player.__str__())
player.describe_user()

# creating an own dunder method (__method__) for practice
class Object:
    # can't leave an empty __init__method
    def __init__(self):
        pass

# creating our own dunder method  
# !bad practice
    def __printing__(self, msg: Any) -> Any: 
        print(msg)
    
    def __str__(self):
        cube = 'I am a cube!'
        return cube

obj = Object()
obj.__printing__('hello')
# difference
print(obj)

# prints what the method returns
print(repr(obj.__printing__('goal')))

# polymorhism
"""Represents BMW cars class """
class BMW:
    def display_wheel_drive(self) -> str:
        """Returns a formated string"""
        return '---- BMW ----  \
  \n-> FWD - Forward wheel drive'


"""Represents Mercedes cars class """
class Mercedes:
    def display_wheel_drive(self) -> str:
        """Returns a formatted string"""
        return '---- Mercedes ---- \
        \n-> AWD - All wheel drive'

merc = Mercedes()
bmw = BMW()

def display_drive(car_obj: object) -> None:
    """Displaying each object's wheel drive type"""
    print(car_obj.display_wheel_drive())

# providing objects as arguments
display_drive(merc)
display_drive(bmw)

