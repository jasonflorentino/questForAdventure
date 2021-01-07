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
    
    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def toggleVisibility(self):
        self.isVisible = not self.isVisible
        return self
    
    def hasOdour(self):
        if self.odour:
            return True
        else:
            return False
    
    def getOdour(self):
        return self.odour

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
    
    def makeTakeable(self):
        self.isTakeable = True
        return self

    def makeUntakeable(self):
        self.isTakeable = False
        return self
    
    def getsTaken(self, response):
        if self.takeResp:
            response.add(self.takeResp + "\n")
        else:
            response.add("")
        return response

    def getsDropped(self, response):
        if self.dropResp:
            response.add(self.dropResp + "\n")
        else:
            response.add("")
        return response

class Container(Item):
    def __init__(self, arguments):
        Item.__init__(self, arguments)
        self.isContainer = arguments.get("isContainer", True)
        self.isOpen = arguments.get("isOpen", False)
        self.isCloseable = arguments.get("isCloseable", True)
        self.contents = arguments.get("contents", [])
        self.preposition = arguments.get("preposition", "inside")
    
    def addToContents(self, itemKey):
        self.contents.append(itemKey)
        return self

    def removeFromContents(self, itemKey):
        self.contents.remove(itemKey)
        return self
    
    def toggleOpen(self):
        self.isOpen = not self.isOpen
        return self
    
    def checkIfOpen(self):
        if self.isOpen:
            return True
        else:
            return False
    
    def getContents(self):
        return self.contents
    
    def getPrep(self):
        return self.preposition

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
    "nothing": {
        "name": "???"
    },
    "bed": {
        "name": "Bed",
        "description": "It is comfortable and warm. No place for an Adventurer like yourself!",
        "odour": "The sweet smell of fresh linen and days wasted.",
        "isVisible": True,
        "isUseable": True,
        "isReusable": True,
        "useResp": "I guess we could just forget this whole adventure thing that happens to be *your calling in life*. Or you could get up, you lazy, son of a bar wench",
    },
    "mirror": {
        "name": "Mirror",
        "description": "You can't help but wonder if the chain-mail makes your butt look big.",
        "isVisible": True,
        "isUseable": True,
        "isReusable": True,
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
    },
    "broom": {
        "name": "Broom",
        "description": "This is a broom. You sweep the floor with it. It is used to clean. Cleaning is making things not dirty. I don't think you understand.",
        "isVisible": True,
        "isTakeable": True,
        "isUseable": True,
        "isReusable": True,
        "takeResp": "Well, there's a first for everything.",
        "useResp": "You sweep.",
    },
    "candles": {
        "name": "Candles",
        "description": "Who lit these? This is definitely a fire hazard.",
        "isVisible": True,
    },
    "warAxe": {
        "name": "War Axe",
        "description": "Ah the good old days when you could swing an axe the same size as you. I think it would be better to try another weapon since you aren't as strong as you used to be.",
        "isVisible": True,
    },
    "dagger": {
        "name": "Dagger",
        "description": "Useful during your days of thieving, but you aren't quite stealthy enough now that you've gained more than a couple of pounds eating cake with the King.",
        "isVisible": True,
    },
    "bow": {
        "name": "Bow",
        "description": "One of your first weapons.  You used to shoot bottles of mead off the barrack walls. It seems as though you've long since ran out of arrows, and your eyes aren't what they once were.",
        "isVisible": True, 
    },
    "sword": {
        "name": "Sword",
        "description": "The light dances across the blade. This is your most trusted weapon, sure to help you in battle.",
        "isVisible": True,
        "isTakeable": True,
        "isUseable": True,
        "isReusable": True,
        "takeResp": "As you grasp the hilt you are reminded of past battles won, and a single tear comes to your eyes. All this time lounging with royalty seems to have made you soft. You sheath your weapon after taking a few practice swings around the room, then wipe your tear before anyone sees.",
        "useResp": "Woah! Watch where you swing that thing!",
    },
    "shield": {
        "name": "Shield",
        "description": "There are dents all over this thing! This shield has saved your life on a number of occasions.",
        "isVisible": True,
        "isTakeable": True,
        "isUseable": True,
        "isReusable": True,
        "takeResp": "Heavy, but a life-saver. I wonder how it feels on your arm after all this time.",
        "useResp": "You slip your arm through the straps and grasp tightly. You start to feel more confident in your choice to go adventuring.",
    },
    "note": {
        "name": "Note",
        "description": "The note says 'xyzzy' in scrawled writing. Just a bunch of nonsense!",
        "isTakeable": True,
    },
    "signPost": {
        "name": "Sign Post",
        "description": "North: Cavernous Mountains.\nWest: Dark Forest.\nSouth: Bog\nEast: Private Property.",
        "isVisible": True,
    },
    "lint": {
        "name": "Lint",
        "isVisible": True,
        "description": "You question your life choices.",
        "isTakeable": True,
        "takeResp": 'Of course. Sure. Why not.',
    },
    "darkenedCrack": {
        "name": "Darkened Crack",
        "description": "A crack just barely big enough for you to fit through. A normal person would fit comfortably.",
        "isVisible": True,
    },
    "strangeStone": {
        "name": "Strange Stone",
        "description": "It seems to be covered in small etchings and sparkles slightly. There are five slender grooves along the sides, placed so as to fit comfortably in your hand. It seems to be an ancient artifact.",
        "isVisible": True,
        "isTakeable": True,
    },
    "trees": {
        "name": "Trees",
        "description": "Tall trees surround you. They seem to get denser to the South.",
        "isVisible": True,
    },
    "bushes": {
        "name": "Bushes",
        "description": "These bushes seem to be covered in thorns. Maybe to keep something out?",
        "isVisible": True,
    },
    "largeOak": {
        "name": "Large Oak",
        "description": "It seems to be centuries old due to its size. If that was the case with people, I would guess you were centuries old as well.\nThe tree has an assortment of strange holes throughout it.",
        "isVisible": True,
    },
    "berryBushes": {
        "name": "Berry Bushes",
        "description": "These bushes are covered in strange little berries. They don't look very appetizing.",
        "isVisible": True,
    },
    "strangeBerries": {
        "name": "Strange Berries",
        "description": "The berries are black. That can't be good.",
        "isTakeable": True,
        "isUsable": True,
        "odour": "They smell sour."
    },
    "smoke": {
        "name": "Smoke",
        "description": "The smoke seems to be coming from the north. Maybe there is a bonfire! Or a stake burning! Oh how I love a good stake burning.",
        "odour": "Smoky. Interesting."
    },
    "thatchRoofedCottages": {
        "name": "Thatch Roofed Cottages",
        "description": "Still smoking. It seems as though the attack was recent.",
        "isVisible": True,
        "odour": "Smells like burnt dreams."
    }
}

