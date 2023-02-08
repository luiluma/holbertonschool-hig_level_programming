#!/usr/bin/python3


class Square():
    """class initialization"""
    def __init__(self, size=0):
        """ Definition with private instance attribute size
        which is assigned with the double underscore before given name"""
        self.__size = size
        if type(size) is not int:
            raise typeerror("size must be an integer")
        if size < 0
            raise valueerror("size must be >= 0")
