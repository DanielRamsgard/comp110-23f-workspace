"""File to define Bear class."""

__author__ = "730695813"


class Bear:
    """Bear class information and methods."""

    age: int
    hunger_score: int
    
    def __init__(self):
        """Constructor for class."""
        # initial setup
        self.age = 0
        self.hunger_score = 0
    
    def one_day(self) -> None:
        """Increases age attribute by one."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        """Increase hunger score."""
        self.hunger_score += num_fish