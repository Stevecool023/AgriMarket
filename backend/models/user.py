#!/usr/bin/env python3

"""
User class that inherits from BaseModel
"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """ Class that defines attributes for a User """
    if models.storage_t == 'db':
        __tablename__ = 'users'


        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        location = Column(String(128), nullable=True)
        phone_number = Column(String(128), nullable=True)
        # Define a relationship to connect a user with their products
        products = relationship('Product', backref='user')
        equipment = relationship('Equipment', backref='user')
        transactions = relationship('Transaction', backref='user', foreign_keys='Transaction.user_id')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
        location = ""
        phone_number = ""

    def __init__(self, *args, **kwargs):
        """ initializes user """
        super().__init__(*args, **kwargs)
