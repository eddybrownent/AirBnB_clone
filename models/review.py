#!/usr/bin/python3
"""
This script defines a Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This class represents a Review

    Attributes:
        place_id (str): ID of the Place associated with the Review
        user_id (str): ID of the User associated with the Review
        text (str): The text content of the Review
    """

    place_id = ""
    user_id = ""
    text = ""
