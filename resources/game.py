#! Python3
# game.py

# Imports if run from main.py
from .game_events import *
from .player import *
from .rooms import *
from .objects import *

# Imports if run from source file
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

    def inRoomOrInventory(self, itemKey):
        if self.activeRoom.itemInRoom(itemKey) or self.player.itemInInventory(itemKey):
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
        response.addToPrint("")
        return response
    
    def examineItem(self, response, itemKey):
        if self.itemDoesntExist(itemKey):
            response.set_itemDoesntExist()
            return response
        elif not self.inRoomOrInventory(itemKey):
            response.addToPrint("There is none here.\n").setStatus_FailedAction("Item not in room or inventory")
            return response
        else:
            itemName = self.objects[itemKey].getName()
            itemDescription = self.objects[itemKey].getDescription()
            response.addToPrint(f"You examine the {itemName}...\n{itemDescription}")
            response.setStatus_Success("game.examineItem()")
            if isinstance(self.objects[itemKey], Container):
                self.checkItemContents(response, itemKey)
            return response

    def takeItem(self, response, itemKey):
        if self.itemDoesntExist(itemKey):
            response.set_itemDoesntExist()
            return response
        elif self.itemIsntInTheSameRoom(itemKey) and self.itemIsntInPlayerInventory(itemKey):
            response.addToPrint("There is none here.\n").setStatus_FailedAction("Item not in room or inventory")
            return response
        elif not self.objects[itemKey].takeable(): # Check if item is takeable
            response.addToPrint("You can't take that.\n").setStatus_FailedAction("Item isn't takeable")
            return response
        else:
            itemName = self.objects[itemKey].getName()
            self.activeRoom.removeFromContents(itemKey)
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