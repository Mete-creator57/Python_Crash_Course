# Working with Classes and Instances
# Returning values from a class

"""A set of classes """


class Car:
    """A class that can be used to represent a car and it's properties"""
    def __init__(self, make, year, model):
        """Initializes car's attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.petrol_amount = 0
    
    def describe_car(self):
        """Stores car's attributes in a single variable
        And then return it
        """
        description = f"{self.make} {self.model} {self.year}"
        return description
    
    def fill_petrol_tank(self, amount):
        """Updates petrol amount by assigning a  given parameter to it
        and the returns it
        """
        print('Filling the petrol tank...')
        self.petrol_amount = amount
        return self.petrol_amount
    




# only gets executed when this file is running
if __name__ == 'main':
    # assign the returned value to an isntance
    my_car = Car('Audi', '2024', 'A4')
    print(my_car.describe_car())

    # turns into a list
    # split() function is used to turn a returned string to a list
    #  and assign it
    feats = my_car.describe_car().split()
    print(feats)
    # printing each element in a list
    for feat in feats:
        print(feat)


# Setting A Default Value for an Attribute 
# Modifying Attribute Values
"""A class representing a bike and it's properties"""
class Bike:
    def __init__(self, make, year, model):
        """Initializes attributes along with a defalut attribute"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # a default attribute
    
    def describe_bike(self):
        """Returning a Value from a method"""
        description = f"{self.make} {self.model} {self.year}"
        return description
    
    def read_odometer(self):
        """Printing the bikes's milleage"""
        print(f"Total miles on your bike: {self.odometer_reading} ")

    def update_odometer(self, mileage):
        """Set the odometer reading to a given value, making sure that a given value
        is not less than the previous odometer reading"""
        if mileage < self.odometer_reading:
            print('You can not roll back an odometer!')
        elif mileage == self.odometer_reading:
            print('New value can not be equal to a previous one!')
        else:
            self.odometer_reading = mileage # updating attribute's value
            # displaying only 2 decimal places after an integer
            print(f'Now odometer is {self.odometer_reading:.2f}')
        

    def increase_odometer(self, increasing):
        """Increments value of the odometer"""
        if increasing <= 0:
            print('Value can not be less or equal to 0!')
        else:
            self.odometer_reading += increasing
            print(f'Increased by {increasing:.2f}')
            print(F'Updated odo: {self.odometer_reading:.2f}')




# insurance
if __name__ == 'main':
    my_bike = Bike('Honda', '2024', 'A4')
    my_bike.read_odometer()
    my_bike.describe_bike()
    my_bike.update_odometer(40)
    my_bike.increase_odometer(40.21)





