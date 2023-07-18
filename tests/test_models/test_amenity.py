#!/usr/bin/python3
"""
Unittest module for the Amenity Class
"""

import json
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test Cases for the Amenity class
    """

    def setUp(self):
        """
        Sets up the test methods
        """
        pass

    def tearDown(self):
        """
        Tears down the test methods
        """
        self.resetStorage()
        pass

    def resetStorage(self):
        """
        Resets the FileStorage data
        """
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """
        Tests instantiation of the Amenity class
        """
        ame = Amenity()
        self.assertEqual(str(type(ame)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(ame, Amenity)
        self.assertTrue(issubclass(type(ame), BaseModel))

    def test_attributes(self):
        """
        Tests the attributes of Amenity class
        """
        attributes = storage.attributes()["Amenity"]
        ame = Amenity()
        for attr_name, attr_type in attributes.items():
            self.assertTrue(hasattr(ame, attr_name))
            self.assertEqual(type(getattr(ame, attr_name, None)), attr_type)


if __name__ == "__main__":
    unittest.main()
