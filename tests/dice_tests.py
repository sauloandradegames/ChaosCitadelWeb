from nose.tools import *
from CHAOS.dice import *

def test_rollDice():
    dice = Dice(6)
    dice.roll()

def test_multiRoll():
    dice = Dice(6)
    dice.multiRoll(2)
