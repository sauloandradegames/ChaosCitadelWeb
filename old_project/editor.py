#editor.py
#Manages game customization (CRUD)

#TODO: Modificar initializeStory para oferecer suporte a Pickle

import combat
import player
import pickle
import os

def createCharacter():
	"""Menu function: generates a new character"""
	name = ""
	energy = 0
	skill = 0
	magic = 0
	luck = 0
	scroll = []

	currmagic = 0

	isConfirmed = False
	userinput = 0

	while (not isConfirmed):
		os.system("clear")
		energy = combat.rollDice() + combat.rollDice() + 12
		skill = combat.rollDice() + 6
		magic = combat.rollDice() + combat.rollDice() + 6
		luck = combat.rollDice() + 6

		print "Energy: " + str(energy) + " (Your Max HP)"
		print "Skill : " + str(skill) + " (Your Atk power)"
		print "Magic : " + str(magic)
		print "Luck  : " + str(luck)

		userinput = raw_input("Do you wish to mantain these stats? [Y/N] ")

		if (userinput == "Y") or (userinput == "y"):
			isConfirmed = True

	currmagic = magic
	isConfirmed = False

	while (not isConfirmed):
		os.system("clear")
		print "Choose with scrolls you wish to carry onto the dungeon."
		print "Available scrolls: " + str(currmagic)
		print "+---+-------------------------------+"
		print "| A | Scroll of Restore Energy | " + str(scroll.count("energy")) + " |"
		print "| B | Scroll of Restore Skill  | " + str(scroll.count("skill")) + " |"
		print "| C | Scroll of Restore Luck   | " + str(scroll.count("luck")) + " |"
		print "+---+-------------------------------+"
		print "| D | Scroll of Mirror Image   | " + str(scroll.count("copycat")) + " |"
		print "| E | Scroll of Perception     | " + str(scroll.count("perception")) + " |"
		print "| F | Scroll of Fire           | " + str(scroll.count("fire")) + " |"
		print "| G | Scroll of Fool's Gold    | " + str(scroll.count("fakegold")) + " |"
		print "| H | Scroll of Illusion       | " + str(scroll.count("illusion")) + " |"
		print "| I | Scroll of Levitate       | " + str(scroll.count("levitate")) + " |"
		print "| J | Scroll of Shield         | " + str(scroll.count("shield")) + " |"
		print "| K | Scroll of Strength       | " + str(scroll.count("strength")) + " |"
		print "| L | Scroll of Weakness       | " + str(scroll.count("weakness")) + " |"
		print "+---+-------------------------------+"

		if (currmagic > 0):
			userinput = raw_input("Type a letter for a scroll: ")
			if (userinput == "A") or (userinput == "a"):
				scroll.append("energy")
				currmagic -= 1
			elif (userinput == "B") or (userinput == "b"):
				scroll.append("skill")
				currmagic -= 1
			elif (userinput == "C") or (userinput == "c"):
				scroll.append("luck")
				currmagic -= 1
			elif (userinput == "D") or (userinput == "d"):
				scroll.append("copycat")
				currmagic -= 1
			elif (userinput == "E") or (userinput == "e"):
				scroll.append("perception")
				currmagic -= 1
			elif (userinput == "F") or (userinput == "f"):
				scroll.append("fire")
				currmagic -= 1
			elif (userinput == "G") or (userinput == "g"):
				scroll.append("fakegold")
				currmagic -= 1
			elif (userinput == "H") or (userinput == "h"):
				scroll.append("illusion")
				currmagic -= 1
			elif (userinput == "I") or (userinput == "i"):
				scroll.append("levitate")
				currmagic -= 1
			elif (userinput == "J") or (userinput == "j"):
				scroll.append("shield")
				currmagic -= 1
			elif (userinput == "K") or (userinput == "k"):
				scroll.append("strength")
				currmagic -= 1
			elif (userinput == "L") or (userinput == "l"):
				scroll.append("weakness")
				currmagic -= 1
		else:
			userinput = raw_input("Is that ok? [Y/N] ")
			if (userinput == "Y") or (userinput == "y"):
				isConfirmed = True
			else:
				currmagic = magic
				scroll = []

	name = raw_input("Type a name for your character: ")
	return player.Player(name, energy, skill, magic, luck, scroll)

def createEvent():
	"""Menu Function: generates a new event and return it."""
	event_id = ""
	event_isFinalState = ""
	event_description = ""

	event_path = []
	path_id = ""
	path_description = ""

	addpath = True

	event_id = raw_input("Event ID: ")
	userinput = raw_input("Finishes the game in this event? [Y/N]: ")
	if (userinput == "Y") or (userinput == "y"):
		event_isFinalState = True
	else:
		event_isFinalState = False
	event_description = raw_input("Type the description of the event:\n")

	while (addpath):
		print "=== Creating Paths ==="
		path_id = raw_input("= Go to event: ")
		path_description = raw_input("= Type the description of this path:\n")
		userinput = raw_input("Create another path? [Y/N]: ")
		event_path.append((int(path_id), path_description))
		if (userinput == "N") or (userinput == "n"):
			addpath = False

	return (int(event_id), event_isFinalState, event_description, event_path)

def saveEvent(storyobj, storyfile):
	"""Save the storyobj on the storyfile"""
	with open(storyfile, "a") as f:
		pickle.dump(storyobj, f)

def initializeStory(storyfile, combatfile):
	"""Loads the game story and combats from the text files"""
	story = [] # List of normal events
	combat = [] # List of combat events

	event_id = 0 # Id of the current event
	event_description = " " # Description of the current event

	path = [] # Path of the current normal event
	path_nextid = 0 # Id of the next event
	path_description = " " # Description of the path option

	enemies = [] # List of enemies of the current combat event
	enemy_name = "" # Enemy's name
	enemy_energy = 0 # Enemy's energy
	enemy_skill = 0 # Enemy's skill

	# Read the story file and generate the story
	with open(storyfile) as textfile:
		for line in textfile:
			if (line[0] == "!"):
				event_id = int(line[1:4])
				event_description = line[5:-1]
			elif (line[0] == "-"):
				path_nextid = int(line[1:4])
				path_description = line[5:-1]
				path.append((path_nextid, path_description))
			elif (line[0] == "+"):
				story.append((event_id, event_description, 	path))
				path = []

	with open(combatfile) as textfile:
		for line in textfile:
			if (line[0] == "!"):
				event_id = int(line[1:4])
				event_description = line[5:-1]
			elif (line[0] == "-"):
				enemy_name = line[1:-9]
				enemy_energy = line[-8:-5]
				enemy_skill = line[-4:-1]
				enemies.append((enemy_name, enemy_energy, enemy_skill))
			elif (line[0] == "+"):
				combat.append((event_id, enemies))
				enemies = []

	return [story, combat]
