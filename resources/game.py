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
    
    def itemIsntInTheSameRoom(self, item):
        if self.activeRoom.itemInRoom(item):
            return False
        return True
    
    def itemIsntInPlayerInventory(self, ITEM_NAME):
        if self.player.itemInInventory(ITEM_NAME):
            return False
        return True

    def inRoomOrInventory(self, itemKey, ITEM_NAME):
        if self.activeRoom.itemInRoom(itemKey) or self.player.itemInInventory(ITEM_NAME):
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
    
    def getInventory(self, response):
        response.addToPrint("\nYour Inventory:")
        self.player.listInventory(response)
        response.addToPrint("")
        return response
    
    def examineItem(self, response, item):
        try:
            ITEM_NAME = self.objects[item].name
        except:
            pass
        if self.itemDoesntExist(item):
            response.set_itemDoesntExist()
            return response
        elif not self.inRoomOrInventory(item, ITEM_NAME):
            response.addToPrint("There is none here.\n").setStatus_FailedAction("Item not in room or inventory")
            return response
        else:
            response.addToPrint(f"You examine the {ITEM_NAME}...\n" + self.objects[item].description)
            response.setStatus_Success("game.examineItem()")
            if isinstance(self.objects[item], Container):
                self.objects[item].checkIfOpen(response)
            return response

    def takeItem(self, response, item):
        try:
            ITEM_NAME = self.objects[item].name
        except:
            pass
        if self.itemDoesntExist(item):
            response.set_itemDoesntExist()
            return response
        elif self.itemIsntInTheSameRoom(item) and self.itemIsntInPlayerInventory(ITEM_NAME):
            response.addToPrint("There is none here.\n").setStatus_FailedAction("Item not in room or inventory")
            return response
        elif not self.objects[item].takeable(): # Check if item is takeable
            response.addToPrint("You can't take that.\n").setStatus_FailedAction("Item isn't takeable")
            return response
        else:
            self.activeRoom.removeFromContents(item)
            self.player.addToInventory(ITEM_NAME)
            response.addToPrint(f"You took the {ITEM_NAME}.").setStatus_Success("game.takeItem()")
            return self.objects[item].getsTaken(response)
    
    def dropItem(self, response, item):
        try:
            ITEM_NAME = self.objects[item].name
        except:
            pass
        if self.itemDoesntExist(item):
            response.set_itemDoesntExist()
            return response
        elif self.itemIsntInPlayerInventory(ITEM_NAME):
            response.addToPrint("You don't have one of those.\n").setStatus_FailedAction("Item not in inventory")
            return response
        else:
            self.player.removeFromInventory(ITEM_NAME)
            self.activeRoom.addToContents(item)
            response.addToPrint(f"You dropped the {ITEM_NAME}.").setStatus_Success("game.dropItem()")
            return self.objects[item].getsDropped(response)