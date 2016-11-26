from nose.tools import *
from CHAOS.player import *
from CHAOS.combat import *

def test_combatScreen():
    player = Player("Player_test", 10, 10, 10, 10)
    enemy = ("Enemy_test", 10, 10)
    assert_equal(combatScreen(player, enemy), 0)
