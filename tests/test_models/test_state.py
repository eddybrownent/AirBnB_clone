#!/usr/bin/python3
"""
Unittest module for the State Class
"""

from models.state import State
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
import json
import re
import time
import os


class TestState(unittest.TestCase):
    """
    Test cases for the State class
    """
    def setUp(self):
        """
        Set up test methods
        """
        pass

    def tearDown(self):
        """
        Tear down test methods
        """
        self.reset_storage()
        pass

    def reset_storage(self):
        """
        Reset FileStorage data
        """
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """
        Test instantiation of State class
        """
        state = State()
        self.assertEqual(str(type(state)), "<class 'models.state.State'>")
        self.assertIsInstance(state, State)
        self.assertTrue(issubclass(type(state), BaseModel))

    def test_attributes(self):
        """
        Test the attributes of State class
        """
        attributes = storage.attributes()["State"]
        state = State()
        for attr_name, attr_type in attributes.items():
            self.assertTrue(hasattr(state, attr_name))
            self.assertEqual(type(getattr(state, attr_name, None)), attr_type)


if __name__ == "__main__":
    unittest.main()
