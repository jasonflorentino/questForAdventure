#! Python3
# main.py - Runs the main game program

from time import sleep

from mainFunc import write
from mainFunc import mainMenu
from mainFunc import main

title = """
  Q U E S T  F O R  A D V E N T U R E  
=======================================

"""
goodbye = "Farewell, adventure seeker.\n"

if __name__ == '__main__':
    while True:
        write(title)      # Prints game title to screen
        game = mainMenu()   # Returns Game object or False if user quits
        play = main(game)   # Run game using Game object. Returns Ture if user plays again, False if user quits
        if play == False:
            write(goodbye)
            sleep(1)
            break