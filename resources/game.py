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
        self.player = Player()
        self.rooms = createRooms()
        self.objects = createObjects()
    
    def incrementTurnCount(self):
        self.turnCount += 1
        return self
    
    def eventCheck(self):
        sendBack = None
        if self.turnCount == 1:
            beginning(self)
            sendBack = "beginning"
        print()
        return sendBack

    def execute(self, userInputObject):
        textToPrint, actionToEval = actionsDict[userInputObject.word1](self, userInputObject)
        return (textToPrint, actionToEval)
    
    def movePlayer(self, newLocation):
        self.player.changeLocation(newLocation)
        self.rooms[newLocation].incrementVisits()
        return self.getStatus()
    
    def getStatus(self):
        cL = self.rooms[self.player.currentLocation]
        roomDesc = ""
        if cL.visits == 1:
            roomDesc = cL.description
        else:
            roomDesc = cL.shortDesc
        roomStatus = f"[{cL.name}]\n{roomDesc}"
        return roomStatus