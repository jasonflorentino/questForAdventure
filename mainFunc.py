#! Python3
# mainFunc.py - functions called from the main game file

from time import sleep

from resources import Game
import player
from userInput import UserInput

def write(text):
    for letter in text:
        print(letter, end='', flush=True)
        # sleep(.02) # Uncomment for slow printing

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

def mainMenu():
    print("       -- (N)ew / (Q)uit --\n")
    choice = getMenuInput()
    if choice in ("q", "quit"):
        return False
    else:
        game = Game("New")
        return game

print(mainMenu())

def main(game):
    if game == False:
        return False
    action = ""
    while True:
        # print('Turn Count: ' + str(game.turnCount)) # DEBUG
        # print("Current Location: " + game.currentLocation.name)  # DEBUG
        # print(game.currentLocation.contents) # DEBUG
        if game.turnCount == 0:
            game.beginning()
        action = turn(game)     # THE TURN
        game.turnCount += 1
        if action == "quit":
            break
        else:
            pass
    return True

def turn(game):
    newInput = UserInput()
    newInput.asssignCmds(newInput.getInput())
    turnAction = validateInput(game, newInput)
    # print(f"user input: {turnAction} - turn()")    # DEBUG
    print()
    if turnAction == "invalid":
        notAValidAction()
    else:
        turnAction = game.directInput(turnAction)
    return turnAction

# TODO: Pick up input validation here...
# work to validate multiple inputs

def validateInput(game, inputObj):
    if len(inputObj.word1) == 0:
        return "invalid"
    # inputlist = userInput.split()
    actionWord = ""
    if inputObj.word1 in game.cmd:
        actionWord = inputObj.word1
    else:
        actionWord = "invalid"
    return actionWord

def notAValidAction():
    print("Huh?")