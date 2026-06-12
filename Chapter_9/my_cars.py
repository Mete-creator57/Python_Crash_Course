# importing multiple classes from a single module
from Chapter_9.car import Bike
from Chapter_9.car import Car as C
import Chapter_9.cat as caat

my_car = C('Honda',2020,'ddswe')
print(my_car.describe_car())

my_cat = caat.Cat('male', 'edward', 14)
my_cat.sound()


class Bicycle(Bike):
    def __init__(self, make, year, model, wheel_num=2):
        super().__init__(make, year, model)

        