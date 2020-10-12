#! Python3
# mainFunc.py - functions called from the main game file

from time import sleep

from resources import Game

def display(text):
    for letter in text:
        print(letter, end='', flush=True)
        sleep(.02)

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
    userInput = ""
    while True:
        print('turn count = ' + str(game.turnCount))
        if game.turnCount == 0:
            game.beginning()
        userinput = parseUserInput(input("> ").lower())
        if userinput == "quit":
            break
        else:
            pass
    return True

def parseUserInput(userInput):
    text = userInput
    return text