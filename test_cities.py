"""
Program that tests the city_functions.py module.

Author: Oscar Lopez
Date: Jan 13, 2019
"""

import unittest
from city_functions import set_location

class SetLocationTestCase(unittest.TestCase):
    """ Tests for city_functions.py"""

    def test_set_location(self):
        location = set_location("san diego","united states")
        self.assertEqual(location,"San Diego, United States")

    def test_set_location_with_states(self):
        location = set_location("san diego","united states","california")
        self.assertEqual(location,"San Diego, California, United States")

unittest.main()