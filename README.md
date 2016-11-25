# Chaos Citadel Web

This is the repository of "Chaos Citadel Web" project. The main objective of this project is to create a web-version of "The Citadel of Chaos" gamebook.

At the beginning, this project only contains a character sheet. The program will run on a unix terminal. Later, the same character sheet will be a web application. In this stage, it's only possible to play the game if the player have the book, but the player can use the app to register the character stats, instead of use pen, paper and a dice.

Later, the app will have the full game experience.

## Project structure

This is the repository structure:

```
+CHAOS
+bin
+old_project
+templates
|--assets
+tests
README.md
setup.py
```

- */CHAOS:* project main folder. Contains the core scripts
- */bin:* project binary folder. Contains necessary scripts for the web application
- */old_project:* temporary folder. Contains the alpha stage of the terminal aplication
- */templates:* html templates folder. Contains html files for the web aplication
- */templates/assets:* css folder. Contains css files and other media assets (e.g images)
- */tests:* unit tests folder. Contains unit test cases.
- *README.md:* this file
- *setup.py:* configuration and instalation file

## Workstation enviroment

At the moment:

- Any text editor (Atom recomended)
- Any web browser (Most of the time, Chrome)
- Python 2.7
- Nosetests
- Virtual Env
- Distutils
