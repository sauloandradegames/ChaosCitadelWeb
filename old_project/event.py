#event.py
#Class Event - manage game events

class NormalEvent:
	def __init__(self, id, isFinalState, description, path):
		"""Defines a normal event"""
		self.id = id # event's id
		self.isFinalState = isFinalState # it's the last event of the game?
		self.description = description # event's description
		self.path = path # possible routes

	def getId(self):
		"""Return the event id"""
		return self.id

	def getIsFinalState(self):
		"""Return if the event ends the game or not"""
		return self.isFinalState

	def getDescription(self):
		"""Return the event description"""
		return self.description

	def getPath(self):
		"""Return the list of possible routes available from this one"""
		return self.path

class CombatEvent:
	def __init__(self, id, monsters):
		"""Defines a combat event"""
		self.id = id # event's id
		self.monsters = monsters # list of tuple (mon_name, mon_energy, mon_skill)

	def getId(self):
		"""Return the event id"""
		return self.id

	def getMonsters(self):
		"""Return the list of monsters"""
		return self.monsters