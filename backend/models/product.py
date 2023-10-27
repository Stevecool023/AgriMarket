#!/usr/bin/env python3

"""
Product class that inherits from BaseModel
"""

from models.base_model import BaseModel


class Product(BaseModel):
    """ Class that defines attributes for agricultural products """

    name = ""
    description = ""
    quantity = 0
    price = 0.0
    category = ""
    location = ""
    owner_id = ""
