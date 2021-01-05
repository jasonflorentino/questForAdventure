#! Python3
# game.py

# Imports if run from main.py
from .game_events import *
from .player import *
from .rooms import *
from .objects import *
from .util import toCamelCase

# Imports if running game.py
# from game_events import *
# from player import *
# from rooms import *
# from objects import *

class Game():
    def __init__(self, name):
        self.name = name
        self.turnCount = 1
        self.player = Player() # Player Object
        self.rooms = createRooms() # Dictionary of "roomNam": Room Object
        self.objects = createObjects() # Dictionary of "objectName": Game Object
        self.activeRoom = False # Stores reference to current Room Object
    
    def incrementTurnCount(self):
        self.turnCount += 1
        return self
    
    def eventCheck(self):
        sendBack = None
        if self.turnCount == 1:
            beginning(self)
            sendBack = "beginning"
        return sendBack
    
    def movePlayer(self, newLocation, response):
        self.activeRoom = self.rooms[newLocation] # Room Object
        self.player.changeLocation(newLocation)
        self.rooms[newLocation].incrementVisits()
        return self.getRoomDescription(response)

    def itemDoesntExist(self, item):
        if item in self.objects:
            return False
        return True
    
    def itemIsntInTheSameRoom(self, itemKey):
        if self.activeRoom.itemInRoom(itemKey):
            return False
        return True
    
    def itemIsntInPlayerInventory(self, itemKey):
        if self.player.itemInInventory(itemKey):
            return False
        return True

    def inRoomOrInventoryOrContainers(self, itemKey):
        if self.activeRoom.itemInRoom(itemKey) or self.player.itemInInventory(itemKey) or self.checkContainers(itemKey):
            return True
        return False
    
    def checkContainers(self, itemKey):
        ITEMS = self.activeRoom.getContents() + self.player.getInventory()
        for item in ITEMS:
            if isinstance(self.objects[item], Container):
                if self.objects[item].checkIfOpen():
                    for content in self.objects[item].getContents():
                        if itemKey == content:
                            return True
        return False

    def getRoomDescription(self, response):
        here = self.activeRoom

        roomDesc = ""
        if here.visits == 1:
            roomDesc = here.description
        else:
            if here.shortDesc:
                roomDesc = here.shortDesc
            else:
                roomDesc = here.description  

        response.addToPrint(f"\n[{here.name}]\n{roomDesc}\n")
        return response
    
    def getDirectionTarget(self, direction):
        return self.activeRoom.getNextRoom(direction)
    
    def getRoomContents(self, response):
        here = self.activeRoom
        response.addToPrint(f"\nYou look around the {here.name}...")
        return here.listContents(self, response)
    
    def listInventory(self, response):
        response.addToPrint("\nYour Inventory:")
        INVENTORY = self.player.getInventory()
        if len(INVENTORY) == 0:
            response.addToPrint("There is nothing to show.")
        else:
            for itemKey in INVENTORY:
                response.addToPrint(f"- {self.objects[itemKey].getName()}")
        response.addToPrint("")
        return response
    
    def checkItemContents(self, response, itemKey):
        if self.objects[itemKey].checkIfOpen():
            CONTENTS = self.objects[itemKey].getContents()
            PREP = self.objects[itemKey].getPrep()
            if len(CONTENTS) == 0:
                response.addToPrint(f"There is nothing {PREP}.")
            else:
                response.addToPrint(f"There is something {PREP}...")
                for itemKey in CONTENTS:
                    ITEM_NAME = self.objects[itemKey].getName()
                    response.addToPrint(f"- {ITEM_NAME}")
        else:
            response.addToPrint("It's closed...")
        return response
    
    def makeContentsTakeable(self, itemKey):
        for item in self.objects[itemKey].getContents():
            self.objects[item].makeTakeable()

    def makeContentsUntakeable(self, itemKey):
        for item in self.objects[itemKey].getContents():
            self.objects[item].makeUntakeable()
    
    def examineItem(self, response, itemKey):
        if self.itemDoesntExist(itemKey):
            response.set_itemDoesntExist()
        elif not self.inRoomOrInventoryOrContainers(itemKey):
            response.addToPrint("There is none here.").setStatus_FailedAction("Item not in room or inventory")
        else:
            itemName = self.objects[itemKey].getName()
            itemDescription = self.objects[itemKey].getDescription()
            response.addToPrint(f"You examine the {itemName}...\n{itemDescription}")
            response.setStatus_Success("game.examineItem()")
            if isinstance(self.objects[itemKey], Container):
                self.checkItemContents(response, itemKey)
        response.addToPrint("")
        return response

    def takeItem(self, response, itemKey):
        if self.itemDoesntExist(itemKey):
            response.set_itemDoesntExist()
            return response
        elif not self.inRoomOrInventoryOrContainers(itemKey):
            response.addToPrint("There is none here.\n").setStatus_FailedAction("Item not in room or inventory")
            return response
        elif not self.objects[itemKey].takeable(): # Check if item is takeable
            response.addToPrint("I think that should stay right where it is.\n").setStatus_FailedAction("Item isn't takeable")
            return response
        else:
            itemName = self.objects[itemKey].getName()
            ROOM_CONTENTS = self.activeRoom.getContents()
            if itemKey in ROOM_CONTENTS:
                self.activeRoom.removeFromContents(itemKey)
            else:
                for item in ROOM_CONTENTS:
                    if isinstance(self.objects[item], Container) and self.objects[item].checkIfOpen():
                        self.objects[item].removeFromContents(itemKey)
            self.player.addToInventory(itemKey)
            response.addToPrint(f"You took the {itemName}.").setStatus_Success("game.takeItem()")
            return self.objects[itemKey].getsTaken(response)
    
    def dropItem(self, response, itemKey):
        if self.itemDoesntExist(itemKey):
            response.set_itemDoesntExist()
            return response
        elif self.itemIsntInPlayerInventory(itemKey):
            response.addToPrint("You don't have one of those.\n").setStatus_FailedAction("Item not in inventory")
            return response
        else:
            itemName = self.objects[itemKey].getName()
            self.player.removeFromInventory(itemKey)
            self.activeRoom.addToContents(itemKey)
            response.addToPrint(f"You dropped the {itemName}.").setStatus_Success("game.dropItem()")
            return self.objects[itemKey].getsDropped(response)
    
    def openItem(self, response, itemKey):
        if self.itemDoesntExist(itemKey):
            response.set_itemDoesntExist()
        elif not self.inRoomOrInventoryOrContainers(itemKey):
            response.addToPrint("There is none here.").setStatus_FailedAction("Item not in room or inventory")
        elif not isinstance(self.objects[itemKey], Container):
            response.addToPrint("You can't open that.").setStatus_FailedAction("Item isn't a container")
        elif self.objects[itemKey].checkIfOpen():
            response.addToPrint("It's already open.")
            self.checkItemContents(response, itemKey)
        else:
            self.objects[itemKey].toggleOpen()
            ITEM_NAME = self.objects[itemKey].getName()
            response.addToPrint(f"You open the {ITEM_NAME}...")
            self.checkItemContents(response, itemKey)
            self.makeContentsTakeable(itemKey)
        response.addToPrint("")
        return response
    
    def closeItem(self, response, itemKey):
        if self.itemDoesntExist(itemKey):
            response.set_itemDoesntExist()
        elif not self.inRoomOrInventoryOrContainers(itemKey):
            response.addToPrint("There is none here.").setStatus_FailedAction("Item not in room or inventory")
        elif not isinstance(self.objects[itemKey], Container):
            response.addToPrint("You can't close that.").setStatus_FailedAction("Item isn't a container")
        elif not self.objects[itemKey].checkIfOpen():
            response.addToPrint("It's already closed.")
        elif not self.objects[itemKey].isCloseable:
            response.addToPrint("You can't close that.").setStatus_FailedAction("Container cannot be closed")
        else:
            ITEM_NAME = self.objects[itemKey].getName()
            self.objects[itemKey].toggleOpen()
            self.makeContentsUntakeable(itemKey)
            response.addToPrint(f"You closed the {ITEM_NAME}.")
        response.addToPrint("")
        return response

    def smellRoom(self, response):
        response.addToPrint("You take a whiff of your surroundings...")
        if self.activeRoom.hasOdour():
            response.addToPrint(self.activeRoom.getOdour())
        else:
            response.addToPrint("You smell nothing in particular.")
        response.addToPrint("")
        return response

    def smellItem(self, response, itemKey):
        if self.itemDoesntExist(itemKey):
            response.set_itemDoesntExist()
        elif not self.inRoomOrInventoryOrContainers(itemKey):
            response.addToPrint("There is none here.").setStatus_FailedAction("Item not in room or inventory")
        else:
            ITEM_NAME = self.objects[itemKey].getName()
            response.addToPrint(f"You smell the {ITEM_NAME}...")
            if self.objects[itemKey].hasOdour():
                response.addToPrint(self.objects[itemKey].getOdour())
            elif isinstance(self.objects[itemKey], Npc):
                response.addToPrint(f"They pull back, alarmed and mildly repulsed.")
            else:
                response.addToPrint(f"It doesn't smell like much.")
        response.addToPrint("")
        return response
    
    def putItem(self, response, itemKey):
    # Check if valid item
        if self.itemDoesntExist(itemKey):
            response.set_itemDoesntExist()
            response.addToPrint("")
            return response
        elif self.itemIsntInPlayerInventory(itemKey):
            response.addToPrint("You don't have one of those.\n").setStatus_FailedAction("Item not in inventory")
            return response
        
    # Get target item and check if valid
        target = input("Where do you want to put it?\n>> ").lower()
        if target in ("down", "ground", "floor"):
            response.setStatus_FailedAction("Dropping item instead...")
            self.dropItem(response, itemKey)
            return response
        else:
            target = toCamelCase(target)

        if self.itemDoesntExist(target):
            response.set_itemDoesntExist()
            response.addToPrint("")
            return response
        elif not self.inRoomOrInventoryOrContainers(target):
            response.addToPrint("There is none here.\n").setStatus_FailedAction("Item not in room or inventory")
            return response

    # Execute (halt if target is a container and isn't open)
        ITEM_NAME = self.objects[itemKey].getName()
        TARGET_NAME = self.objects[target].getName()
        PREP = self.objects[target].getPrep()

        if isinstance(self.objects[target], Container) and not self.objects[target].checkIfOpen():
            response.addToPrint(f"The {TARGET_NAME} isn't open...\n").setStatus_FailedAction("Item not in room or inventory")
            return response

        response.addToPrint(f"You put the {ITEM_NAME} {PREP} the {TARGET_NAME}...")
        self.player.removeFromInventory(itemKey)
        self.objects[target].addToContents(itemKey)

        response.addToPrint("")
        return response
