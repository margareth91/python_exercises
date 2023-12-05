import random


class Die:

    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        result = random.randint(1, self.sides)
        print(f"Na kostce wyrzucono {result}.")
        # return result


die1 = Die(sides=6)
die1.roll_die()

die2 = Die(sides=10)
die2.roll_die()

die3 = Die(sides=20)
die3.roll_die()
