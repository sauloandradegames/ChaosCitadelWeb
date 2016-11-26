# combat.py
# Combat management

from CHAOS.player import *
from CHAOS.dice import *
#import random
import os

def combatScreen(player, enemy):
    """ Implement the combat screen (Terminal only) """
    # player: reference from a player object
    # enemy: a tuple (str enemy_name, int enemy_hp, int enemy_skill)

    d6 = Dice(6)
    player_atk = 0 # Player atk power
    enemy_atk = 0 # Enemy atk power

    enemy_name = enemy[0] # get enemy name from input
    enemy_energy = enemy[1] # get enemy life from input
    enemy_skill = enemy[2] # get enemy skill from input

    combat_inProgress = True # for control the combat loop

    while combat_inProgress:
        # Clear screen, print combat info
        os.system("clear")
        print "Player: [EN: " + str(player.getEnergy()) + "/" + str(player.getMaxEnergy()) + "] [SK: " + str(player.getSkill()) + "] [LK: " + str(player.getLuck()) + "]"
        print enemy_name + ": [EN: " + str(enemy_energy) + "] [SK: " + str(enemy_skill) + "]"
        print ""

        # Calculate player and enemy attack power:
        # > Roll 2d6 for the player. Add the player skill.
        # > Roll 2d6 for the enemy. Add the enemy skill.
        player_atk = d6.multiRoll(2) + player.getSkill()
        enemy_atk = d6.multiRoll(2) + enemy_skill

        print "Player atk: " + str(player_atk)
        print "Enemy  atk: " + str(enemy_atk)
        print ""

        # Combat rules:
        # player_atk > enemy_atk: Player hits
        # > Player can test luck to amplify damage
        # player_atk < enemy_atk: Enemy hits
        # > Player can test luck to reduce incoming damage
        # player_atk = enemy_atk: Nobody hits
        # > Neither player nor enemy takes damage

        # Combat results for player hit:
        # > Good luck: enemy takes 4 damage
        # > Normal   : enemy takes 2 damage
        # > Bad luck : enemy takes 1 damage

        # Combat results for enemy hit:
        # > Good luck: player takes 1 damage
        # > Normal   : player takes 2 damage
        # > Bad luck : player takes 3 damage

        if player_atk > enemy_atk:
            print "You hits the enemy"
            userinput = raw_input("Use your luck to amplify damage? [Y/N]")
            if (userinput == "Y") or (userinput == "y"):
                player_luck = player.testYourLuck()
                if player_luck == 'good':
                    print "Critical Hit! Enemy takes 4 damage."
                    enemy_energy -= 4
                elif player_luck == 'bad':
                    print "Your hit was just a scratch! Enemy takes 1 damage."
                    enemy_energy -= 1
            else:
                print "Enemy takes 2 damage."
                enemy_energy -= 2
            print "Enemy now have " + str(enemy_energy) + " energy left."
        elif (player_atk < enemy_atk):
            print enemy_name + " hits you."
            userinput = raw_input("Use your luck to minimize the wounds? [Y/N]")
            if (userinput == "Y") or (userinput == "y"):
                player_luck = player.testYourLuck()
                if player_luck == 'good':
                    print "Was just a scratch. You take 1 damage."
                    player.setEnergy(-1)
                elif player_luck == 'bad':
                    print "That's gonna hurt! You take 3 damage."
                    player.setEnergy(-3)
            else:
                print "You take 2 damage."
                player.setEnergy(-2)
            print "You now have " + str(player.getEnergy()) + " energy left."
        elif player_atk == enemy_atk:
            print "You evaded the " + enemy_name + " attack."
        print ""

        # Checks if the player or enemy have died
        # Ask if the player want to flee
        if player.getEnergy() <= 0:
            print "You have perished! Game over!"
            combat_inProgress = False
            userinput = raw_input("-- Press enter to continue.")
            print ""
        elif enemy_energy <= 0:
            print "You killed " + enemy_name + ". You win!"
            combat_inProgress = False
            userinput = raw_input("-- Press enter to continue.")
            print ""
        else:
            print "-- Press enter to continue."
            print "-- Or type 'R' and press enter to run from the current combat."
            userinput = raw_input("-- You will take 2 point of damage if you run from this combat.")
            if (userinput == "R") or (userinput == "r"):
                combat_inProgress = False
                player.setEnergy(-2)
            print ""
    return 0
