import typing 
import textwrap
import shutil
size = shutil.get_terminal_size()
print(size.columns)
print(size.lines)

# Creating a class
class Cat:
    def __init__(self, sex, name, age): 
        """Initialize variables's attributes"""
        self.sex = sex
        self.name = name
        self.age = age

    def jump(self):
        """Simulate jumping"""
        print(f'{self.name.title()} is jumping!')
    
    def sound(self):
        """Simulate cat meowing"""
        print(f'{self.name.title()} is meowing!')

# creating an object (an isctance of the class)
catty = Cat('female','Elizabeth',15)
# accessing object's attributes
catty.jump()
catty.sound()

# creating multiple instances
special_cat = Cat(name='clark', sex='Male',age=2)
my_cat = Cat('Female', 'Jennifer', 14)

print(textwrap.fill(f"""{special_cat.name.title()} is {special_cat.age}
years old {special_cat.sex.lower()}""",width=size.columns))
special_cat.jump()
special_cat.sound()


text = f"""{my_cat.name.title()} is {my_cat.age}
years old {my_cat.sex.lower()}"""

print(f'\n{textwrap.fill(text,width=size.columns)}')

my_cat.jump()
my_cat.sound()



