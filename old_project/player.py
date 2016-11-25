#player.py
#Class Player - Manages player status

import random

class Player:
	def __init__(self, name, maxEnergy, maxSkill, maxMagic, maxLuck, scroll, gold=0):
		self.name = name           # Player's name
		self.maxEnergy = maxEnergy # Player's max life
		self.maxSkill = maxSkill   # Player's max combat skill
		self.maxMagic = maxMagic   # Player's max num. of scrolls
		self.maxLuck = maxLuck     # Player's max luck

		self.currEnergy = self.maxEnergy # Player's current life
		self.currSkill = self.maxSkill   # Player's current combat skill
		self.currLuck = self.maxLuck     # Player's current luck

		self.gold = gold     # Player's current ammount of gold
		self.backpack = []   # Player's backpack
		self.scroll = scroll     # Player's scrolls
		self.equipment = PlayerEquipment()  # Player's equipped items

	def getName(self):
		"""Return player's name"""
		return self.name

	def getMaxEnergy(self):
		"""Return player's max life"""
		return self.maxEnergy

	def getMaxSkill(self):
		"""Return player's max combat skill"""
		return self.maxSkill

	def getMaxMagic(self):
		"""Return player's max arcane skill"""
		return self.maxMagic

	def getMaxLuck(self):
		"""Return player's max luck"""
		return self.maxLuck

	def getCurrEnergy(self):
		"""Return player's current life"""
		return self.currEnergy

	def getCurrSkill(self):
		"""Return player's current combat skill"""
		return self.currSkill

	def getCurrLuck(self):
		"""Return player's current luck"""
		return self.currLuck

	def getGold(self):
		"""Return player's current ammount of gold"""
		return self.gold

	def getBackpack(self):
		"""Return player's backpack"""
		return self.backpack

	def getEquipment(self):
		"""Return player's equipment"""
		return self.equipment

	def getScroll(self):
		"""Return player's list of scrolls"""
		return self.scroll

	def setMaxEnergy(self, ammo):
		"""Set the player's max life"""
		# ammo: ammount of energy to increase/decrease
		self.maxEnergy += ammo

	def setMaxSkill(self, ammo):
		"""Set the player's max combat skill"""
		# ammo: ammount of skill to increase/decrease
		self.maxSkill += ammo

	def setMaxMagic(self, ammo):
		"""Set the player's max arcane skill"""
		# ammo: ammount of magic to increase/decrease
		self.maxMagic += ammo

	def setEnergy(self, damage):
		"""Set the player's current life"""
		# damage: indicate how much life to add/dec
		# negative damage ==> damage the player
		# positive damage ==> heals the player
		self.currEnergy += damage
		if (self.currEnergy > self.maxEnergy):
			self.currEnergy = self.maxEnergy
		if (self.currEnergy < 0):
			self.currEnergy = 0

	def setSkill(self, ammo):
		"""Set the player's current combat skill"""
		# ammo: ammount of skill to increase/decrease
		self.currSkill += ammo
		if (self.currSkill > self.maxSkill):
			self.currSkill = self.maxSkill
		if (self.currSkill < 0):
			self.currSkill = 0

	def setMagic(self, ammo):
		"""Set the player's current arcane skill"""
		# ammo: ammount of magic to increase/decrease
		self.currMagic += ammo
		if (self.currMagic > self.maxMagic):
			self.currMagic = self.maxMagic
		if (self.currMagic < 0):
			self.currMagic = 0

	def setLuck(self, ammo):
		"""Set the player's current luck"""
		# ammo: ammount of luck to increase/decrease
		self.currLuck += ammo
		if (self.currLuck > self.maxLuck):
			self.currLuck = self.maxLuck
		if (self.currLuck < 0):
			self.currLuck = 0

	def setGold(self, ammo):
		"""Set the player's gold"""
		# ammo: ammount of gold to add/remove
		self.gold += ammo

	def putInBackpack(self, item):
		"""Add item to the player's backpack"""
		self.backpack.append(item)

	def printCharacterStatsLess(self):
		"""Print a short table containing only character stats (short form)"""
		print "=================="
		print "| " + self.getName()
		print "| EN : " + str(self.getCurrEnergy())
		print "| SK : " + str(self.getCurrSkill())
		print "| LK : " + str(self.getCurrLuck())
		print "| $$ : " + str(self.getGold())
		print "=================="

	def printCharacterStats(self):
		"""Print a short table containing character stats (full form)"""
		print "=================="
		print "| NAME: " + self.getName()
		print "=================="
		print "| ENERGY : " + str(self.getCurrEnergy()) + "/" + str(self.getMaxEnergy())
		print "| SKILL  : " + str(self.getCurrSkill()) + "/" + str(self.getMaxSkill())
		print "| LUCK   : " + str(self.getCurrLuck()) + "/" + str(self.getMaxLuck())
		print "=================="
		print "| GOLD   : " + str(self.getGold())
		print "=================="

	def printCharacterEquip(self):
		"""Prints a short table containing the character equipment"""
		print "=================="
		print "| EQUIPMENT:"
		print "| " + self.getEquipment().getArmor()
		print "| " + self.getEquipment().getWeapon()
		print "| " + self.getEquipment().getOffhand()
		print "=================="

	def printCharacterBackpack(self):
		"""Prints a short table containing the character inventory"""
		print "=================="
		print "| BACKPACK:"
		for item in self.getBackpack():
			print "| " + item
		print "=================="

	def printCharacterScroll(self):
		"""Prints a short table containing the character scrolls"""
		print "=================="
		print "| SCROLLS:"
		if (self.getScroll().count("energy") != 0):
			print "| Restore Energy : " + str(self.getScroll().count("energy"))
		if (self.getScroll().count("skill") != 0):
			print "| Restore Skill : " + str(self.getScroll().count("skill"))
		if (self.getScroll().count("luck") != 0):
			print "| Restore Luck : " + str(self.getScroll().count("luck"))
		if (self.getScroll().count("copycat") != 0):
			print "| Mirror Image : " + str(self.getScroll().count("copycat"))
		if (self.getScroll().count("perception") != 0):
			print "| Perception : " + str(self.getScroll().count("perception"))
		if (self.getScroll().count("fire") != 0):
			print "| Fire : " + str(self.getScroll().count("fire"))
		if (self.getScroll().count("fakegold") != 0):
			print "| Fool's Gold : " + str(self.getScroll().count("fakegold"))
		if (self.getScroll().count("illusion") != 0):
			print "| Illusion : " + str(self.getScroll().count("illusion"))
		if (self.getScroll().count("levitate") != 0):
			print "| Levitate : " + str(self.getScroll().count("levitate"))
		if (self.getScroll().count("shield") != 0):
			print "| Shield : " + str(self.getScroll().count("shield"))
		if (self.getScroll().count("strength") != 0):
			print "| Strength : " + str(self.getScroll().count("strength"))
		if (self.getScroll().count("weakness") != 0):
			print "| Weakness : " + str(self.getScroll().count("weakness"))
		print "=================="

	def printCharacter(self):
		"""Print a table containing all the character information"""
		self.printCharacterStats()
		self.printCharacterEquip()
		self.printCharacterBackpack()
		self.printCharacterScroll()

	#def takeFromBackpack(self, item):
		# Take item from backpack (if exists)
	#TODO: define a function to take items from backpack

class PlayerEquipment:
	def __init__(self):
		self.armor = ""
		self.weapon = ""
		self.offhand = ""

	def getArmor(self):
		"""Return player equipped armor"""
		return self.armor

	def getWeapon(self):
		"""Return player equipped weapon"""
		return self.weapon

	def getOffhand(self):
		"""Return player equipped offhand"""
		return self.offhand

	def setArmor(self, armor):
		"""Equip player with an armor"""
		self.armor = armor

	def setWeapon(self, weapon):
		"""Equip player with a weapon"""
		self.weapon = weapon

	def setOffhand(self, offhand):
		"""Equip player with an offhand"""
		self.offhand = offhand
