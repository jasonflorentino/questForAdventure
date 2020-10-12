#! Python3
# mainFunc.py - functions called from the main game file

from time import sleep

from resources import Game

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
    if choice == "q" or choice == "quit":
        return False
    elif choice == "n" or choice == "new":
        game = Game("New")
        return game
    else:
        return True

def main(game):
    if game == False:
        return False
    action = ""
    while True:
        print('turn #' + str(game.turnCount)) # DEBUG
        if game.turnCount == 0:
            game.beginning()
        action = turn()
        game.turnCount += 1
        if action == "quit":
            break
        else:
            pass
    return True

def parseUserInput(userInput):
    actionWord = userInput
    # Identify input
    # check if valid command
    # return INVALID if not
    return actionWord
    
def turn():
    turnAction = parseUserInput(input("\n> ").lower())
    # receives valid command
    # check if command is actionable
    # return can't do if not
    # otherwise, execute action
    return turnAction