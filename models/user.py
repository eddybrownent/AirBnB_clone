#!/usr/bin/python3
"""
This script has a class User
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    This class represents a User

    attributes:
        email (str): The email address of the User
        password (str): The password of the User
        first_name (str): The first name of the User
        last_name (str): The last name of the User.
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
