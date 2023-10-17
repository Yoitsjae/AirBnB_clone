#!/usr/bin/python3
"""
Defines the Amenity class.
"""

from my_models.base_model import MyBaseModel

class Amenity(MyBaseModel):
    """
    Represent an amenity.

    Attributes:
        name (str): The name of the amenity.
    """
    name = ""
