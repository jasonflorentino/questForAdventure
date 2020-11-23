# python3
# player.py

class Player(object):
    def __init__(self, name="Player 1"):
        self.name = name
        self.currentLocation = None
        self.inventory = []
    
    def changeLocation(self, roomString):
        self.currentLocation = roomString
        return self

    def addToInventory(self, itemString):
        self.inventory.append(itemString)
        return self
    
    def removeFromInventory(self, itemString):
        self.inventory.remove(itemString)
        return self