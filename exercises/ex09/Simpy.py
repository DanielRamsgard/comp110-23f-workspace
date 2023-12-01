"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730695813"


class Simpy:
    """Simpy class declaration."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Constrcutor for Simpy class."""
        self.values = values

    def __str__(self) -> str:
        """Returns list of values."""
        # return the f string
        return f"Simpy({self.values})"
    
    def fill(self, input_val: float, num_val: int) -> None:
        """Method for filling values with a specific float."""
        # initial setup
        self.values = list()

        # loop over list and append values
        for i in range(0, num_val, 1):
            self.values.append(input_val)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Method for putting a range of values into values."""
        # assertion so that step is not 0.0
        assert step != 0.0

        # initial setup
        self.values = list()
        num_iterations: int = int((stop - start) / step)
        current_val = start

        # loop over list 
        for i in range(0, num_iterations, 1):
            self.values.append(current_val)
            current_val += step
    
    def sum(self) -> float:
        """Method returns sum of values within self.values."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Method performs element-wise addition."""
        # initial setup
        float: float = 1.0
        final_simpy: Simpy = Simpy([])

        # code block for if we have a float as input two
        if type(float) is type(rhs):
            for i in range(0, len(self.values), 1):
                final_simpy.values.append(self.values[i] + rhs)
            
            # return statement for float type of input two
            return final_simpy
        
        # assertion
        assert len(self.values) == len(rhs.values)

        # code block for if we have a simpy as input two
        for i in range(0, len(self.values), 1):
            final_simpy.values.append(self.values[i] + rhs.values[i])
        
        # return statement for simpy type as input two
        return final_simpy
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Method performs element-wise exponentiation."""
        # initial setup
        float: float = 1.0
        final_simpy: Simpy = Simpy([])

        # code block for if we have a float as input two
        if type(float) is type(rhs):
            for i in range(0, len(self.values), 1):
                final_simpy.values.append(self.values[i] ** rhs)
            
            # return statement for float type of input two
            return final_simpy
        
        # assertion
        assert len(self.values) == len(rhs.values)

        # code block for if we have a simpy as input two
        for i in range(0, len(self.values), 1):
            final_simpy.values.append(self.values[i] ** rhs.values[i])
        
        # return statement for simpy type as input two
        return final_simpy
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Method creates a mask with values relating to equality."""
        # initial setup
        float: float = 1.0
        final_list: list[bool] = list()

        # code block for if we have a float as input two
        if type(float) is type(rhs):
            for i in range(0, len(self.values), 1):
                if self.values[i] == rhs:
                    final_list.append(True)
                else: 
                    final_list.append(False)
            
            # return statement for float type of input two
            return final_list
        
        # assertion
        assert len(self.values) == len(rhs.values)

        # code block for if we have a simpy as input two
        for i in range(0, len(self.values), 1):
            if self.values[i] == rhs.values[i]:
                final_list.append(True)
            else:
                final_list.append(False)
        
        # return statement for simpy type as input two
        return final_list
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Method returns a mask if values are greater than values on right-side of operand."""
        # initial setup
        float: float = 1.0
        final_list: list[bool] = list()

        # code block for if we have a float as input two
        if type(float) is type(rhs):
            for i in range(0, len(self.values), 1):
                if self.values[i] > rhs:
                    final_list.append(True)
                else: 
                    final_list.append(False)
            
            # return statement for float type of input two
            return final_list
        
        # assertion
        assert len(self.values) == len(rhs.values)

        # code block for if we have a simpy as input two
        for i in range(0, len(self.values), 1):
            if self.values[i] > rhs.values[i]:
                final_list.append(True)
            else:
                final_list.append(False)
        
        # return statement for simpy type as input two
        return final_list
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """This method returns certain values at a certain indexes or ones that correspond to a mask."""
        # initial setup
        int_check: int = 1
        final_simpy: Simpy = Simpy([])

        # check if we have an int
        if type(int_check) is type(rhs):
            return self.values[rhs]
        
        # continue if we have a mas
        for i in range(0, len(self.values), 1):
            if rhs[i]:
                final_simpy.values.append(self.values[i])

        # return statement
        return final_simpy