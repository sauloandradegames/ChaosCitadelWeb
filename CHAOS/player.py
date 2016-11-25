# player.py
# Class Player: define a player

from CHAOS.dice import *

class Player:
    def __init__(self, name, maxEnergy=0, maxSkill=0, maxMagic=0, maxLuck=0, backpack=[], scroll=[], armor=None, weapon=None, offhand=None, gold=0):
        # Player's attributes:
        # Name: player's name
        # Energy: player's life
        # Skill: player's combat power. Defines whenever the player hits a enemy
        # Magic: player's arcane skills. Defines how much scrolls the player can carry at the beggining of the adventure
        # Luck: player's luck. Defines how fortunate the player is
        # Gold: player's spoils
        # Backpack: player's bag of holding. Which items the player is carring with him/her
        # Scrolls: all the player scrolls
        # Armor: Player current equipped armor
        # Weapon: Player current equipped weapon
        # Offhand: Player current equipped offhand (e.g shield)
        self.name = name
        self.maxEnergy = maxEnergy
        self.maxSkill = maxSkill
        self.maxMagic = maxMagic
        self.maxLuck = maxLuck

        self.energy = maxEnergy
        self.skill = maxSkill
        self.magic = maxMagic
        self.luck = maxLuck

        self.gold = gold
        self.backpack = backpack
        self.scroll = scroll
        self.armor = armor
        self.weapon = weapon
        self.offhand = offhand

    # ============================================
    # =================== GETS ===================
    # ============================================
    def getName(self):
        """ Return player's name """
        return self.name

    def getMaxEnergy(self):
        """ Return player's max energy """
        return self.maxEnergy

    def getMaxSkill(self):
        """ Return player's max skill """
        return self.maxSkill

    def getMaxMagic(self):
        """ Return player's max magic """
        return self.maxMagic

    def getMaxLuck(self):
        """ Return player's max luck """
        return self.maxLuck

    def getEnergy(self):
        """ Return player's current energy """
        return self.energy

    def getSkill(self):
        """ Return player's current skill """
        return self.skill

    def getMagic(self):
        """ Return player's current magic """
        return self.magic

    def getLuck(self):
        """ Return player's current luck """
        return self.luck

    def getGold(self):
        """ Return player's current gold """
        return self.gold

    def getBackpack(self):
        """ Return player's backpack """
        return self.backpack

    def getScroll(self):
        """ Return player's scrolls """
        return self.scroll

    def getArmor(self):
        """ Return player's equipped armor """
        return self.armor

    def getWeapon(self):
        """ Return player's equipped weapon """
        return self.weapon

    def getOffhand(self):
        """ Return player's equipped offhand """
        return self.offhand

    # ============================================
    # =================== SETS ===================
    # ============================================

    def setName(self, name):
        """ Set/changes value for player name """
        self.name = name

    def setMaxEnergy(self, ammo):
        """ Add/remove ammo from maxEnergy """
        self.maxEnergy += ammo
        if self.maxEnergy < 0:
            self.maxEnergy = 0

    def setMaxSkill(self, ammo):
        """ Add/remove ammo from maxSkill """
        self.maxSkill += ammo
        if self.maxSkill < 0:
            self.maxSkill = 0

    def setMaxMagic(self, ammo):
        """ Add/remove ammo from maxMagic """
        self.maxMagic += ammo
        if self.maxMagic < 0:
            self.maxMagic = 0

    def setMaxLuck(self, ammo):
        """ Add/remove ammo from maxLuck """
        self.maxLuck += ammo
        if self.maxLuck < 0:
            self.maxLuck = 0

    def setEnergy(self, ammo):
        """ Add/remove ammo from current energy """
        self.energy += ammo
        if self.energy > self.maxEnergy:
            self.energy = self.maxEnergy
        if self.energy < 0:
            self.energy = 0

    def setSkill(self, ammo):
        """ Add/remove ammo from current skill """
        self.skill += ammo
        if self.skill > self.maxSkill:
            self.skill = self.maxSkill
        if self.skill < 0:
            self.skill = 0

    def setMagic(self, ammo):
        """ Add/remove ammo from current magic """
        self.magic += ammo
        if self.magic > self.maxMagic:
            self.magic = self.maxMagic
        if self.magic < 0:
            self.magic = 0

    def setLuck(self, ammo):
        """ Add/remove ammo from current luck """
        self.luck += ammo
        if self.luck > self.maxLuck:
            self.luck = self.maxLuck
        if self.luck < 0:
            self.luck = 0

    def setGold(self, ammo):
        """ Add/remove ammo from current gold """
        self.gold += ammo
        if self.gold < 0:
            self.gold = 0

    def equipArmor(self, armor=None):
        """ Equip player with armor """
        if armor:
            self.armor = armor

    def equipWeapon(self, weapon=None):
        """ Equip player with weapon """
        if weapon:
            self.weapon = weapon

    def equipOffhand(self, offhand=None):
        """ Equip player with offhand """
        if offhand:
            self.offhand = offhand

    def putOnBackpack(self, item):
        """ Insert item on the backpack """
        self.backpack.append(item)

    def takeFromBackpack(self, item):
        """ Remove item on the backpack """
        if item in self.backpack:
            self.backpack.remove(item)

    def addScroll(self, scroll):
        """ Add a scroll """
        self.scroll.append(scroll)

    def useScroll(self, scroll):
        """ Use a scroll """
        if scroll in self.scroll:
            self.scroll.remove(scroll)

    # ============================================
    # ============== DICE FUNCTIONS ==============
    # ============================================

    def testYourLuck(self):
        """ Perform a TestYourLuck roll. Return 'good' or 'bad' """
        # Rules for 'Test Your Luck':
        # Pay 1 luck point. Roll 2d6
        # roll <  player_luck: Good luck
        # roll >= player_luck: Bad luck
        d6 = Dice(6)
        luck_result = d6.multiRoll(2)
        if luck_result < self.luck:
            self.luck -= 1
            if (self.luck < 0):
                self.luck = 0
            return 'good'
        elif luck_result >= self.luck:
            self.luck -= 1
            if (self.luck < 0):
                self.luck = 0
            return 'bad'
