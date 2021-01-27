

class Employee:
    """
    A class to store staff name and sallary
    """

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, user_input=''):
        """
        a method that increases the annual salary
        by an amount by default or user given
        """
        if user_input:
            add_raise = self.annual_salary + user_input
        else:
            add_raise = self.annual_salary + 5_000
        return add_raise


if __name__ == "__main__":

    user_1 = Employee('Taofiq', 'Bakare', 100_000)

    def_raise = user_1.give_raise(3_000)
    print(f"Your new annual salary is {def_raise}")
