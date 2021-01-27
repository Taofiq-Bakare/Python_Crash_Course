# create and use a class

class Dog:
    """ A simple attempt to model a dog"""

    def __init__(self, name, age):
        """ initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """
        simulates a dog sitting in response to 
        a command
        """
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """
        simulates rolling over in 
        response to a command
        """
        print(f"{self.name} rolled over!")


""" make instances of the class Dog"""

my_dog = Dog('Bingo', 7)
your_dog = Dog('Jack', 8)

# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog's age is {my_dog.age}.")

""" call the methods """

# my_dog.sit()
# my_dog.roll_over()

your_dog.sit()
your_dog.roll_over()
