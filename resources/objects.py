#! Python3
# objects.py

"""
OBJECT CLASSES
"""

class GameObject():
    def __init__(self, name, description, odour, isVisible):
        self.name = name
        self.description = description
        self.odour = odour
        self.isVisible = isVisible
    
    def toggleVisibility(self):
        self.isVisible = not self.isVisible
        return self

class Item(GameObject):
    def __init__(self, name, description, odour, isVisible,
            isTakeable, isUseable, isReusable, isUsed,
            takeResp, useResp, dropResp):
       GameObject.__init__(self, name, description, odour, isVisible)
       self.isTakeable = isTakeable
       self.isUseable = isUseable
       self.isReusable = isReusable
       self.isUsed = isUsed
       self.takeResp = takeResp
       self.useResp = useResp
       self.dropResp = dropResp

class Container(Item):
    def __init__(self, name, description, odour, isVisible,
        isTakeable, isUseable, isReusable, isUsed,
        takeResp, useResp, dropResp, isContainer, isOpen,
        isCloseable, contents):
        Item.__init__(self, name, description, odour, isVisible,
            isTakeable, isUseable, isReusable, isUsed,
            takeResp, useResp, dropResp)
        self.isContainer = isContainer
        self.isOpen = isOpen
        self.isCloseable = isCloseable
        self.contents = contents
    
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

class Npc(GameObject):
    def __init__(self, name, description, odour, isVisible, isTalkable, talkResp):
        GameObject.__init__(self, name, description, odour, isVisible)
        self.isTalkable = isTalkable
        self.talkResp = talkResp

"""
GENERATE OBJECTS
"""

def createObjects():
    gameObjects = {**itemObjectData, **containerObjectData, **npcObjectData}
    return gameObjects

"""
DEFAULT OBJECT DATA
"""

itemObjectData = {
    "bed": Item(
        "bed",
        "It is comfortable and warm. No place for an Adventurer like yourself!",
        "The sweet smell of fresh linen and days wasted.",
        True,
        False,
        True,
        True,
        False,
        False,
        "I guess we could just forget this whole adventure thing that happens to be *your calling in life*. Or you could get up, you lazy, son of a bar wench",
        False
    ),
    "mirror": Item(
        "mirror",
        "You can't help but wonder if the chain-mail makes your butt look big.",
        False,
        True,
        False,
        True,
        True,
        False,
        False,
        "You can't help but wonder if the chain-mail makes your butt look big.",
        False
    )
}

containerObjectData = {
    "wardrobe": Container(
        "wardrobe",
        "A large mahogany wardrobe.",
        "This smells like grandma: mothballs and disappointment.",
        True,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        True,
        False,
        True,
        ["armour"]
    ),
    "chamber pot": Container(
        "chamber pot",
        "Why would you want to look at that? Gross.",
        "Urrgh. Why would you do that? You know what goes in there!",
        True,
        True,
        True,
        True,
        False,
        "Why? I guess you could gross out your enemies with this.",
        "You feel ... relieved.",
        False,
        True,
        False,
        True,
        []
    )
}

npcObjectData = {

}