#!/usr/bin/python3
"""
Unittest module for the City Class
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test cases for the City class
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
        Home = City()
        self.assertEqual(str(type(Home)), "<class 'models.city.City'>")
        self.assertIsInstance(Home, City)
        self.assertTrue(issubclass(type(Home), BaseModel))

    def test_city_is_a_subclass_of_basemodel(self):
        self.assertTrue(issubclass(type(self.city), BaseModel))

    def test_8_attributes(self):
        """
        Tests the attributes of City class
        """
        attributes = storage.attributes()["City"]
        Home = City()
        for key, val in attributes.items():
            self.assertTrue(hasattr(Home, key))
            self.assertEqual(type(getattr(Home, k, None)), val)


if __name__ == "__main__":
    unittest.main()
