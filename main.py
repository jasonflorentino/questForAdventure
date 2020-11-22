#! Python3
# main.py - Runs the main game program

from time import sleep

from resources import gameplay_functions as gpf
# from mainFunc import mainMenu
# from mainFunc import main

TITLE = """
  Q U E S T  F O R  A D V E N T U R E  
=======================================

"""
GOODBYE = "Farewell, adventure seeker.\n"

if __name__ == '__main__':
    while True:
        gpf.write(TITLE)      # Prints game title to screen
        game = gpf.mainMenu()   # Returns Game object or False if user quits
        play = gpf.playGame(game)   # Run game using Game object. Returns Ture if user plays again, False if user quits
        if not play:
            gpf.write(GOODBYE)
            sleep(1)
            break