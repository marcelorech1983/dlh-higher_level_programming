#!/usr/bin/python3
"""This module represent a class called Square"""


class Square:
    """This class represents a Square."""
    def __init__(self, size=0):
        """inicialize with size"""
        self.size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """Return the size."""
        return self.__size

    @size.setter
    def size(self, size=0):
        """Define the size with validation"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Define the area."""
        return self.__area
