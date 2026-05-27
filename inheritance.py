# importing 'Car' class from car module (another file)
from car import Car

# subclass (child class)
class Hybrid_Car(Car):
    """Represent aspects of a car that pertain to hybrid cars"""
    # default argument (is_fast=True)
    def __init__(self, make, year, model, is_fast=True,):
        """ Initialize attributes of the parent class.
        Then initialize attributes pertained to a hybrid car
        """
        # calling the parent class to inherit all the methods from it
        # so an instance of Hybrid_Car class can access all of it's parent methods
        super().__init__(make, year, model) 

        # defining a new attribute specifically for a child class
        self.battery = Battery()
        self.wheel_drive = 'FWD'
        # initializing an instance as an attribute
        self.is_fast = Speed(201)
        

    def update_wheel_drive(self, wheel_drive_type):
        self.wheel_drive = wheel_drive_type
        return self.wheel_drive
    

    # overriding parent class's method
    def fill_petrol_tank(self, amount):
        print("The hybrid is fueled with savings in mind...")
        # We still can access the result of parent class's method
        # returns an updated value of self.gas_amount.
        # super(). function is used for accessing parent class's methods and attributes
        # it depends on what method you type after (.)
        return super().fill_petrol_tank(amount) 

# Creating another class to test Composition
class Speed:
    def __init__(self, speed, is_fast=True):
        self.is_fast = is_fast
        self.speed = speed

    def describe_speed(self):
        if self.speed > 200:
            self.is_fast = True
            print(F'Result: {self.is_fast}')
            print(f'This car is fast! Max Speed: {self.speed}')
            return self.speed
        else:
            self.is_fast = False
            print(F'Result: {self.is_fast}')
            print(f'This car is slow! Max Speed: {self.speed}')
            return self.speed
        
class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65
            return self.battery_size
        
    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + "-kWh battery.")
        
    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 125
        
        print(f'This car can go about {range} miles on a full charge')


            



# creating an instance
toyota = Hybrid_Car('toyota'.title(), '2021', 'corolla'.upper(), is_fast=False)

# accessing parent class's method
print(toyota.describe_car())

# child class's method
toyota.battery.describe_battery()

print(f'WHEEL DRIVE TYPE: {toyota.update_wheel_drive('AWD')}')
print(f"Before fueling: {toyota.petrol_amount}")
# updating self.petrol_amount value (incrementing by 10)
toyota.fill_petrol_tank(10)
print(toyota.petrol_amount)


print()
toyota.is_fast.describe_speed()


toyota.battery.describe_battery()

toyota.battery.get_range()
toyota.battery.upgrade_battery()
toyota.battery.get_range()