#!/usr/bin/python3
"""Defines unittests for models/state.py"""
from tests.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """tests instantiation of the state class"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = state

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
