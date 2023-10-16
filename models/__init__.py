#!/usr/bin/python3
"""
Initialize the magic method for the models directory.
"""

from my_models.my_engine.my_file_storage import MyFileStorage

storage = MyFileStorage()
storage.reload()
