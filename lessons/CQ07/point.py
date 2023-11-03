"""Creating a Point class."""
from __future__ import annotations

__author__ = "730695813"


class Point:
    """Class that takes x and y inputs and performs operations."""
    # defining the attributes
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Constructor for Point class."""
        # set inputs to class attributes
        self.x = x_init
        self.y = y_init
    
    def scale_by(self, factor: int) -> None:
        """A method that scales by a certain factor."""
        # scaliing the values by the input factor
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Retuns a Point object that has scaled x and y values."""
        # create new object of class
        new_point: Point = Point(self.x, self.y)

        # create scaled x and y values
        new_point.x *= factor
        new_point.y *= factor

        # return a new point
        return new_point