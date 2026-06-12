
# Number Served (9-4)
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        if len(self.name) > 10:
            print(f"The restaurant name is: {self.name.upper()}")
        else:
             print(f"The restaurant name is: {self.name.title()}")
       
        print(f"Cuisine Type: {self.cuisine_type.title()}")
    
    def open_restaurant(self):
        print('The Restaurant is open for customers!')

    def update_cust_served(self, cust_served):
        self.number_served = cust_served
        return self.number_served # returning value from a method
        
    def increment_num_served(self, num):
        if num <= 0:
            print('You can not add nothing or add a negative number')
        else:
            self.number_served += num
            return self.number_served

my_rest = Restaurant('djssj', 'dskskks')
print(str(my_rest.number_served) + 'customers have been served now')
print('Updating...')
print(str(my_rest.update_cust_served(10)) + ' customers have been served in total')

print('Incrementing...')
print(str(my_rest.increment_num_served(10)) + ' customers have been served by now ')

# Login Attempts (9-5)
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

print()

random_user = User('Mete', 'Tunkiz', 16, 'male', 20)
print(f'Current number of login attempts: {random_user.login_attempts}')
print("Incremented by 1: " + str(random_user.increment_login_attempts()))
print('Resetting...')
print(random_user.reset_login_attempts())
