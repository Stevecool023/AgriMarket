#!/usr/bin/env python3
"""
BaseModel class that defines all common attributes/methods for other classes

"""

# Import storage here if needed
from datetime import datetime
from uuid import uuid4
import models

if models.storage_t == "db":
    from sqlalchemy import Column, String, DateTime
    from sqlalchemy.ext.declarative import declarative_base
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    if models.storage_t == "db":
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
        updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Update the to_dict() method as mentioned in the initial instructions.
    # Add teh delete() method as described in the initial instructions.

    """BaseModel Class definition"""
    
    def __init__(self, *args, **kwargs):

        """ Constructor """

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue

                if (key == "created_at" or key == "updated_at"):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

            
                setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)


    def __str__(self):
        """ Define what should be printed for each instance of the class """
        st = "[{:s}] ({:s}) {:s}"
        st = st.format(self.__class__.__name__, self.id, str(self.__dict__))
        return st

    def save(self):
        """

        Update the Public Instance Attr updated_at with the current datetime

        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        dcopy = self.__dict__.copy()
        dcopy["__class__"] = self.__class__.__name__
        dcopy["created_at"] = self.created_at.isoformat()
        dcopy["updated_at"] = self.updated_at.isoformat()
        return dcopy
