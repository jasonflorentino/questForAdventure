#! Python3
# response.py

from time import sleep
from .util import write

# Test import
# from util import write

class Response():
    def __init__(self):
        self.gameStatus = None
        self.toPrint = []
    
    def addToPrint(self, string):
        self.toPrint.append(string)
        return self
    
    def setGameStatus(self, status):
        self.gameStatus = status
        return self
    
    def writeResponse(self, slow=False):
        for text in self.toPrint:
            write(text)
        return self
        # if slow:
        #     for text in self.toPrint:
        #         for letter in text:
        #             print(letter, end='', flush=True)
        #             sleep(.02)
        # else:
        #     for line in self.toPrint:
        #         print(line)
        # return self