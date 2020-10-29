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
        # print('main(): turn #' + str(game.turnCount)) # DEBUG
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
    turnAction = validateInput(game, input("\n> ").lower())       # USER INPUT
    # print(f"user input: {turnAction} - turn()")    # DEBUG
    print()
    if turnAction == "invalid":
        notAValidAction()
    else:
        turnAction = game.directInput(turnAction)
    return turnAction

def validateInput(game, userInput):
    if len(userInput) == 0:
        return "invalid"
    inputlist = userInput.split()
    actionWord = ""
    if inputlist[0] in game.cmd:
        actionWord = inputlist[0]
    else:
        actionWord = "invalid"
    return actionWord

def notAValidAction():
    print("Huh?")