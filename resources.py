#! Python3
# resources.py - class and functions definitions for main game.

from time import sleep

from gameData import gameData

def write(text):
    for letter in text:
        print(letter, end='', flush=True)
        # sleep(.02) # Uncomment for slow printing

class Game(object):
    def __init__(self, name):
        self.name = name
        self.player = globals()['gameData']['player']
        self.items = globals()['gameData']['items']
        self.places = globals()['gameData']['places']
        self.turnCount = 0

    def incrementTurn(self):
        self.turnCount += 1

    def changeName(self, newName):
        self.name = newName
    
    def printName(self):
        print('The game name is ' + self.name)

    def changeCurrentLocation(self, newLocation):
        self.player['currentLocation'] = newLocation
        
    def printCurrentLocation(self):
        print('[%s]' % self.player['currentLocation'])
    
    def beginning(self):
        text = [
            "\nYou are an experienced adventurer who has saved kingdoms and rescued damsels in distress. You have slayed dragons and conquered sorcerers and have received generous rewards from Kings and villagers alike for your heroic feats. Now you are looking for your next adventure since you have grown weary of living in the lap of luxury.",
            "\nAnd so your quest begins...the quest for honour, glory, and fair maidens...",
            "\nThe Quest...",
            "\n   for Adventure!\n\n"
        ]
        for line in text:
            write(line)
            input()
        self.printCurrentLocation()
        write(self.places["chamber"]["longDesc"] + "\n")
        self.turnCount += 1

    def north():
        print("Game class DEBUG: YOU WENT NORTH!")

    def south():
        print("Game class DEBUG: YOU WENT south!")

    def east():
        print("Game class DEBUG: YOU WENT east!")

    def west():
        print("Game class DEBUG: YOU WENT west!")

    def help():
        print("Game class DEBUG: action success: help")

    def inventory():
        print("Game class DEBUG: action success: inventory")
    
    def look():
        print("Game class DEBUG: action success: look")

    def quit():
        youSure = input("Are you sure you want to quit? (y/n)\n> ").lower()
        if youSure == "y" or youSure == "yes":
            print("Returning to main menu...")
            return "quit"
        else:
            return "no-quit"
        # print("action success - Game class - quit()")

    def xyzzy():
        print("Game class DEBUG: action success: xyzzy")

    def cast():
        print("Game class DEBUG: action success: cast")
    
    def close():
        print("Game class DEBUG: action success: close")

    def drop():
        print("Game class DEBUG: action success: drop")

    def place():
        print("Game class DEBUG: action success: place")

    def take():
        print("Game class DEBUG: action success: take")

    def talk():
        print("Game class DEBUG: action success: talk")

    def smell():
        print("Game class DEBUG: action success: smell")

    def open():
        print("Game class DEBUG: action success: open")

    def use():
        print("Game class DEBUG: action success: use")

    def examine():
        print("Game class DEBUG: action success: examine")

    def move():
        print("Game class DEBUG: action success: move")

    cmd = {
        "north":north,
        "south":south,
        "east":east,
        "west":west,
        "help":help,
        "inventory":inventory,
        "look":look,
        "quit":quit,
        "xyzzy":xyzzy,
        "cast":cast,
        "close":close,
        "drop":drop,
        "place":place,
        "take":take,
        "talk":talk,
        "smell":smell,
        "open":open,
        "use":use,
        "examine":examine,
        "move":move,
        }

    def directInput(self, turnAction):
        action = self.cmd[turnAction]()
        return action