#!/usr/bin/python3
"""
Defines the City class.
"""

from my_models.base_model import MyBaseModel

class City(MyBaseModel):
    """
    Represent a city.

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
