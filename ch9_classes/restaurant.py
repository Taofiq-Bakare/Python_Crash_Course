"""
A module for restaurants

"""


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, ):
        """ initialize restaurant name and cuisine types"""

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """ Prints the name of the restaurant and the
        available cuisines"""
        print(f"The restaurant's name is {self.restaurant_name}")
        print(f"They serve {self.cuisine_type} dishes")

    def open_restaurant(self):
        """ It prints that the restaurant is
        opened for business"""
        print("The restaurant is opened. ")

    def customers_served(self):
        print(f"{self.number_served} customers have been served")

    def set_number_served(self, served_customers):
        self.number_served += served_customers

    def incre_number_served(self, incre_customers):
        self.number_served += incre_customers


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vanilla", "strawberry", "chocolate"]

    def ice_cream_flavors(self):
        print(f"The flavors of ice creams available are:")
        for ice in self.flavors:
            print(f"{ice.title()}")
