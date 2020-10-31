#! Python3
# resources.py - class and functions definitions for main game.

from time import sleep

from gameData import gameData
import gameObjects

def write(text):
    for letter in text:
        print(letter, end='', flush=True)
        # sleep(.02)      # Uncomment for slow printing

class Game(object):
    def __init__(self, name):
        self.name = name
        self.currentLocation = gameObjects.chamber
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

    def isRealItem(self, item):
        if item in self.items:
            return True
        else:
            return False

    def inSameRoom(self, item):
        if self.items[item]['location'] == self.currentLocation:
            return True
        else:
            return False

    def isTakeable(self, item):
        if self.items[item]['takeable']:
            return True
        else:
            return False
    
    def addToInventory(self, item):
        self.inventory.append(item)
        self.items[item]["location"] = "inventory"
        print(f"{item.capitalize()} was added to inventory.")

        """

        COMMANDS
        
        """

    def north(self):
        if self.places[self.currentLocation]["north"]:
            self.currentLocation = self.places[self.currentLocation]["north"]
            print("You go north...\n")
            self.look()
            self.places[self.currentLocation]["visits"] += 1
        else:
            print("You can't go that way.")
        return "north"

    def south(self):
        if self.places[self.currentLocation]["south"]:
            self.currentLocation = self.places[self.currentLocation]["south"]
            print("You go south...\n")
            self.look()
            self.places[self.currentLocation]["visits"] += 1
        else:
            print("You can't go that way.")
        return "south"

    # def east(self):
    #     if self.places[self.currentLocation]["east"]:
    #         self.currentLocation = self.places[self.currentLocation]["east"]
    #         print("You go east...\n")
    #         self.look()
    #         self.places[self.currentLocation]["visits"] += 1
    #     else:
    #         print("You can't go that way.")
    #     return "east"
    def east(self):
        self.currentLocation = self.currentLocation.east
        print("You go east.")
        print(f"[{self.currentLocation.name}]")
        print(self.currentLocation.shortDesc)

    # def west(self):
    #     if self.places[self.currentLocation]["west"]:
    #         self.currentLocation = self.places[self.currentLocation]["west"]
    #         print("You go west...\n")
    #         self.look()
    #         self.places[self.currentLocation]["visits"] += 1
    #     else:
    #         print("You can't go that way.")
    #     return "west"
    def west(self):
        self.currentLocation = self.currentLocation.west
        print("You go west.")
        print(f"[{self.currentLocation.name}]")
        print(self.currentLocation.shortDesc)

    def help(self):
        print("You call for help. Nobody hears.")
        return "help"

    def inventory(self):
        print("INVENTORY:")
        print(self.inventory)

    def look(self):
        if self.places[self.currentLocation]["visits"] == 0:
            self.printCurrentLocation()
            print(self.places[self.currentLocation]["longDesc"])
        else:
            self.printCurrentLocation()
            print(self.places[self.currentLocation]["shortDesc"])
        return "look"

    def quit(self):
        youSure = input("Are you sure you want to quit? (y/n)\n> ").lower()
        if youSure == "y" or youSure == "yes":
            print("Returning to main menu...")
            return "quit"
        else:
            return "no-quit"

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
        obj = input("What do you want to take?\n- ")
        if not self.isRealItem(obj):
            print(f"{obj} doesn't exist.")
            return ("take ", obj)
        elif not self.inSameRoom(obj):
            print(f"There is no {obj} here.")
            return ("take ", obj)
        elif not self.isTakeable(obj):
            print("You can't take that")
            return ("take ", obj)
        else:
            print(f"You took {self.items[obj]['screenName']}.")
            self.addToInventory(obj)

    def talk(self):
        print("Game class DEBUG: action success: talk")

    def smell(self):
        print("Game class DEBUG: action success: smell")

    def open(self):
        print("Game class DEBUG: action success: open")

    def use(self):
        print("Game class DEBUG: action success: use")

    def examine(self):
        obj = input("What do you want to examine?\n- ")
        if not self.isRealItem(obj):
            print(f"{obj} doesn't exist.")
            return ("examine ", obj)
        elif not self.inSameRoom(obj):
            print(f"There is no {obj} here.")
            return ("examine ", obj)
        else:
            print(f"You examine {self.items[obj]['screenName']}.")
            print(self.items[obj]['desc'])
            return ("examine ", obj)

    def move(self):
        direction = input("In which direction do you want to go?\n- ")
        try:
            self.directInput(direction)
        except:
            print("I don't understand")
        return "move"

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

test = Game("test")
print(test.currentLocation.name)
test.west()
test.east()