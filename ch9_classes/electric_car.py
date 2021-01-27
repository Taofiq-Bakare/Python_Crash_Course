""" 
A module for the electric car that depends on
the car superclass
"""

""" experiment with inheritance"""




from car import Car
class ElectricCar(Car):
    """" Represents aspects specific to electric cars"""

    def __init__(self, make, model, year):
        """ Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()


class Battery:
    """
    A simple attempt to model a battery for an electric car.
    """

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def desscribe_battery(self):
        """
        print  a statement describing the battery size
        """
        print(f"This car has a {self.battery_size}-KWh battery")

    def get_range(self):
        """
        Print a statement about the range this battery provides.
        """
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on full charge")

    def upgrade_battery(self,):
        if self.battery_size < 100:
            self.battery_size = 100
