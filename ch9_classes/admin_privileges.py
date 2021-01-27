"""
A module that contains the subclasses for
the users module

"""
from users import Users


class Admin(Users):
    def __init__(self, first_name, last_name, age, country):
        """ inherit the superclass attributes"""
        super().__init__(first_name, last_name, age=age, country=country)
        self.privileges = Privileges()


class Privileges:
    def __init__(self,):
        """
        prints the Admin privileges
        """
        self.privileges = [" can add posts",
                           " can delete posts", " can troubleshoot the system"]

    def show_privileges(self):
        """
        print the privileges given to the admin
        """
        print("The Admin privileges are :")

        for priv in self.privileges:
            print(f"{priv.title()}")
