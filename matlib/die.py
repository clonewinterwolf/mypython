from random import randint
class Die:
    """Class to representing a single die."""
    def __init__(self, num_sides=6):
        """Six-sided die"""
        self.num_sides = num_sides
    
    def roll(self):
        """retrun a random value """
        return randint(1, self.num_sides)