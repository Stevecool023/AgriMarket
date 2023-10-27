#!/usr/bin/env python3

"""
Transaction class that inherits from BaseModel
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Float, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Transaction(BaseModel, Base):
    """ Class that defines attributes for agricultural transactions """
    __tablename__ = 'transactions'

    product_id = Column(String(60), ForeignKey('products.id'), nullable=True)
    equipment_id = Column(String(60), ForeignKey('equipment.id'), nullable=True)
    buyer_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    owner_id = Column(String(60), ForeigKey('users.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)

    # Define relationships to connect transactions with products, equipment, buyers, and owners
    product = relationship('Product', foreign_keys='Transaction.product_id', backref='transactions')
    equipment = relationship('Equipment', foreign_keys='Transaction.equipment_id', backref='transactions')
    buyer = relationship('User', foreign_keys='Transaction.buyer_id', back_populates='transactions_as_buyer')
    owner = relationship('User', foreign_keys='Transaction.owner_id', back_populates='transactions_as_owner')
