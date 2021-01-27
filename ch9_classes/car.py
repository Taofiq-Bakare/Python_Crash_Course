"""
A class that can be used to represent a car.

"""


class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """ Initialize attributes to describe a car"""

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 2000

    def get_descriptive_name(self):
        """ Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, milage):
        """ Set the odometer reading ot the given value."""
        # self.odometer_reading = milage

        """ Reject the role back of the odometer reading"""
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles