#!/usr/bin/env python3

"""
User class that inherits from BaseModel
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """ Class that defines attributes for a User """
    __tablename__ = 'users'


    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    location = Column(String(128), nullable=True)
    phone_number = Column(String(128), nullable=True)

    # Define a relationship to connect a user with their products
    products = relationship('Product', back_populates='owner')
    equipment = relationship('Equipment', back_populate='owner')
    transactions_as_buyer = relationship('Transaction', back_populates='buyer', foreign_keys='Transaction.buyer_id')
    transactions_as_owner = relationship('Transaction', back_populates='owner', foreign_keys='Transaction.owner_id')
