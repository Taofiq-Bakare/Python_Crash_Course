"""
Modules for users information
"""


class Users:
    def __init__(self, first_name, last_name, age="", country=""):
        """ initialize the attributes available in a user profile"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.login_attempts = 0

    def describe_user(self):
        """ Describe the user"""
        if self.age and self.country:
            print(f"{self.first_name} {self.last_name} {self.age} {self.country}")
        else:
            print(f"{self.first_name} {self.last_name}")

    def greet_user(self):
        """Create a personalized message"""

        print(f"Welcome {self.first_name} {self.last_name} ")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def login(self):
        print(f"There were {self.login_attempts} login attempts today.")
