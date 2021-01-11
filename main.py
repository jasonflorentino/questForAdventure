#! Python3
# main.py - Runs the main game program

# automate tests by writing sequential commands in "test" and running: $ python3 main.py < test

from time import sleep

from resources import util
from resources import main_functions as func

TITLE = """
  Q U E S T  F O R  A D V E N T U R E  
=======================================

"""
GOODBYE = "Farewell, adventure seeker.\n"

if __name__ == '__main__':
    while True:
        util.write(TITLE)      # Prints game title to screen
        game = func.mainMenu()   # Returns Game object or False if user quits
        play = func.playGame(game)   # Run game using Game object. Returns Ture if user plays again, False if user quits
        if not play:
            sleep(1)
            util.write(GOODBYE)
            sleep(1)
            break