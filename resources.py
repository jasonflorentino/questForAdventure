#! Python3
# resources.py - class and functions definitions for main game.

from time import sleep

from gameData import gameData

def write(text):
    for letter in text:
        print(letter, end='', flush=True)
        # sleep(.02)      # Uncomment for slow printing

class Game(object):
    def __init__(self, name):
        self.name = name
        self.currentLocation = "chamber"
        self.inventory = []
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
        self.currentLocation = newLocation
        
    def printCurrentLocation(self):
        print('[%s]' % self.places[self.currentLocation]['screenName'])
    
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
        self.places["chamber"]["visits"] += 1
        self.turnCount += 1

    def north(self):
        self.currentLocation = self.places[self.currentLocation]["north"]
        print("You go north...\n")
        self.look()
        self.places[self.currentLocation]["visits"] += 1

    def south(self):
        self.currentLocation = self.places[self.currentLocation]["south"]
        print("You go south...\n")
        self.look()
        self.places[self.currentLocation]["visits"] += 1

    def east(self):
        self.currentLocation = self.places[self.currentLocation]["east"]
        print("You go east...\n")
        self.look()
        self.places[self.currentLocation]["visits"] += 1

    def west(self):
        self.currentLocation = self.places[self.currentLocation]["west"]
        print("You go west...\n")
        self.look()
        self.places[self.currentLocation]["visits"] += 1

    def help(self):
        print("Game class DEBUG: action success: help")

    def inventory(self):
        print("Game class DEBUG: action success: inventory")

    def look(self):
        if self.places[self.currentLocation]["visits"] == 0:
            self.printCurrentLocation()
            print(self.places[self.currentLocation]["longDesc"])
        else:
            self.printCurrentLocation()
            print(self.places[self.currentLocation]["shortDesc"])

    def quit(self):
        youSure = input("Are you sure you want to quit? (y/n)\n> ").lower()
        if youSure == "y" or youSure == "yes":
            print("Returning to main menu...")
            return "quit"
        else:
            return "no-quit"
        # print("action success - Game class - quit()")

    def xyzzy(self):
        print("Game class DEBUG: action success: xyzzy")

    def cast(self):
        print("Game class DEBUG: action success: cast")
    
    def close(self):
        print("Game class DEBUG: action success: close")

    def drop(self):
        print("Game class DEBUG: action success: drop")

    def place(self):
        print("Game class DEBUG: action success: place")

    def take(self):
        print("Game class DEBUG: action success: take")

    def talk(self):
        print("Game class DEBUG: action success: talk")

    def smell(self):
        print("Game class DEBUG: action success: smell")

    def open(self):
        print("Game class DEBUG: action success: open")

    def use(self):
        print("Game class DEBUG: action success: use")

    def examine(self):
        print("Game class DEBUG: action success: examine")

    def move(self):
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
        action = self.cmd[turnAction](self)
        return action