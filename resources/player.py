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

    def addToInventory(self, itemString):
        try:
            self.inventory.append(itemString)
            return self
        except:
            print("Item wasn't added to inventory")
    
    def removeFromInventory(self, item_name):
        self.inventory.remove(item_name)
        return self
    
    def listInventory(self, response):
        if len(self.inventory) == 0:
            response.addToPrint("There is nothing to show.")
        else:
            for itemName in self.inventory:
                response.addToPrint(f"- {itemName}")
        return response
    
    def itemInInventory(self, item_name):
        if item_name in self.inventory:
            return True
        return False