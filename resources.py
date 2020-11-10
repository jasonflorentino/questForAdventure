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
    
    def addToInventory(self, item):
        self.inventory.append(item)
        self.items[item]["location"] = "inventory"
        print(f"{item.capitalize()} was added to inventory.")

    def getSecondInput(self, action):
        return input(f"What do you want to {action}?\n")

    def notARealItem(self, item):
        if item not in gameObjects.allItems:
            print(f"There is no {item}.")
            return True
        else:
            return False
    
    def notInTheSameRoom(self, itemObj):
        if itemObj not in self.currentLocation.contents:
            print(f"There is no {itemObj.name} here.")
            return True
        else:
            return False

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
        print("You see: ", end='')
        room.printContents()
        print()

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
        item = self.getSecondInput("close")
        try:
            itemObj = gameObjects.allItems[item]
        except:
            pass
        if self.notARealItem(item):
            return
        elif itemObj not in self.inventory and itemObj not in self.currentLocation.contents:    # Item exists, now check if in reach
            print(f"There is no {item} here.")
        else:
            itemObj.close()

    def drop(self):
        item = self.getSecondInput("drop")
        try:
            itemObj = gameObjects.allItems[item]
        except:
            pass
        if self.notARealItem(item):
            return
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
        item = self.getSecondInput("place")
        try:
            itemObj = gameObjects.allItems[item]
        except:
            pass
        if self.notARealItem(item):
            return
        elif itemObj not in self.inventory:    # Item exists, now check if in inventory
            print(f"There is no {item} in your inventory.")
        else:
            cont = input(f"In what do you want to place the {item}?\n")
            try:
                contObj = gameObjects.allItems[cont]
            except:
                pass
            if self.notARealItem(item):
                return
            elif contObj not in self.inventory and contObj not in self.currentLocation.contents:    # Item exists, now check if in reach
                print(f"There is no {cont} here.")
            else:
                self.inventory.remove(itemObj)
                contObj.place(itemObj)

    def take(self):
        item = self.getSecondInput("take")
        try:
            itemObj = gameObjects.allItems[item]
        except:
            pass
        if self.notARealItem(item):
            return
        elif self.notInTheSameRoom(itemObj):
            return
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
        item = self.getSecondInput("open")
        try:
            itemObj = gameObjects.allItems[item]
        except:
            pass
        if self.notARealItem(item):
            return
        elif itemObj not in self.inventory and itemObj not in self.currentLocation.contents:    # Item exists, now check if in reach
            print(f"There is no {item} here.")
        else:
            itemObj.open()

    def use(self):
        print("Game class DEBUG: action success: use")

    def empty(self):
        item = self.getSecondInput("empty")
        try:
            itemObj = gameObjects.allItems[item]
        except:
            pass
        if self.notARealItem(item):
            return
        elif itemObj not in self.inventory and itemObj not in self.currentLocation.contents:    # Item exists, now check if in reach
            print(f"There is no {item} here.")
        else:
            self.currentLocation.contents.append(itemObj.empty())

    def examine(self):
        item = self.getSecondInput("examine")
        try:
            itemObj = gameObjects.allItems[item]
        except:
            pass
        if self.notARealItem(item):
            return
        elif self.notInTheSameRoom(itemObj):
            return
        else:   # All checks pass -- examine item
            print(f"You examine the {item}...")
            sleep(0.5)
            itemObj.printDesc()
            if itemObj.container:
                if itemObj.isOpen:
                    if len(itemObj.contents) > 0:
                        print(f"Inside there is a {itemObj.contents[0].name}.")
                    else:
                        print("There is nothing inside.")
                else:
                    print("It's shut.")


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
        "cast":cast,
        "close":close,
        "drop":drop,
        "empty":empty,
        "examine":examine,
        "help":help,
        "inventory":inventory,
        "look":look,
        "move":move,
        "open":open,
        "place":place,
        "quit":quit,
        "smell":smell,
        "take":take,
        "talk":talk,
        "use":use,
        "xyzzy":xyzzy,
        }

    def directInput(self, turnAction):
        action = self.cmd[turnAction](self)
        return turnAction

test = Game("test")
print(test.inventory)
print(test.currentLocation.contents)
# test.directInput("look")
test.directInput("take")
# test.directInput("open")
# test.directInput("place")
# test.directInput("inventory")
# test.directInput("look")
# test.directInput("empty")
# test.directInput("look")

