from random import randint


class Die:
    """Klasa przedstawiajaca pojedyncza kosc do gry"""

    def __init__(self, num_sides=6):
        """Podstawowa kosc ma postac szescianu"""
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)
