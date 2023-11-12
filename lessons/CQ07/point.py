"""Creating a Point class."""
from __future__ import annotations

__author__ = "730695813"


class Point:
    """Class that takes x and y inputs and performs operations."""
    # defining the attributes
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
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

    def __str__(point: Point) -> str:
        """Prints values of x and y."""
        return f"x: {point.x}; y: {point.y}"
    
    def __mul__(point: Point, factor: int | float) -> Point:
        """Returns new point with scaled variables."""
        # initial setup
        new_point: Point = Point(1.0, 1.0)
        point.x *= factor
        point.y *= factor
        new_point.x = point.x
        new_point.y = point.y

        # return new point
        return new_point
    
    def __add__(point: Point, factor: int | float) -> Point:
        """Adds a value to both x and y."""
        # initial setup
        new_point: Point = Point(0.0, 0.0)
        point.x += factor
        point.y += factor
        new_point.x = point.x
        new_point.y = point.y

        # return the new point
        return new_point


my_p: Point = Point(1.0, 2.0)
print(my_p + 7.0)