#!/usr/bin/python3

import os
import json
import datetime
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns  dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects with key
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects
        to the JSON file
        """
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes a JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, mode='r') as file:
                new_dict = json.load(file)

            for key, val in new_dict.items():
                class_name = val.get('__class__')
                obj = eval(class_name + '(**val)')
                FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass
