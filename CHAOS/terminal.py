# terminal.py
# Runs the game in terminal mode

from CHAOS.menu import *

character = None
running = True
playing = False

while running:
    character = mainMenu()
    if character == None:
        playing = False
        running = True
    elif character == 'exit':
        playing = False
        running = False
    else:
        playing = True
        running = True
    while playing:
        playing = gameMenu(character)
