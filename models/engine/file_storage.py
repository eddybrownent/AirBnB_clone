#!/usr/bin/python3

import os
import json
import datetime


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialized_objects, file)

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }
        return classes

    def reload(self):
        if not os.path.isfile(FileStorage.__file_path):
            return

        with open(self.__file_path, "r", encoding="utf-8") as file:
            serialized_objects = json.load(file)
            reconstructed_objects = {
                key: self.classes()[serialized_obj["__class__"]](**serialized_obj)
                for key, serialized_obj in serialized_objects.items()
            }
            FileStorage.__objects = reconstructed_objects
