# python3
# player.py

class Player(object):
    def __init__(self, name="Player 1"):
        self.name = name
        self.currentLocation = None
        self.inventory = [] # List of items as Screen Names
    
    def changeLocation(self, roomString):
        self.currentLocation = roomString
        return self

    def addToInventory(self, itemKey):
        self.inventory.append(itemKey)
        return self
    
    def removeFromInventory(self, itemKey):
        self.inventory.remove(itemKey)
        return self
    
    def getInventory(self):
        return self.inventory
    
    def itemInInventory(self, itemKey):
        if itemKey in self.inventory:
            return True
        return False