#!/usr/bin/env python3

"""
Product class that inherits from BaseModel
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Product(BaseModel, Base):
    """ Class that defines attributes for agricultural products """
    if models.storage_t == 'db':
        __tablename__ = 'products'

        name = Column(String(128), nullable=False)
        description = Column(String(256), nullable=True)
        quantity = Column(Integer, nullable=False)
        price = Column(Float, nullable=False)
        category = Column(String(128), nullable=True)
        location = Column(String(128), nullable=True)
