# menu.py
# Handles all the menu and print stuff

from CHAOS.player import *
from CHAOS.combat import *
from CHAOS.dice import *
from CHAOS.items import *
import os

def mainMenu():
    """ Prints the main menu """
    os.system("clear")
    print '{:=^80}'.format(" THE CITADEL OF CHAOS - ELETRONIC CHARACTER SHEET ")
    print "[1] Start a new adventure"
    print "[2] Load a previous game"
    print "[3] Exit to terminal"
    userinput = raw_input("> ")

    if userinput == '1':
        return characterCreationMenu()
    elif userinput == '2':
        # do some loading stuff
        pass
    elif userinput == '3':
        return 'exit'

def characterCreationMenu():
    """ Prints the character creation screen and generates a new character. """
    # New player attributes
    name = ""
    energy = 0
    skill = 0
    magic = 0
    luck = 0
    armor = ""
    weapon = ""
    offhand = ""
    scroll = []

    # For selecting scrolls
    currmagic = 0

    # The user accepts the new character stats / scrolls?
    confirmed = False

    # User input!
    userinput = ""

    # Dice for stats roll
    d6 = Dice(6)

    os.system("clear")
    print '{:=^80}'.format(" CREATING NEW CHARACTER - NAME ")
    print ""

    name = raw_input("What shall be your name? ")


    while not confirmed:
        os.system("clear")
        print '{:=^80}'.format(" CREATING NEW CHARACTER - STATS ")
        print ""

        energy = d6.multiRoll(2) + 12
        skill = d6.roll() + 6
        magic = d6.multiRoll(2) + 6
        luck = d6.roll() + 6

        print "Energy: " + str(energy) + " (Your Max HP)"
        print "Skill : " + str(skill) + " (Your attack power)"
        print "Magic : " + str(magic) + " (How much scrolls can you carry)"
        print "Luck  : " + str(luck) + " (How fortunate you are)"
        userinput = raw_input("Do you wish to keep these stats? [Y/N]")

        if userinput == "Y" or userinput == 'y':
            confirmed = True

    currmagic = magic
    confirmed = False

    while not confirmed:
        os.system("clear")
        print '{:=^80}'.format(" CREATING NEW CHARACTER - SCROLLS ")
        print ""

        print "Choose which scrolls you wish to carry onto the adventure:"
        print "Available scrolls: " + str(currmagic)
        print '{:=<80}'.format('')
        print "| A |" + '{:<69}'.format(" " + scroll_list['energy']+ " ") + '{:^4}'.format(str(scroll.count('energy')))
        print "| B |" + '{:<69}'.format(" " + scroll_list['skill']+ " ") + '{:^4}'.format(str(scroll.count('skill')))
        print "| C |" + '{:<69}'.format(" " + scroll_list['luck']+ " ") + '{:^4}'.format(str(scroll.count('luck')))
        print '{:=<80}'.format('')
        print "| D |" + '{:<69}'.format(" " + scroll_list['copycat']+ " ") + '{:^4}'.format(str(scroll.count('copycat')))
        print "| E |" + '{:<69}'.format(" " + scroll_list['perception']+ " ") + '{:^4}'.format(str(scroll.count('perception')))
        print "| F |" + '{:<69}'.format(" " + scroll_list['fire']+ " ") + '{:^4}'.format(str(scroll.count('fire')))
        print "| G |" + '{:<69}'.format(" " + scroll_list['fakegold']+ " ") + '{:^4}'.format(str(scroll.count('fakegold')))
        print "| H |" + '{:<69}'.format(" " + scroll_list['illusion']+ " ") + '{:^4}'.format(str(scroll.count('illusion')))
        print "| I |" + '{:<69}'.format(" " + scroll_list['levitate']+ " ") + '{:^4}'.format(str(scroll.count('levitate')))
        print "| J |" + '{:<69}'.format(" " + scroll_list['shield']+ " ") + '{:^4}'.format(str(scroll.count('shield')))
        print "| K |" + '{:<69}'.format(" " + scroll_list['strength']+ " ") + '{:^4}'.format(str(scroll.count('strength')))
        print "| L |" + '{:<69}'.format(" " + scroll_list['weakness']+ " ") + '{:^4}'.format(str(scroll.count('weakness')))
        print '{:=<80}'.format('')

        if currmagic > 0:
            userinput = raw_input("Type a letter for a scroll to add: ")
            if userinput == "A" or userinput == 'a':
                scroll.append('energy')
                currmagic -= 1
            elif userinput == "B" or userinput == 'b':
                scroll.append('skill')
                currmagic -= 1
            elif userinput == "C" or userinput == 'c':
                scroll.append('luck')
                currmagic -= 1
            elif userinput == "D" or userinput == 'd':
                scroll.append('copycat')
                currmagic -= 1
            elif userinput == "E" or userinput == 'e':
                scroll.append('perception')
                currmagic -= 1
            elif userinput == "F" or userinput == 'f':
                scroll.append('fire')
                currmagic -= 1
            elif userinput == "G" or userinput == 'g':
                scroll.append('fakegold')
                currmagic -= 1
            elif userinput == "H" or userinput == 'h':
                scroll.append('illusion')
                currmagic -= 1
            elif userinput == "I" or userinput == 'i':
                scroll.append('levitate')
                currmagic -= 1
            elif userinput == "J" or userinput == 'j':
                scroll.append('shield')
                currmagic -= 1
            elif userinput == "K" or userinput == 'k':
                scroll.append('strength')
                currmagic -= 1
            elif userinput == "L" or userinput == 'l':
                scroll.append('weakness')
                currmagic -= 1
        else:
            userinput = raw_input("Is that ok? [Y/N]")
            if userinput == "Y" or userinput == "y":
                confirmed = True
            else:
                currmagic = magic
                scroll = []


    os.system("clear")
    print '{:=^80}'.format(" CREATING NEW CHARACTER - STARTING EQUIPMENT ")
    print ""

    userinput = raw_input("Do you have any starting gear? [Y/N] ")
    if userinput == "Y" or userinput == "y":
        armor = raw_input("Which armor? ")
        weapon = raw_input("Which weapon? ")
        offhand = raw_input("Which offhand? ")

    newplayer = Player(name, energy, skill, magic, luck, [], scroll, armor, weapon, offhand)

    os.system("clear")
    print '{:=^80}'.format(" CREATING NEW CHARACTER - CONFIRM EVERYTHING ")
    print ""
    printCharacterSheet(newplayer)
    userinput = raw_input("It's everything ok? [Y/N]")

    if userinput == "Y" or userinput == "y":
        return newplayer
    else:
        return None

