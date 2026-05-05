#!/usr/bin/python3
"""This module represent a class called Square"""


class Square:
    """This class represents a Square."""
    def __init__(self, size=0):
        """inicialize with size"""
        self.size = size

    def area(self):
        """Define the area."""
        self.area = []
        return self.area

    @property
    def size(self):
        """Return the size."""
        return self.__size

    @size.setter
    def size(self, size):
        """Define the size with validation"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
