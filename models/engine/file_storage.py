#!/usr/bin/python3
""" FileStorage that serializes instances to a JSON file and deserializes JSON
file to instances:
"""

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """ Class FileStorage that serializes instances to a JSON file and deserializes
    JSON file to instances:
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects:
        """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id:
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path):
        """
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """ Deserializes the JSON file to __objects:
        """
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for k, v in json.load(f).items():
                    self.__objects[k] = eval(v['__class__'])(**v)
                    self.__objects[k].__dict__ = v
        except FileNotFoundError:
            pass