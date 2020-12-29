#! Python3
# objects.py

"""
OBJECT CLASSES
"""

class GameObject():
    def __init__(self, arguments):
        self.name = arguments.get("name", False)
        self.description = arguments.get("description", False)
        self.odour = arguments.get("odour", False)
        self.isVisible = arguments.get("isVisible", False)
    
    def toggleVisibility(self):
        self.isVisible = not self.isVisible
        return self

class Item(GameObject):
    def __init__(self, arguments):
       GameObject.__init__(self, arguments)
       self.isTakeable = arguments.get("isTakeable", False)
       self.isUseable = arguments.get("isUseable", False)
       self.isReusable = arguments.get("isReusable", False)
       self.isUsed = arguments.get("isUsed", False)
       self.takeResp = arguments.get("takeResp", False)
       self.useResp = arguments.get("useResp", False)
       self.dropResp = arguments.get("dropResp", False)

    def takeable(self):
        if self.isTakeable:
            return True
        return False
    
    def getsTaken(self, response):
        if self.takeResp:
            response.addToPrint(self.takeResp + "\n")
        else:
            response.addToPrint("\n")
        return response

    def getsDropped(self, response):
        if self.dropResp:
            response.addToPrint(self.dropResp + "\n")
        else:
            response.addToPrint("\n")
        return response

class Container(Item):
    def __init__(self, arguments):
        Item.__init__(self, arguments)
        self.isContainer = arguments.get("isContainer", True)
        self.isOpen = arguments.get("isOpen", False)
        self.isCloseable = arguments.get("isCloseable", True)
        self.contents = arguments.get("contents", [])
    
    def addToContents(self, objectString):
        self.contents.append(objectString)
        return self

    def removeFromContents(self, objectString):
        self.contents.remove(objectString)
        return self
    
    def toggleOpen(self):
        self.isOpen = not self.isOpen
        return self

    def openContainer(self):
        if self.isOpen:
            print(f"The {self.name} is already open.")
            return self
        else:
            self.toggleOpen()
            return self

    def closeContainer(self):
        if self.isOpen:
            self.toggleOpen()
            return self
        else:
            print(f"The {self.name} is already closed.")
            return self
    
    def checkIfOpen(self, response):
        if self.isOpen:
            response.addToPrint("It's open")
        else:
            response.addToPrint("It's closed...")
        return response

class Npc(GameObject):
    def __init__(self, arguments):
        GameObject.__init__(self, arguments)
        self.isTalkable = arguments.get("isTalkable", False)
        self.talkResp = arguments.get("talkResp", False)

"""
GENERATE OBJECTS
"""

def createObjects():
    gameObjects = {}
    # Create items
    for k, v in itemObjectData.items():
        gameObjects[k] = Item(v)
    # Create containers
    for k, v in containerObjectData.items():
        gameObjects[k] = Container(v)
    # Create NPCs
    for k, v in npcObjectData.items():
        gameObjects[k] = Npc(v)
        
    return gameObjects

"""
DEFAULT OBJECT DATA
"""

itemObjectData = {
    "bed": {
        "name": "Bed",
        "description": "It is comfortable and warm. No place for an Adventurer like yourself!",
        "odour": "The sweet smell of fresh linen and days wasted.",
        "isVisible": True,
        "isTakeable": False,
        "isUseable": True,
        "isReusable": True,
        "isUsed": False,
        "useResp": "I guess we could just forget this whole adventure thing that happens to be *your calling in life*. Or you could get up, you lazy, son of a bar wench",
    },
    "mirror": {
        "name": "Mirror",
        "description": "You can't help but wonder if the chain-mail makes your butt look big.",
        "isVisible": True,
        "isTakeable": False,
        "isUseable": True,
        "isReusable": True,
        "isUsed": False,
        "useResp": "You can't help but wonder if the chain-mail makes your butt look big.",
    },
    "armour": {
        "name": "Armour",
        "description": "Ooooh...shiny.",
        "isUseable": True,
        "isReusable": True,
        "odour": "Smells like metal. Who would have thought?",
        "takeResp": "Oof! This weighs a tonne! You've been sitting around too long in your underpants eating sweets. You should put the armour on so you can at least look the part.",
        "useResp": "It fits you like a glove. It looks like your boots could be buffed out a bit though. You should examine the mirror to see how you look.",
    },
    "huntingTrophies": {
        "name": "Hunting Trophies",
        "description": "Every type of animal head imaginable is up on this wall.",
        "isVisible": True,
    },
    "lavishGifts": {
        "name": "Lavish Gifts",
        "description": "Oooh...shiny. Lots of gold this and bejewelled that up here.",
        "isVisible": True,
    },
    "soapyWater": {
        "name": "Soapy Water",
        "description": "The water is murky and topped with bubbles.",
        "odour": "Lemony Fresh!",
    }
}

containerObjectData = {
    "wardrobe": {
        "name": "Wardrobe",
        "description": "A large mahogany wardrobe.",
        "odour": "This smells like grandma: mothballs and disappointment.",
        "isVisible": True,
        "isContainer": True,
        "isOpen": False,
        "isCloseable": True,
        "contents": ["armour"]
    },
    "chamberPot": {
        "name": "Chamber Pot",
        "description": "Why would you want to look at that? Gross.",
        "odour": "Urrgh. Why would you do that? You know what goes in there!",
        "isVisible": True,
        "isTakeable": True,
        "isUseable": True,
        "isReusable": True,
        "isUsed": False,
        "takeResp": "Why? I guess you could gross out your enemies with this.",
        "useResp": "You feel ... relieved.",
        "isContainer": True,
        "isOpen": False,
        "isCloseable": True,
    },
    "bucket": {
        "name": "Bucket",
        "description": "It looks like the maids just finished cleaning and left this here.",
        "isVisible": True,
        "isTakeable": True,
        "isUseable": True,
        "isReusable": True,
        "takeResp": "What? Are you going to clean your chamber pot with this?",
        "useResp": "You pour its contents onto the floor.",
        "isContainer": True,
        "isOpen": True,
        "isCloseable": False,
        "contents": ["soapyWater"]       
    },

}

npcObjectData = {

}