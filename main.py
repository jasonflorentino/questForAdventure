#! Python3
# main.py - Runs the main game program

from time import sleep

from resources import Game
from resources import parseUserInput

title = """
  Q U E S T  F O R  A D V E N T U R E  
=======================================

"""
goodbye = "Farewell, adventure seeker.\n"

def display(text):
    for letter in text:
        print(letter, end='', flush=True)
        sleep(.02)

def getMenuInput():
    choice = ""
    while True:
        choice = input("> ").lower()
        if choice in ("n", "q"):
            break
        else:
            print("Please enter a valid input.")
            continue
    return choice

def mainMenu():
    print("     -- (N)ew / (Q)uit --\n")
    choice = getMenuInput()
    if choice == "q":
        return False
    elif choice == "n":
        game = Game("New")
        return game
    else:
        return True

def main(game):
    if game == False:
        return False
    userInput = ""
    while True:
        userinput = parseUserInput(input("> ").lower())
        if userinput == "quit":
            break
        else:
            continue
    return True

if __name__ == '__main__':
    while True:
        display(title)      # Prints game title to screen
        game = mainMenu()   # Returns Game object or False if user quits
        play = main(game)   # Run game using Game object. Returns Ture if user plays again, False if user quits
        if play == False:
            display(goodbye)
            break