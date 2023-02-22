#!/usr/bin/python3
""" first class Base """
import json
from os import path


class Base:
    """ Base """

    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor initialization """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
