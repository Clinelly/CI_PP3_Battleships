# Code inspired by Corey Schafer's unittest video:
# (https://www.youtube.com/watch?v=6tNS--WetLI)
# code modified for functionality of this project.
# imports unittest module.
import unittest
# imports login.py file
import login


class TestLogin(unittest.TestCase):
    """
    Sets up a class with different methods to test each login.py function.
    setUp establishes the variable to be used in each test.
    """
    def setUp(self):
        self.valid_input = {'y', 'n'}
        self.str_input_1 = 'g'
        self.int_input_1 = 1
        self.str_input_2 = "G"
        self.float_input = 2.5

    def tearDown(self):
        pass

    def test_login(self):
        self.assertNotIn(self.str_input_1, self.valid_input)
        self.assertNotIn(self.int_input_1, self.valid_input)
        self.assertNotIn(self.str_input_2, self.valid_input)
        self.assertNotIn(self.float_input, self.valid_input)

    def test_check_login(self):
        with self.assertRaises(ValueError):
            if self.str_input_1 not in self.valid_input:
                raise ValueError
            elif self.int_input_1 not in self.valid_input:
                raise ValueError


if __name__ == '__main__':
    unittest.main()
