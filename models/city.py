#!/usr/bin/python3
"""New class inherit from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class City that inherit from BaseModel"""

    state_id = ""
    name = ""
