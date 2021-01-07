#! Python3
# response.py

from time import sleep
from .util import write

# Test import
# from util import write

class Response():
    def __init__(self, action):
        self.action = action
        self.gameStatus = None
        self.toPrint = []
    
    def add(self, string):
        self.toPrint.append(string)
        return self
    
    def setGameStatus(self, status):
        self.gameStatus = status
        return self

    def setStatus_Success(self, caller="Unknown caller"):
        self.gameStatus = f"{caller} set status to: Success"
        return self

    def setStatus_BadInput(self):
        self.gameStatus = "Invalid Input"
        return self
    
    def setStatus_FailedAction(self, note="No note given"):
        self.gameStatus = f"{self.action} action failed: {note}"
        return self
    
    def writeResponse(self, slow=False):
        for text in self.toPrint:
            write(text)
        return self
    
    def set_itemDoesntExist(self):
        self.add("That's not a thing.").setStatus_FailedAction("Item doesn't exist")
        return self