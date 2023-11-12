"""File to define River class."""

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear

__author__ = "730695813"


class River:
    """River class information and methods."""
    
    def __init__(self, num_fish: int, num_bears: int): 
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Check ages and remove if necessary."""
        # initial setup
        self.surviving_fish: list[Fish] = list()
        self.surviving_bears: list[Bear] = list()

        # iterate over list
        for i in range(0, len(self.fish), 1):
            if self.fish[i].age <= 3:
                self.surviving_fish.append(self.fish[i])

        # iterate over list
        for i in range(0, len(self.bears), 1):
            if self.bears[i].age <= 5:
                self.surviving_bears.append(self.bears[i])

        # update lists
        self.fish = self.surviving_fish
        self.bears = self.surviving_bears

    def bears_eating(self) -> None:
        """Eats fish."""
        # check initial condition
        for i in range(0, len(self.bears), 1):
            if len(self.fish) <= 5:    
                return
            self.bears[i].eat(3)
            for i in range(0, 3, 1):
                self.fish.pop(i)
    
    def check_hunger(self) -> None:
        """Checks bear's hunger."""
        # initial setup
        self.healthy_bears: list[Bear] = list()

        # iterate over the bears
        for i in range(len(self.bears)):
            if self.bears[i].hunger_score >= 0:
                self.healthy_bears.append(self.bears[i])
        
        # update list
        self.bears = self.healthy_bears
        
    def repopulate_fish(self) -> None:
        """Adds fish to population."""
        # initial setup
        self.new_fish_num = (len(self.fish) // 2) * 4

        # iterate over list
        for i in range(0, self.new_fish_num, 1):
            self.fish.append(Fish())
    
    def repopulate_bears(self) -> None:
        """Add bears to population."""
        # initial setup
        self.new_bear_num: int = len(self.bears) // 2

        # iterate over list and add bears
        for i in range(0, self.new_bear_num):
            self.bears.append(Bear())
    
    def remove_fish(self, amount: int) -> None:
        """Removes a certain amount of fish from the river."""
        # check edge case
        if len(self.fish) < amount:
            self.fish = list()
        
        # iterate over fish and remove them
        for i in range(0, amount, 1):
            self.fish.pop(i)
    
    def view_river(self) -> None:
        """View river shows river status."""
        # running print commands
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
            
    def one_river_day(self) -> None:
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """Calls one_river_day() seven times."""
        for i in range(0, 7, 1):
            self.one_river_day()