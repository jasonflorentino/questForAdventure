#! Python3
# game.py

# Imports if run from main.py
# from .game_events import *
# from .game_actions import *
# from .player import *
# from .rooms import *
# from .objects import *

# Imports if run from source file
from game_events import *
from game_actions import *
from player import *
from rooms import *
from objects import *

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
        textToPrint, actionToEval = actionsDict[userInputObject.word1](self)
        return (textToPrint, actionToEval)