def gameMenu(player):
    """ Print the game menu on screen. Return if the game ends or not."""
    os.system("clear")

    printCharacterStats(player)
    print ""

    print '{:=^80}'.format(" GAME MENU ")
    print "[1] Set player stats"
    print "[2] Equipment management"
    print "[3] Backpack management"
    print "[4] Scroll management"
    print "[5] Start a fight"
    print "[6] Character status"
    print "[7] Roll dice"
    print "[8] Test your luck"
    print "[9] End game"
    userinput = raw_input("> ")

    if userinput == '1':   # Set player stats
        os.system("clear")

        printCharacterStats(player)
        print ""

        print '{:=^80}'.format(" SET PLAYER STATS ")
        print "Which stat do you want to change?"
        print "[1] Energy"
        print "[2] Skill"
        print "[3] Luck"
        print "[4] Gold"
        print "[5] Cancel"
        userinput = raw_input("> ")
        if userinput in ['1', '2', '3', '4']:
            print "How much?"
            print "Greater than zero: Add stat [42 => stat+42]"
            print "Less than zero: Subtract stat [-42 => stat-42]"
            ammo = raw_input("> ")

            if userinput == '1': # Energy
                player.setEnergy(int(ammo))
            elif userinput == '2': # Skill
                player.setSkill(int(ammo))
            elif userinput == '3': # Luck
                player.setLuck(int(ammo))
            elif userinput == '4': # Gold
                player.setGold(int(ammo))
    elif userinput == '2': # Equipment management
        os.system("clear")

        printCharacterEquipment(player)
        print ""

        print '{:=^80}'.format(" EQUIPMENT MANAGEMENT ")
        print "[1] Equip armor"
        print "[2] Equip weapon"
        print "[3] Equip offhand"
        print "[4] Cancel"
        userinput = raw_input("> ")

        if userinput in ['1', '2', '3']:
            new_item = raw_input("> Which item? ")
            if userinput == '1':
                player.equipArmor(new_item)
            elif userinput == '2':
                player.equipWeapon(new_item)
            elif userinput == '3':
                player.equipOffhand(new_item)
    elif userinput == '3': # Backpack management
        os.system("clear")

        printCharacterBackpack(player)
        print ""

        print '{:=^80}'.format(" BACKPACK MANAGEMENT ")
        print "[1] Put an item"
        print "[2] Take an item"
        print "[3] Cancel"
        userinput = raw_input("> ")

        if userinput in ['1', '2']:
            new_item = raw_input("> Which item? ")
            if userinput == '1':
                player.putOnBackpack(new_item)
            elif userinput == '2':
                player.takeFromBackpack(new_item)
    elif userinput == '4': # Scroll management
        os.system("clear")

        printCharacterScroll(player)
        print ""

        print '{:=^80}'.format(" SCROLL MANAGEMENT ")
        print "[1] Add new scroll"
        print "[2] Activate scroll"
        print "[3] Cancel"
        userinput = raw_input("> ")

        if userinput in ['1', '2']:
            new_scroll = raw_input("> Which scroll? ")
            if new_scroll in scroll_list:
                if userinput == '1':
                    player.addScroll(new_scroll)
                elif userinput == '2':
                    player.useScroll(new_scroll)
            else:
                print "> Invalid scroll."
                print "> These are valid scrolls: "
                print "> 'energy', 'skill', 'luck', copycat', 'perception' 'fire', 'fakegold', 'illusion', 'levitate', 'shield', 'strength', 'weakness'"
    elif userinput == '5': # Start a fight
        os.system("clear")

        print '{:=^80}'.format(" START A FIGHT ")

        enemy_name = raw_input("> Enemy name   : ")
        enemy_skill = raw_input("> Enemy skill  : ")
        enemy_energy = raw_input("> Enemy energy : ")
        combatScreen(player, (enemy_name, int(enemy_energy), int(enemy_skill)))
    elif userinput == '6': # Character status
        os.system("clear")

        printCharacterSheet(player)
        print ""

        userinput = raw_input("> Press enter to continue.")
    elif userinput == '7': # Roll dice
        os.system("clear")

        print '{:=^80}'.format(" ROLL DICE ")

        d6 = Dice(6)
        num_dices = raw_input("> How many dices? ")
        print ""

        print "[" + str(d6.multiRoll(int(num_dices))) + "]"
        print ""
        userinput = raw_input("> Press enter to continue.")
    elif userinput == '8': # Test your luck
        os.system("clear")

        print '{:=^80}'.format(" TEST YOUR LUCK ")

        result = player.testYourLuck()

        if result == 'good':
            print "You have GOOD luck!"
        elif result == 'bad':
            print "You have BAD  luck!"
        userinput = raw_input("> Press enter to continue.")
    elif userinput == '9': # End game
        os.system("clear")

        userinput = raw_input("> Do you wish to save your game? [Y/N]")

        if userinput == "Y" or userinput == "y":
            # do some save game stuff
            print "Game saved!"
            userinput = raw_input("> Press enter to continue.")
        return False
    return True

