import unittest
from city_function import city_name as cn


class CityNameTest(unittest.TestCase):
    """
    Test for this 
    Ilorin, Kwara
    case
    """

    def test_city_country(self):
        location = cn('ilorin', 'kwara')
        self.assertEqual(location, 'Ilorin, Kwara')

    def test_city_country_population(self):
        location = cn('ilorin', 'kwara', 3_000_000)
        self.assertEqual(location, 'Ilorin, Kwara - Population 3000000')


if __name__ == '__main__':
    unittest.main()
