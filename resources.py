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
        print(f"[{self.currentLocation.name.title()}]")
        print(self.currentLocation.longDesc)
        print()
        self.currentLocation.visits += 1
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
        if self.currentLocation.north:
            self.currentLocation = self.currentLocation.north
            print("You go north...\n")
            self.look()
            self.currentLocation.visits += 1
        else:
            print("You can't go that way.")

    def south(self):
        if self.currentLocation.south:
            self.currentLocation = self.currentLocation.south
            print("You go south...\n")
            self.look()
            self.currentLocation.visits += 1
        else:
            print("You can't go that way.")

    def east(self):
        if self.currentLocation.east:
            self.currentLocation = self.currentLocation.east
            print("You go east...\n")
            self.look()
            self.currentLocation.visits += 1
        else:
            print("You can't go that way.")

    def west(self):
        if self.currentLocation.west:
            self.currentLocation = self.currentLocation.west
            print("You go west...\n")
            self.look()
            self.currentLocation.visits += 1
        else:
            print("You can't go that way.")

    def help(self):
        print("You call for help. Nobody hears.")
        return "help"

    def inventory(self):
        if len(self.inventory) == 0:
            print("There is nothing in your inventory.")
        else:
            print("INVENTORY:")
            for itemObj in self.inventory:
                itemObj.printName()

    def look(self):
        room = self.currentLocation
        print(f"[{room.name}]")
        if room.visits == 0:
            room.printLongDesc()
        else:
            room.printShortDesc()
        print("You see:")
        room.printContents()

    def quit(self):
        youSure = input("Are you sure you want to quit? (y/n)\n> ").lower()
        if youSure == "y" or youSure == "yes":
            print("Returning to main menu...")
            time.sleep(0.5)
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
        item = input("What do you want to drop?\n- ")
        try:
            itemObj = gameObjects.allItems[item]
        except:
            pass
        if item not in gameObjects.allItems:     # Checks if item is a real item
            print(f"I don't know what that is.")
        elif itemObj not in self.inventory:    # Item exists, now check if in inventory
            print(f"There is no {item} in your inventory.")
        else:   # all checks pass -- take item
            self.inventory.remove(itemObj)
            self.currentLocation.contents.append(itemObj)
            if itemObj.dropResp:
                print(itemObj.dropResp)
            else:
                print(f"You dropped the {item}.")

    def place(self):
        print("Game class DEBUG: action success: place")

    def take(self):
        item = input("What do you want to take?\n- ")
        try:
            itemObj = gameObjects.allItems[item]
        except:
            pass
        if item not in gameObjects.allItems:     # Checks if item is a real item
            print(f"There is no {item}.")
        elif itemObj not in self.currentLocation.contents:    # Item exists, now check if in same room
            print(f"There is no {item} here.")
        elif itemObj.takeable == False:   # Checks if item is takeable
            print(f"This ought to stay right here.")
        else:   # all checks pass -- take item
            self.inventory.append(itemObj)
            self.currentLocation.contents.remove(itemObj)
            if itemObj.takeResp:
                print(itemObj.takeResp)
            else:
                print(f"You took the {item}.")

    def talk(self):
        print("Game class DEBUG: action success: talk")

    def smell(self):
        print("Game class DEBUG: action success: smell")

    def open(self):
        item = input("What do you want to open?\n- ")
        try:
            itemObj = gameObjects.allItems[item]
        except:
            pass
        if item not in gameObjects.allItems:     # Checks if item is a real item
            print(f"There is no {item}.")
        elif itemObj not in self.inventory and itemObj not in self.currentLocation.contents:    # Item exists, now check if in reach
            print(f"There is no {item} here.")
        elif itemObj.container == False:
            print(f"{item.title()} can't be opened.")
        elif itemObj.isOpen == True:
            print(f"{item.title()} is already open.")
        else:
            itemObj.open()

    def use(self):
        print("Game class DEBUG: action success: use")

    def examine(self):
        item = input("What do you want to examine?\n- ")
        try:
            itemObj = gameObjects.allItems[item]
        except:
            pass
        if item not in gameObjects.allItems:     # Checks if real item
            print(f"There is no {item}.")
        elif itemObj not in self.currentLocation.contents:    # Item exists, now check if in same room
            print(f"There is no {item} here.") 
        else:   # All checks pass -- examine item
            print(f"You examine the {item}...")
            sleep(0.5)
            itemObj.printDesc()

    def move(self):
        direction = input("In which direction do you want to go?\n- ")
        try:
            self.directInput(direction)
        except:
            print("I don't understand.")

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
        return turnAction

test = Game("test")
print(test.inventory)
print(test.currentLocation.contents)
test.directInput("look")
test.directInput("take")
test.directInput("west")
test.directInput("open")
