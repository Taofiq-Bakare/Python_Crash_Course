import unittest
from name_function import get_formatted_name as gfn


class NameTestCase(unittest.TestCase):
    """
    Tests for "name_function.py
    """

    def test_first_last_name(self):
        """
        Do names like
        'Janis Joplin'
        work?
        """
        formatted_name = gfn('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """
        Do middle names work?
        """
        formatted_name = gfn('janis', 'japlin', 'joe')
        self.assertEqual(formatted_name, 'Janis Joe Japlin')


# if this program was imported into another module
# the unit test wont run in that program
if __name__ == "__main__":
    unittest.main()
