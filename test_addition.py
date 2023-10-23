import unittest
from math_problems import add

class TestAddition(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(3, 2), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)