def printCharacterStats(player):
    """ Print character basic stats on screen """
    print '{:=<80}'.format('')
    print "|" + '{:^15}'.format(player.getName()) + "|" +  '{:^15}'.format("Energy: " + str(player.getEnergy()) + "/" + str(player.getMaxEnergy())) + "|" '{:^15}'.format("Skill: " + str(player.getSkill()) + "/" + str(player.getMaxSkill())) + "|" + '{:^15}'.format("Luck: " + str(player.getLuck()) + "/" + str(player.getMaxLuck())) + "|" + '{:^14}'.format("Gold: " + str(player.getGold())) + "|"
    print '{:=<80}'.format('')

def printCharacterEquipment(player):
    """ Print character equipment on screen """
    print '{:=<80}'.format('')
    print "|" + '{:^78}'.format("Equipment") + "|"
    print "|" + '{:<78}'.format(" Armor   : " + player.getArmor()) + "|"
    print "|" + '{:<78}'.format(" Weapon  : " + player.getWeapon()) + "|"
    print "|" + '{:<78}'.format(" Offhand : " + player.getOffhand()) + "|"
    print '{:=<80}'.format('')

def printCharacterBackpack(player):
    """ Print character backpack on screen """
    print '{:=<80}'.format('')
    print "|" + '{:^78}'.format("Backpack") + "|"
    for item in player.getBackpack():
        print "|" + '{:<78}'.format(" " + item) + "|"
    print '{:=<80}'.format('')

def printCharacterScroll(player):
    """ Print character scrolls on screen """
    print '{:=<80}'.format('')
    print "|" + '{:^78}'.format("Scrolls") + "|"
    for scroll in scroll_list:
        if player.getScroll().count(scroll) != 0:
            print "|" + '{:<78}'.format(" x" + str(player.getScroll().count(scroll)) + " " + scroll_list[scroll]) + "|"
    print '{:=<80}'.format('')

def printCharacterSheet(player):
    """ Print all character stats on screen """
    printCharacterStats(player)
    printCharacterEquipment(player)
    printCharacterBackpack(player)
    printCharacterScroll(player)
