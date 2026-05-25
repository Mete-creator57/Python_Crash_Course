# Restaraunt (9-1)
class Restaraunt:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def decsribe_restaraunt(self):
        if len(self.name) > 10:
            print(f"The restaraunt name is: {self.name.upper()}")
        else:
             print(f"The restaraunt name is: {self.name.title()}")
       
        print(f"Cuisine Type: {self.cuisine_type.title()}")
    
    def open_restaraunt(self):
        print('The Restaraunt is open for customers!')

my_rest = Restaraunt("Domino's Pizza", 'fast food')
print(my_rest.name, my_rest.cuisine_type)

my_rest.decsribe_restaraunt()
my_rest.open_restaraunt()

# 3 Rests (9-2)
your_rest = Restaraunt('Mikel coffee factory', 'coffee shop')
some_rest = Restaraunt('Starbucks', 'coffee shop')
another_rest = Restaraunt('KFC', 'Fast food')

your_rest.decsribe_restaraunt()
some_rest.decsribe_restaraunt()
another_rest.decsribe_restaraunt()

# Users (9-3)
class User:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
    
    def describe_user(self):
        full_name = f"{self.first_name.title()} {self.last_name}"
        print(F"Full name: {full_name.title()}")
        print('Age: %d' % (self.age))
        print(f"Gender: {self.gender.title()}")


    def greeting(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f'Hello {full_name.title()}!')

me = User('Mete batir','Tunkiz', 15, 'male')
friend = User('Ahmed','abdalfettah', 15, 'male')
mother = User('dsajksa dsd','fsdfds', 41, 'female')

me.greeting()
me.describe_user()
print()

friend.greeting()
friend.describe_user()
print()

mother.greeting()
mother.describe_user()
print()
    