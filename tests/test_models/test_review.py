#!/usr/bin/python3
"""Test suite for Review class in models.review"""
import unittest

from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test cases for the Review class
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

    def test_8_instantiation(self):
        """
        Tests instantiation of Review class
        """
        text = Review()
        self.assertEqual(str(type(text)), "<class 'models.review.Review'>")
        self.assertIsInstance(text, Review)
        self.assertTrue(issubclass(type(text), BaseModel))

    def test_8_attributes(self):
        """
        Tests the attributes of Review class
        """
        attributes = storage.attributes()["Review"]
        text = Review()
        for key, val in attributes.items():
            self.assertTrue(hasattr(text, key))
            self.assertEqual(type(getattr(text, key, None)), val)


if __name__ == "__main__":
    unittest.main()
