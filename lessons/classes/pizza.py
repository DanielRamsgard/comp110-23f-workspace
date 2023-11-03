"""Define class"""

from __future__ import annotations # lets you return class witihn class delcaration

class Pizza:

    # list attributes -> variables that are instantiated <name>: <type>
    size: str
    toppings: int
    gluten_free: bool

    def __init__(self, inp_size: str, inp_toppings: int, inp_gf: bool):
        """My constructor."""
        self.size = inp_size
        self.toppings = inp_toppings
        self.gluten_free = inp_gf

    
    def price(self) -> float:
        """Calculate price of pizza."""
        if self.size == "large":
            price: float = 6.25

        price: float = 5.00
        price += .75 * self.toppings

        if self.gluten_free:
            price += 1.00

        return price
        
        # returns a Pizza object don't have to say return self RV is it tho (points to)


    def add_toppings(self, input_toppings: int):
        self.toppings += input_toppings
        return 
    

    def make_new_pizza_add_toppings(self, num_toppings: int) -> Pizza:
        """Make new p with new tops."""
        new_pizza: Pizza = Pizza(self.size, self.toppings + num_toppings, self.gluten_free)
        return new_pizza