#!/usr/bin/python3
"""
Test for the Place class
"""
import unittest

from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test cases for the Place class
    """
    def setUp(self):
        """
        Sets up test methods
        """
        pass

    def tearDown(self):
        """
        Tears down test methods
        """
        self.resetStorage()
        pass

    def test_instantiation(self):
        """
        Tests instantiation of Place class
        """
        home = Place()
        self.assertEqual(str(type(home)), "<class 'models.place.Place'>")
        self.assertIsInstance(home, Place)
        self.assertTrue(issubclass(type(home), BaseModel))

    def test_8_attributes(self):
        """
        Tests the attributes of Place class
        """
        attributes = storage.attributes()["Place"]
        home = Place()
        for key, val in attributes.items():
            self.assertTrue(hasattr(home, k))
            self.assertEqual(type(getattr(home, key, None)), val)


if __name__ == "__main__":
    unittest.main()