containerObjectData = {
    "wardrobe": {
        "name": "Wardrobe",
        "description": "A large mahogany wardrobe.",
        "odour": "This smells like grandma: mothballs and disappointment.",
        "isVisible": True,
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
        "isOpen": True,
        "isCloseable": False,
        "contents": ["soapyWater"]       
    },
    "dustyShelf": {
        "name": "Dusty Shelf",
        "description": "Looks like the one place in the house that doesn't get cleaned.",
        "isVisible": True,
        "isOpen": True,
        "isCloseable": False,
        "preposition": "on top"
    },
    "chest": {
        "name": "Chest",
        "description": "Ok fine. But it's just an old musty chest, sitting in an old musty room. Definitely not of any importance. It's probably rusted shut!",
        "odour": "It smells old and musty.",
        "useResp": "Wow. You don't give up, do you? No need to look at anything in here. Just dust and cobwebs.",
        "isVisible": True,
        "isOpen": False,
        "isCloseable": True,
        "contents": ["note"]    
    },
    "strangeHoles": {
        "name": "Strange Holes",
        "description": "There seems to be a faint glow coming from inside one of the holes. It darts quickly out of your vision. I think it was a fairy!",
        "isOpen": True,
        "isCloseable": False,
        "contents": ["nothing"]
    }
}

npcObjectData = {
    "fairy": {
        "name": "Fairy",
        "description": "The fairy peeks her head out of one of the holes. She is quite flustered.",
    },
    "concernedVillager": {
        "name": "Concerned Villager",
        "description": "The man paces in front of his freshly burnt home. He looks around eagerly for someone to talk to."
    },
    "cryingVillagers": {
        "name": "Crying Villagers",
        "description": "A group of villagers huddled together, weeping loudly. Maybe you should talk to someone to figure out what happened, instead of just standing there with your mouth open."
    }
}