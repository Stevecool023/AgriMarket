#!/usr/bin/env python3

"""
Module for serializing and deserializing instances to JSON and keeping storage of instances
Contains the FileStorage class
"""

# Add imports for the AgriMarket models here
# from models.agrimarket_model import AgriMarketModel
# Add other model imports 'as needed'

import json
from models.base_model import BaseModel
from models.user import User
from models.equipment import Equipment
from models.product import Product
from models.transaction import Transaction

# Define classes dictionary for AgriMarket models
# classes = {"AgriMarketModel": AgriMarketModel, ...}


class FileStorage:

    """
    Class that stores and loads instances to/from files in JSON format
    serializes instances to a JSON file & deserializes back to instances
    """

    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        if cls in not None:
            new_dict ={}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj key <obj class name>.id """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj


    def save(self):
        """ Serialize __objects to the JSON file (path: __file_path) """
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)


    def reload(self):
        """
        deserialize the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing. If the file
        doesn't exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except:
            pass

    def delete(self, obj=None):
        """ delete obj from __objects if it's inside """
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """ call reload() method for deserializing the JSON file to objects """
        self.reload()
