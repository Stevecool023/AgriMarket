#!/usr/bin/env python3

"""
Equipment class that inherits from BaseModel
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Equipment(BaseModel, Base):
    """ Class that defines attributes for agricultural equipment """
    __tablename__ = 'equipment'


    name = Column(String(128), nullable=False)
    description = Column(String(256), nullable=True)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    condition = Column(String(128), nullable=True)
    location = Column(String(128), nullable=True)
    owner_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    # Define a relationship to connect equipment with its owner (user)
    owner = relationship('User', back_populates='equipment')
