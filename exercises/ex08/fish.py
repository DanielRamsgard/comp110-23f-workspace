"""File to define Fish class."""

__author__ = "730695813"


class Fish:
    """Fish class information and methods."""
    
    age: int
    hunger_score: int
    
    def __init__(self):
        """Constructor for class."""
        # initial setup
        self.age = 0
        self.hunger_score = 0

    def one_day(self) -> None:
        """Increases age by one."""
        self.age += 1