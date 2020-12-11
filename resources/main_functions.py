#! Python3
# game_functions.py

from .game import Game
from .user_input import UserInput
from .util import write
from .response import Response
from .game_actions import *

def mainMenu():
    print("       -- (N)ew / (Q)uit --\n")
    choice = getMenuInput()
    if choice in ("q", "quit"):
        return False
    else:
        gameObject = Game("New")
        return gameObject

def getMenuInput():
    choice = ""
    while True:
        choice = input("> ").lower()
        if choice in ("n", "q", "new", "quit"):
            break
        else:
            print("Please enter a valid input.")
            continue
    return choice

def playGame(game):
    if game:
        while True:
            event = game.eventCheck()
            if event == "quit":
                break
            action = turn(game)
            if action == "quit":
                break
            game.incrementTurnCount()
            
        return False
    else:
        return False

def turn(game):
    command = UserInput()
    if command.isValid:
        response = execute(game, command) # game_actions.execute() => Response Object
        response.writeResponse()
        return response.gameStatus
    else:
        write("Try again.\n")
        return "next-turn"

