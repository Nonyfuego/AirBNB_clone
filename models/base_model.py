#!/usr/bin/python3
"""Create class BaseModel that defines all common
   attributes/methods for other class
"""
from models import storage
from uuid import uuid4
from datetime import datetime


class BaseModel(object):
    """Define class BaseModel."""

    def __init__(self, *args, **kwargs):
        """Initialize constructor."""
        t_form = "%Y-%m-%dT%H:%M:%S.%f"
        self.updated_at = datetime.today()
        self.id = str(uuid4())
        self.created_at = datetime.today()
        if len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, t_form)
                else:
                    if k != "__class__":
                        self.__dict__[k] = v
        else:
            storage.new(self)

    def __str__(self):
        """Representation for name class, id and __dict__.

        Returns:
            string: [class_name] (id) __dict__
        """
        class_name = self.__class__.__name__
        return '[{}] ({}) {}'.format(class_name, self.id, self.__dict__)

    def save(self):
        """Update public instance attributes with the current datetime."""
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """Copy dict od instance for ubdate values.

        Returns:
            dict: dict with new values and update date modificated
        """
        new_dict = self.__dict__.copy()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__

        return new_dict
