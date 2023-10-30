#!/usr/bin/env python3

""" Module to create a unique FileStorage instance for the application """

import models
from os import getenv
# from models.engine.file_storage import FileStorage

storage_t = getenv("SCOOL_TYPE_STORAGE")
if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()

