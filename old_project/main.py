#main.py
#Main program

#TODO: Criar lista de todos os itens do jogo
#TODO: Criar menu de historia
#TODO: Integrar menu de historia com menu de combate
#TODO: Adicionar bonus para dado de ataque
#TODO: Adicionar opcao para cancelar combate
#TODO: Adicionar tratamento de excecoes

import event
import player
import combat
import editor
import pickle
import os

def game(currentplayer):
	"""Runs the game"""
	ingame = True
	userinput = -1

	while (ingame):
		os.system("clear")
		currentplayer.printCharacterStatsLess()
		print("=== GAME MENU ===")
		print("1. Set player energy")
		print("2. Set player skill")
		print("3. Set player luck")
		print("4. Set player gold")
		print("5. Equipment management")
		print("6. Backpack management")
		print("7. Scrolls management")
		print("8. Start a fight")
		print("9. Player status")
		print("0. End game")
		userinput = raw_input("> ")

		if (int(userinput) == 1):
			damage = raw_input("> Energy Damage = ")
			currentplayer.setEnergy(int(damage))
		elif (int(userinput) == 2):
			damage = raw_input("> Skill Damage = ")
			currentplayer.setSkill(int(damage))
		elif (int(userinput) == 3):
			damage = raw_input("> Luck Damage = ")
			currentplayer.setLuck(int(damage))
		elif (int(userinput) == 4):
			loot = raw_input("> Loot value = ")
			currentplayer.setGold(int(loot))
		elif (int(userinput) == 5):
			os.system("clear")
			currentplayer.printCharacterEquip()
			item = raw_input("> Equip what?  ")
			print("> Where?")
			print("> 1. Armor")
			print("> 2. Weapon")
			print("> 3. OffHand")
			userinput = raw_input("> ")
			if (int(userinput) == 1):
				currentplayer.equipment.setArmor(item)
			elif (int(userinput) == 2):
				currentplayer.equipment.setWeapon(item)
			elif (int(userinput) == 3):
				currentplayer.equipment.setOffhand(item)
			os.system("clear")
			currentplayer.printCharacterEquip()
			print "> " + item + " equipped."
			userinput = raw_input("-- Press enter to continue.")
		elif (int(userinput) == 6):
			os.system("clear")
			currentplayer.printCharacterBackpack()
			print("> What?")
			print("1. Put an item")
			print("2. Take an item")
			userinput = raw_input("> ")
			item = raw_input("> Which item? ")
			if (int(userinput) == 1):
				currentplayer.backpack.append(item)
				os.system("clear")
				currentplayer.printCharacterBackpack()
				print "> " + item + " added."
				userinput = raw_input("-- Press enter to continue.")
			elif (int(userinput) == 2):
				currentplayer.backpack.remove(item)
				os.system("clear")
				currentplayer.printCharacterBackpack()
				print "> " + item + " removed."
				userinput = raw_input("-- Press enter to continue.")
		elif (int(userinput) == 7):
			os.system("clear")
			currentplayer.printCharacterScroll()
			print("> Choose an option: ")
			print("1. Use scroll")
			print("2. Add scroll")
			userinput = raw_input("> ")
			print("> Type the name of the scroll")
			print("> 'energy', 'skill', 'luck', 'copycat', 'perception', 'fire', 'fakegold', 'illusion', 'levitate', 'shield', 'strength', 'weakness'")
			scroll = raw_input("> ")
			if (int(userinput) == 1):
				currentplayer.scroll.remove(scroll)
				os.system("clear")
				currentplayer.printCharacterScroll()
				print"> Scroll used."
				userinput = raw_input("-- Press enter to continue.")
			elif (int(userinput) == 2):
				currentplayer.scroll.append(scroll)
				os.system("clear")
				currentplayer.printCharacterScroll()
				print"> Scroll added."
				userinput = raw_input("-- Press enter to continue.")
		elif (int(userinput) == 8):
			os.system("clear")
			enemy_name = raw_input("> Enemy Name: ")
			enemy_hp = raw_input("> Enemy Energy: ")
			enemy_skill = raw_input("> Enemy Skill: ")
			combat.combatScreen(currentplayer, (enemy_name, int(enemy_hp), int(enemy_skill)))
		elif (int(userinput) == 9):
			os.system("clear")
			currentplayer.printCharacter()
			userinput = raw_input("-- Press enter to continue.")
		elif (int(userinput) == 0):
			ingame = False

#===============================================================

character = None
running = True

while (running):
	os.system("clear")
	print("=== THE CITADEL OF CHAOS - PLAYER MANAGER ===")
	print("1. Start a new adventure")
	print("2. Exit to Terminal")
	userinput = raw_input("> ")

	if (userinput == "1"):
		character = editor.createCharacter()
		game(character)
	elif (userinput == "2"):
		running = False

#e1 = editor.createEvent()
#print e1
#editor.saveEvent(e1, "event_testificate.pkl")

#e2 = editor.createEvent()
#print e2
#editor.saveEvent(e2, "event_testificate.pkl")

#playerfilename = "players.pkl"

#p1 = editor.createCharacter()

#with open(playerfilename, "rb") as f:
#	p1 = pickle.load(f)
#	p2 = pickle.load(f)

#p1.printCharacterShort()

#p2.printCharacter()

#p2 = player.Player("Avestruz", 15, 10, 10, 5, [])
#game(p2)
#p2.printCharacter()

#s = editor.initializeStory("testificate.txt", "combat_testificate.txt")
