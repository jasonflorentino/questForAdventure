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
        print('turn #' + str(game.turnCount) + " - main()") # DEBUG
        if game.turnCount == 0:
            game.beginning()
        action = turn(game)
        game.turnCount += 1
        if action == "quit":
            break
        else:
            pass
    return True

def parseUserInput(game, userInput):
    if len(userInput) == 0:
        return "invalid"
    inputlist = userInput.split()
    actionWord = ""
    if inputlist[0] in game.cmd:
        actionWord = inputlist[0]
    else:
        actionWord = "invalid"
    return actionWord

def youCantDoThat():
    print("Huh?")

# def directAction(turnAction):
#     if turnAction == "north":
#         game.north()
#     elif turnAction == "south":
#         game.south()
#     elif 

def turn(game):
    turnAction = parseUserInput(game, input("\n> ").lower())
    print(f"user input: {turnAction} - turn()")    # DEBUG
    if turnAction == "invalid":
        youCantDoThat()
    else:
        turnAction = game.directInput(turnAction)
        # check if second input needed
        # if true, get second input
        # if false pass
        # execute actionword
            # check if action is possible
                # check first action word
                # then check object if exists
    return turnAction