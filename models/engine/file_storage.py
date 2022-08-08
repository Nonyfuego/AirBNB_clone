#!/usr/bin/python3
"""Serializes instances to a JSON file and.
   deserializes JSON file to instances
"""
import json


class FileStorage(object):
    """Define class FileStorage."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Funtion for return class var __objects.

        Returns:
            dict: list of object and key saved
        """
        return FileStorage.__objects

    def new(self, obj):
        """Funtion for add item to class var __objects.

        Args:
            obj (instance): instance of BaseModel
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Funtion for serialize and save all object in json file."""

        new = {}
        with open(self.__file_path, mode='w', encoding='utf-8') as my_file:
            for k, v in FileStorage.__objects.items():
                new.update({k: v.to_dict()})
            my_file.write(json.dumps(new))

    def reload(self):
        """Deserealize and create intance of object saved in json file"""

        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as my_file:
                from models.base_model import BaseModel
                from models.user import User
                from models.state import State
                from models.city import City
                from models.amenity import Amenity
                from models.place import Place
                from models.review import Review
                new_dict = json.loads(my_file.read())
                for key, value in new_dict.items():
                    class_name = value.get("__class__")
                    objt = eval(class_name + "(**value)")
                    FileStorage.__objects[key] = objt

        except IOError:
            pass
