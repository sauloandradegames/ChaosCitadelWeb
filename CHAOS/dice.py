# dice.py
# Class dice: define a dice and roll dice methods

import random

class Dice:
    def __init__(self, sides):
        # Sides: 4 for d4, 6 for d6...
        self.sides = sides

    def roll(self):
        """ Roll the dice and return the result """
        return random.randint(1, self.sides)

    def multiRoll(self, dices):
        """ Roll a number of dices and return the sum of them """
        sum = 0
        for d in range(dices):
            sum += random.randint(1, self.sides)
        return sum
