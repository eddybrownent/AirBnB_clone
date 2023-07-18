#!/usr/bin/python3
"""
Unittest module for the BaseModel Class
"""

import json
import os
import re
import time
import unittest
import uuid
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test Cases for the BaseModel class
    """
    def setUp(self):
        """
        Set up test methods
        """
        pass

    def tearDown(self):
        """
        Tear down test methods
        """
        self.reset_storage()
        pass

    def reset_storage(self):
        """
        Reset FileStorage data
        """
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """
        Test instantiation of BaseModel class
        """
        base_model = BaseModel()
        self.assertEqual(str(type(base_model)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(base_model, BaseModel)
        self.assertTrue(issubclass(type(base_model), BaseModel))

    def test_init_no_args(self):
        """
        Test __init__ with no arguments
        """
        self.reset_storage()
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_init_many_args(self):
        """
        Test __init__ with many arguments
        """
        self.reset_storage()
        args = [i for i in range(1000)]
        base_model = BaseModel(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        base_model = BaseModel(*args)

    def test_attributes(self):
        """
        Test attributes value for instance of a BaseModel class
        """
        attributes = storage.attributes()["BaseModel"]
        base_model = BaseModel()
        for attr_name, attr_type in attributes.items():
            self.assertTrue(hasattr(base_model, attr_name))
            self.assertEqual(type(getattr(base_model, attr_name, None)), attr_type)

    def test_datetime_created(self):
        """
        Test if updated_at & created_at are current at creation
        """
        date_now = datetime.now()
        base_model = BaseModel()
        diff = base_model.updated_at - base_model.created_at
        self.assertTrue(abs(diff.total_seconds()) < 0.01)
        diff = base_model.created_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.1)

    def test_id(self):
        """
        Test for unique user ids
        """
        id_list = [BaseModel().id for i in range(1000)]
        self.assertEqual(len(set(id_list)), len(id_list))

    def test_save(self):
        """
        Test the public instance method save()
        """
        base_model = BaseModel()
        time.sleep(0.5)
        date_now = datetime.now()
        base_model.save()
        diff = base_model.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_str(self):
        """
        Test for __str__ method
        """
        base_model = BaseModel()
        rex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        res = rex.match(str(base_model))
        self.assertIsNotNone(res)
        self.assertEqual(res.group(1), "BaseModel")
        self.assertEqual(res.group(2), base_model.id)
        s = res.group(3)
        s = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", s)
        d = json.loads(s.replace("'", '"'))
        d2 = base_model.__dict__.copy()
        d2["created_at"] = repr(d2["created_at"])
        d2["updated_at"] = repr(d2["updated_at"])
        self.assertEqual(d, d2)

    def test_to_dict(self):
        """
        Test the public instance method to_dict()
        """
        base_model = BaseModel()
        base_model.name = "Laura"
        base_model.age = 23
        d = base_model.to_dict()
        self.assertEqual(d["id"], base_model.id)
        self.assertEqual(d["__class__"], type(base_model).__name__)
        self.assertEqual(d["created_at"], base_model.created_at.isoformat())
        self.assertEqual(d["updated_at"], base_model.updated_at.isoformat())
        self.assertEqual(d["name"], base_model.name)
        self.assertEqual(d["age"], base_model.age)

    def test_to_dict_no_args(self):
        """
        Test to_dict() with no arguments
        """
        self.reset_storage()
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict()
        msg = "to_dict() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_to_dict_excess_args(self):
        """
        Test to_dict() with too many arguments
        """
        self.reset_storage()
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict(self, 98)
        msg = "to_dict() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def test_instantiation_with_kwargs(self):
        """
        Test instantiation with **kwargs
        """
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_new_model.to_dict(), my_model.to_dict())

    def test_instantiation_dict(self):
        """
        Test instantiation with **kwargs from custom dict
        """
        d = {
            "__class__": "BaseModel",
            "updated_at": datetime(2050, 12, 30, 23, 59, 59, 123456).isoformat(),
            "created_at": datetime.now().isoformat(),
            "id": uuid.uuid4(),
            "var": "foobar",
            "int": 108,
            "float": 3.14
        }
        o = BaseModel(**d)
        self.assertEqual(o.to_dict(), d)

    def test_save_called_from_save(self):
        """
        Test that storage.save() is called from save()
        """
        self.reset_storage()
        base_model = BaseModel()
        base_model.save()
        key = "{}.{}".format(type(base_model).__name__, base_model.id)
        d = {key: base_model.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path, "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(d)))
            f.seek(0)
            self.assertEqual(json.load(f), d)

    def test_save_no_args(self):
        """
        Test save() with no arguments
        """
        self.reset_storage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save()
        msg = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)


if __name__ == '__main__':
    unittest.main()
