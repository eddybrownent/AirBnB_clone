#!/usr/bin/python3
"""
This script defines the Place class
"""

from models.base_model import BaseModel


class Place(BaseModel):
<<<<<<< HEAD
    city_id = ""
    user_id = ""
    name = ""
    description = ""
=======
    """
    This class represents a Place
    """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
>>>>>>> 1143054 (pycodestyle and output errors fixing)
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
