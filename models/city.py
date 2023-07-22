#!/usr/bin/python3
"""
This script defines a City class inheriting BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    A class representing a City
    Attributes:
        state_id (str): The Id of the state assorciated with the City
        name (str): Name of the City
    """

    state_id = ""
    name = ""
