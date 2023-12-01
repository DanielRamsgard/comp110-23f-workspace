"""Pratice for quiz 3."""

from __future__ import annotations


class ChristmasTreeFarm:

    plots: list[int]

    def __init__(self, plots: int, initial_planting: int):
        """Constructor for class."""
        self.plots = list()

        for i in range(0, initial_planting, 1):
            self.plots.append(1)

        if plots > initial_planting:
            for i in range(0, plots - initial_planting, 1):
                self.plots.append(0)

    def plant(self, i: int) -> None:
        """Replaces a plot with tree of size 1."""
        self.plots[i] = 1

    def growth(self) -> None:
        """Increases size of each tree by 1."""
        for i in range(0, len(self.plots), 1):
            if self.plots[i] != 0: 
                self.plots[i] += 1

    def harvest(self, replant: bool) -> int:
        """Returns count of harvested trees."""
        count: int = 0

        for i in range(0, len(self.plots), 1):
            if self.plots[i] >= 5:
                if replant:
                    self.plots[i] = 1
                elif not(replant):
                    self.plots[i] = 0
                count += 1 

        return count
    
    def __add__(self, farm: ChristmasTreeFarm) -> ChristmasTreeFarm:
        """Sums them."""
        trees: int = 0

        for tree in self.plots:
            if tree > 0:
                trees += 1

        for tree in farm.plots:
            if tree > 0:
                trees += 1

        new_farm: ChristmasTreeFarm = ChristmasTreeFarm(len(self.plots) + len(farm.plots), trees)
        return new_farm