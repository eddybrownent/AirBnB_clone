#!/usr/bin/python3
"""
This script contains the BaseModel
"""

from datetime import datetime
import models
import uuid


class BaseModel:
    """
    THis class that other classes will inherit from
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes an instance of the BaseModel class

        Args:
            *args: Variable-length argument list
            **kwargs: keyword arguments
        """
        if kwargs:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')

            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of instance"""
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute and saves the instance to storage
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        converts the Basemodel instance to a dictiobary

        Returns:
            dictinary rep of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        return obj_dict
