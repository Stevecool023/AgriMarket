#!/usr/bin/python3
""" Contains the class DBStorage """

import models
from models.user import User
from models.product import Product
from models.equipment import Equipment
from models.transaction import Transaction
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Modify the classes dictionary as needed for the AgriMarket models.
classes = {"User": User, "Product": Product, "Equipment": Equipment, "Transaction": Transaction}

class DBStorage:
    """ Interacts with the MySQL database """
    __engine = None
    __session = None

    def __init__(self):
        """ Instantiate a DBStorage object """
        SCOOL_MYSQL_USER = getenv('SCOOL_MYSQL_USER')
        SCOOL_MYSQL_PWD = getenv('SCOOL_MYSQL_PWD')
        SCOOL_MYSQL_HOST = getenv('SCOOL_MYSQL_HOST')
        SCOOL_MYSQL_DB getenv('SCOOL_MYSQL_DB')
        SCOOL_ENV = getenv('SCOOL_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                        format(SCOOL_MYSQL_USER,
                                            SCOOL_MYSQL_PWD,
                                            SCOOL_MYSQL_HOST,
                                            SCOOL_MYSQL_DB))
        if SCOOL_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query the current database session """
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[cls] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """ Add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session obj if not None """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Reload data from the database """
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """ Call remove() method on the private session attribute """
        self.__session.remove()
