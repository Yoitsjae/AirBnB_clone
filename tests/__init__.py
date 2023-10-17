#!/usr/bin/python3
"""
Initialize the storage for the MyModels directory.
"""

from my_models.engine.file_storage import MyFileStorage

my_storage = MyFileStorage()
my_storage.reload()
