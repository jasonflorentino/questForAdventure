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
        return self.getStatus(response)

    def inRoomOrInventory(self, itemKey, ITEM_NAME):
        if self.activeRoom.itemInRoom(itemKey) or self.player.itemInInventory(ITEM_NAME):
            return True
        return False
    
    def getStatus(self, response):
        here = self.activeRoom

        roomDesc = ""
        if here.visits == 1:
            roomDesc = here.description
        else:
            roomDesc = here.shortDesc

        response.addToPrint(f"\n[{here.name}]\n{roomDesc}\n")
        return response
    
    def getDirectionTarget(self, direction):
        return self.activeRoom.getNextRoom(direction)
    
    def getRoomContents(self, response):
        return self.activeRoom.listContents(self, response)
    
    def getInventory(self, response):
        response.addToPrint("\nYour Inventory:")
        self.player.listInventory(response)
        response.addToPrint("")
        return response
    
    def takeItem(self, response, item):
        ITEM_NAME = self.objects[item].name

        if not item in self.objects:    # Check if item exists
            response.addToPrint("That's not a thing.\n").setStatus_FailedAction("Item doesn't exist")
            return response
        elif not self.activeRoom.itemInRoom(item) and not self.player.itemInInventory(ITEM_NAME):  # Check if item is in room
            response.addToPrint("There is none here.\n").setStatus_FailedAction("Item not in room or inventory")
            return response
        elif not self.objects[item].takeable(): # Check if item is takeable
            response.addToPrint("You can't take that.\n").setStatus_FailedAction("Item isn't takeable")
            return response
        else:
            self.activeRoom.removeFromContents(item)
            self.player.addToInventory(ITEM_NAME)
            response.addToPrint(f"You took the {ITEM_NAME}.\n").setStatus_Success("game.takeItem()")
            return response
        