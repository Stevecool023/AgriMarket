#!/usr/bin/env python3

"""
Transaction class that inherits from BaseModel
"""

from models.base_model import BaseModel


class Transaction(BaseModel):
    """ Class that defines attributes for agricultural transactions """

    product_id = ""
    equipment_id = ""
    buyer_id = ""
    owner_id = ""
    quantity = 0
    total_price = 0.0
