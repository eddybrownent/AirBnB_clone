#!/usr/bin/python3
"""
This script defines the Amenity class inheriting from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    A class representing an Amenity

    Attributes:
        name (str) : the name of the Amenity
    """

    name = ""
