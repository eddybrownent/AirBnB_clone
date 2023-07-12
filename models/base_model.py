#!/usr/bin/python3


from datetime import datetime
from models import storage
import uuid

class BaseModel:

    def __init__(self, *args, **kwargs):
        if kwargs != {} and kwargs is not None:
            for key in kwargs:
                if key == 'created_at':
                    self.__dict__['created_at'] = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.__dict__['updated_at'] = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
    
    def __str__(self):
        return "[{}] ({}) {}" .format(type(self).__name__, self.id, self.__dict__)
    
    def save(self):
        self.updated_at = datetime.now()
        storage.save()
    
    def to_dict(self):

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()
        return obj_dict
