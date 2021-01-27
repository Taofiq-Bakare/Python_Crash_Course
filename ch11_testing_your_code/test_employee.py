import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    """
    A class to test the employee program
    """

    def setUp(self):
        """
        Create instances for all test cases
        """
        self.users = Employee('Taofiq', 'Bakare', 1000)

    def test_give_default_raise(self):
        """
        A test to see if the default case works
        """
        default_test = self.users.give_raise()
        self.assertEqual(default_test, 6000)

    def test_give_custom_raise(self):
        """
        A test to see if the custom case works
        """
        default_test = self.users.give_raise(500)
        self.assertEqual(default_test, 1500)


if __name__ == "__main__":
    unittest.main()
