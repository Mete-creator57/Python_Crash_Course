
# Ice Cream Stand (9-6)
class Restaraunt:
    """Represents a restaraunt"""
    def __init__(self, name, cuisine_type):
        """Represents restaraunt attributes"""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def decsribe_restaraunt(self):
        """Describes a restaraunt"""
        if len(self.name) > 10:
            print(f"The restaraunt name is: {self.name.upper()}")
        else:
             print(f"The restaraunt name is: {self.name.title()}")
       
        print(f"Cuisine Type: {self.cuisine_type.title()}")
    
    def open_restaraunt(self):
        """Tells that a restaraunt is opened"""
        print('The Restaraunt is open for customers!')

    def update_cust_served(self, cust_served):
        """Updates number of already served customers"""
        self.number_served = cust_served
        return self.number_served # returning value from a method
        
    def increment_num_served(self, num):
        """Increments number of served customers"""
        if num <= 0:
            print('You can not add nothing or add a negative number')
        else:
            self.number_served += num
            return self.number_served
        

class IceCreamStand(Restaraunt):
    """Represents an ice cream stand"""
    def __init__(self, name, cuisine_type, flavors):
        """Defining attributes specific to an ice cream stand"""
        super().__init__(name, cuisine_type)

        self.flavors = flavors

    def display_flavors(self):
        for i, flavor in enumerate(self.flavors, 1):
            # making each element in a list start with an uppercase letter
            flavor = flavor.title()
            # leaving some whitespace before an element
            print(f"{i}: {flavor:5}")

smth = IceCreamStand('dsss','fsdsd', ['strawberry', 'chocolate'])
smth.display_flavors()


# Admin (9-7)
class User:
    def __init__(self, first_name, last_name, age, gender, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = login_attempts

    
    def describe_user(self):
        """Displaying full info of a user"""
        full_name = f"{self.first_name.title()} {self.last_name}"
        print(F"Full name: {full_name.title()}")
        print('Age: %d' % (self.age))
        print(f"Gender: {self.gender.title()}")


    def greeting(self):
        """Displaying the greeting message to a console"""
        full_name = f"{self.first_name} {self.last_name}"
        print(f'Hello {full_name.title()}!')

    def increment_login_attempts(self):
        """Incrementing a number of login attempts by 1"""
        self.login_attempts += 1
        return self.login_attempts
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts

class Admin(User):
    """Represents admin and it's capabilities"""
    def __init__(self, first_name, last_name, age, gender, login_attempts):
        """Inherits all attributes of a parent class
        And inits priveleges
        """
        super().__init__(first_name, last_name, age, gender, login_attempts)
        
        # making an instance as an attribute
        self.priveleges = Priveleges(['can add post',
'can delete post', 'can access system settings'])



# Priveleges (9-8)
class Priveleges:
    """A class pertained to priveleges"""
    def __init__(self, priveleges):
          self.priveleges = priveleges

    def show_priveleges(self):
        print('Admin Priveleges: ')
        for pr in self.priveleges:
            print('- ' + pr)

admin = Admin('dsssd', 'dsads', 45, 'sda', 45,)

# accessing through another class
admin.priveleges.show_priveleges()

# Battery Upgrade (9-9)
# in a related file, not here
