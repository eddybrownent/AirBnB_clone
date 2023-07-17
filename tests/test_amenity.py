#!/usr/bin/python3
"""Defines unittest for amenity.py"""
from tests.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_base_model):
    """tests instantiation of amenity class"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        new = self.value()
        self.assertEqual(type(new.name), str)
