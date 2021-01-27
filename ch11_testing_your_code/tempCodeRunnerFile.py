    def test_give_default_raise(self):
        """
        A test to see if the default case works
        """
        default_test = Employee.give_raise('Taofiq', 'Bakare', 1000)
        self.assertEqual(default_test, '6000')