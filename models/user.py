#!/usr/bin/env python3

"""
User class that inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """ Class that defines attributes for a User """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
