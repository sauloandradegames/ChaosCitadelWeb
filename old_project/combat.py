#combat.py
#Manages combat system

#TODO: Save state, rolagem de sorte, bonus de arma
#| NAME: YT Last room: 112
#==================
#| ENERGY : 15/21
#| SKILL  : 8/8
#| LUCK   : 9/11
#==================
#| GOLD   : 0
#==================
#==================
#| EQUIPMENT:
#|
#| Espada Magica +1
#|
#==================
#
#==================
#| BACKPACK:
#| Espelho de Prata
#==================
#==================
#| SCROLLS:
#| Restore Energy : 3
#| Restore Skill : 1
#| Restore Luck : 1
#| Mirror Image : 1
#| Perception : 1
#| Fool's Gold : 1
#==================

import player
import random
import os

def combatScreen(player, enemy):
	"""Implement the game's combat screen"""
	# player: reference from a player object
	# enemy: a tuple (str enemy_name, int enemy_hp, int enemy_skill)
	player_dice = 0 # result for player dice
	player_luckdice = 0 # result for player dice (TestYourLuck)
	enemy_dice = 0 # result for enemy dice
	enemy_name = enemy[0] # get enemy name from input
	enemy_energy = enemy[1] # get enemy life from input
	enemy_skill = enemy[2] # get enemy combat skill from input
	combat_inProgress = True # is the combat still in progress

	while (combat_inProgress):
		os.system("clear")
		print "Player: [EN: " + str(player.getCurrEnergy()) + "/" + str(player.getMaxEnergy()) + "] [SK: " + str(player.getCurrSkill()) + "] [LK: " + str(player.getCurrLuck()) + "]"
		print enemy_name + ": [EN: " + str(enemy_energy) + "] [SK: " + str(enemy_skill) + "]"

		# Roll two d6 for the player. Add the current player skill
		# Roll two d6 for the enemy. Add the current enemy skill
		player_dice = rollDice() + rollDice() + player.getCurrSkill()
		enemy_dice = rollDice() + rollDice() + enemy_skill

		print "PlayerDice: " + str(player_dice)
		print "Enemy Dice: " + str(enemy_dice)

		# These are the combat rules:
		# If player_dice > enemy_dice: Player hits.
		# - Player can throw a lucky dice to amplify the damage
		# If player_dice < enemy_dice: Enemy hits.
		# - Player can throw a lucky dice to reduce the damage
		# If player_dice = enemy_dice: Nobody hits
		# - Neither player nor enemy takes damage

		# When the player throws a lucky dice (TestYourLuck)
		# - Pay 1 luck point. Roll 2d6
		# - If player_dice < player_luck: Good luck
		# - If player_dice >= player_luck: Bad luck

		# Combat results for player hit:
		# - Good luck: enemy takes 4 damage
		# - Normal   : enemy takes 2 damage
		# - Bad luck : enemy takes 1 damage

		# Combat results for enemy hit:
		# - Good luck: player takes 1 damage
		# - Normal   : player takes 2 damage
		# - Bad luck : player takes 3 damage

		if (player_dice > enemy_dice):
			print "You hits the enemy."
			userinput = raw_input("Use your luck to amplify damage? [Y/N]")
			if (userinput == "Y") or (userinput == "y"):
				player_luckdice = rollDice() + rollDice()
				if (player_luckdice < player.getCurrLuck()):
					print "Critical Hit! Enemy takes 4 damage."
					enemy_energy -= 4
				else:
					print "Your hit was just a scratch! Enemy takes 1 damage."
					enemy_energy -= 1
				player.setLuck(-1)
			else:
				print "Enemy takes 2 damage."
				enemy_energy -= 2
			print "Enemy now have " + str(enemy_energy) + " energy left."
		elif (player_dice < enemy_dice):
			print "Enemy hits you."
			userinput = raw_input("Use your luck to minimize the wounds? [Y/N]")
			if (userinput == "Y") or (userinput == "y"):
				player_luckdice = rollDice() + rollDice()
				if (player_luckdice < player.getCurrLuck()):
					print "Was just a scratch. You take 1 damage."
					player.setEnergy(-1)
				else:
					print "That's gonna hurt! You take 3 damage."
					player.setEnergy(-3)
				player.setLuck(-1)
			else:
				print "You take 2 damage."
				player.setEnergy(-2)
			print "You now have " + str(player.getCurrEnergy()) + " energy left."
		elif (player_dice == enemy_dice):
			print "You evaded the enemy attack."

		# Resets all dices at the end of the turn
		player_dice = 0
		player_luckdice = 0
		enemy_dice = 0

		# Checks if player or enemy have died
		if (player.getCurrEnergy() <= 0):
			print "You have perished! Game Over!"
			combat_inProgress = False
		elif (enemy_energy <= 0):
			print "Enemy is dead. You win!"
			combat_inProgress = False
		userinput = raw_input("-- Press enter to continue.")
		print ""

def rollDice():
	"""Roll a d6"""
	return random.randint(1, 6)
