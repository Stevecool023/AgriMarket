#!/usr/bin/env python3

"""
Equipment class that inherits from BaseModel
"""

from models.base_model import BaseModel


class Equipment(BaseModel):
    """ Class that defines attributes for agricultural equipment """
    name = ""
    description = ""
    quantity = 0
    price = 0.0
    condition = ""
    location = ""
    owner_id = ""
