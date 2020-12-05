#! Python3
# game.py

# Imports if run from main.py
from .game_events import *
from .game_actions import *
from .player import *
from .rooms import *
from .objects import *

# Imports if run from source file
# from game_events import *
# from game_actions import *
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

    def execute(self, userInputObject):
        response = actionsDict[userInputObject.word1](self, userInputObject)
        return response
    
    def movePlayer(self, newLocation):
        self.activeRoom = self.rooms[newLocation] # Room Object
        self.player.changeLocation(newLocation)
        self.rooms[newLocation].incrementVisits()
        return self.getStatus()
    
    def getStatus(self):
        here = self.activeRoom
        roomDesc = ""
        if here.visits == 1:
            roomDesc = here.description
        else:
            roomDesc = here.shortDesc
        roomStatus = f"\n[{here.name}]\n{roomDesc}\n"
        return roomStatus