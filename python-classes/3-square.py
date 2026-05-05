#!/usr/bin/python3
"""This module represent a class called Square"""


class Square:
    """This class represents a Square."""
    def __init__(self, size=0):
        """inicialize with size"""
        self.__size = size
        if not isinstance(size, int):
            """Validate if the value is an integer"""
            raise TypeError("size must be an integer")
        if size < 0:
            """Validate if the value is greater or equal 0"""
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
