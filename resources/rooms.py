#! Python3
# rooms.py

"""
ROOM CLASS
"""

class Room():
    def __init__(self, arguments):
        self.name = arguments.get("name", False)
        self.description = arguments.get("description", False)
        self.shortDesc = arguments.get("shortDesc", False)
        self.north = arguments.get("north", False)
        self.east = arguments.get("east", False)
        self.south = arguments.get("south", False)
        self.west = arguments.get("west", False)
        self.contents = arguments.get("contents", [])
        self.odour = arguments.get("odour", False)
        self.visits = 0
    
    def incrementVisits(self):
        self.visits += 1
        return self

    def addToContents(self, itemKey):
        self.contents.append(itemKey)
        return self
    
    def removeFromContents(self, itemString):
        if itemString in self.contents:
            self.contents.remove(itemString)
            return itemString
        else:
            print("That item doesn't exist here.")
            return self
    
    def getNextRoom(self, direction):
        if direction == "north":
            return self.north
        elif direction == "east":
            return self.east
        elif direction == "south":
            return self.south
        else:
            return self.west
    
    def listContents(self, game, response):
        if len(self.contents) >= 1:
            response.add("You see:")
            for item in self.contents:
                response.add("- " + game.objects[item].name)
            response.add("")
        else:
            response.add("You see nothing of interest.\n")
        return response
    
    def itemInRoom(self, itemKey):
        if itemKey in self.contents:
            return True
        else:
            return False
    
    def getContents(self):
        return self.contents
    
    def hasOdour(self):
        if self.odour:
            return True
        else:
            return False

    def getOdour(self):
        return self.odour



"""
GENERATE ROOM OBJECTS
"""

def createRooms():
    roomObjects = {}
    for k, v in roomData.items():
        roomObjects[k] = Room(v)
    return roomObjects


"""
DEFAULT ROOM DATA
"""

roomData = {
    "roomTemplate": {
        "name": "Test Room",
        "description": "test description",
        "shortDesc": "short test description",
        "north": "goNorth",
        "east": "goEast",
        "south": False,
        "west": "goWest",
        "contents": []
    },
    "chamber": {
        "name": "Chamber",
        "description": "You wake up from a restless night's sleep.\nSince you were also knighted for ridding the bog of a bog monster,\nyou could say you woke from a knight's restless night's sleep.\nYou are in your sleeping chamber.\nThere is a door to the West that leads to the Hallway.\nYou should probably get dressed before going out there.",
        "shortDesc": "You are in your sleeping chamber. To the West is the Hallway.",
        "north": False,
        "east": False,
        "south": False,
        "west": "hallway1",
        "contents": ["bed", "mirror", "wardrobe", "chamberPot"]
    },
    "hallway1": {
        "name": "Hallway",
        "description": "The long Hallway leads to the front door in the West. The walls are covered in hunting trophies and lavish gifts from far away. There is a door that leads to the Weapons Room to the North, as well as a bunch of other doors that lead you to unadventurous parts of the house that are definitely not worthwhile going to.",
        "shortDesc": "The front door is further West. The Weapons Room is to the North. And there are a bunch of other doors that lead you to unadventurous parts of the house.",
        "north": "weaponsRoom",
        "east": "chamber",
        "south": "utilityCloset",
        "west": "hallway2",
        "contents": ["huntingTrophies", "lavishGifts"]
    },
    "weaponsRoom": {
        "name": "Weapons Room",
        "description": "A dark room filled with racks upon racks of swords and shields, bows and daggers, and even a few war axes. They glitter eerily in the weak light from the few candles scattered across the room. Examine what you see to check if it will suit your journey.",
        "shortDesc": "It's dark in here. Things glitter eerily in the weak light from the few candles scattered across the room.",
        "south": "hallway1",
        "odour": "Mmm...beeswax and dried blood.",
        "contents": ["candles", "warAxe", "dagger", "bow", "sword", "shield"]
    },
    "utilityCloset": {
        "name": "Utility Closet",
        "description": "Well, this is a closet, that's for sure.",
        "shortDesc": "Yup, still a closet.",
        "north": "hallway1",
        "contents": ["dustyShelf", "broom", "bucket"]
    },
    "hallway2": {
        "name": "Hallway",
        "description": "I told you it was long. The door outside is just ahead to the West. Places of no interest are North and South. Your Chamber is far East.",
        "shortDesc": "The door outside is just over to the West. Places of no interest are North and South. Your Chamber is far East.",
        "north": "boringRoom",
        "east": "hallway1",
        "south": "uninterestingRoom",
        "west": "frontGates",
    },
    "boringRoom": {
        "name": "Boring Room",
        "description": "This room is so boring. When you get back from your adventure you should put a life-size statue of yourself in here. Hopefully you'll have slimmed down a bit by then, so that it won't take up the whole room.",
        "shortDesc": "Boooorrring.",
        "south": "hallway2",
    },
    "uninterestingRoom": {
        "name": "Uninteresting Room",
        "description": "Doesn't look like there's anything in here. Don't bother looking around. Certainly no chests in here. You should probably just go back North.",
        "shortDesc": "Still doesn't look like there's anything in here. You should probably just go back North.",
        "north": "hallway2",
        "contents": ["chest"]
    },
    "frontGates": {
        "name": "Front Gates",
        "description": "Ah, fresh air! Something you've clearly not had enough of recently. You are so close to adventure you can smell it. Now you just have to decide where to go.",
        "shortDesc": "That sweet, sweet air! You are so close to adventure you can smell it.",
        "odour": "Smells like adventure!",
        "north": "cavernousMountains",
        "east": "hallway2",
        "west": "darkForest",
        "contents": ["signpost"]
    },
    "cavernousMountains": {
        "name": "Cavernous Mountains",
        "description": "The mountains loom over you. A darkened crack in the northern rock face seems to lead into the mountains.",
        "north": "cave",
        "south": "frontGates",
    },
    "cave": {
        "name": "Cave",
        "description": "It is dark and damp in the cave. There is a crack of light coming from the south entrance. It seems to fall upon a strange stone lying on the ground.",
        "odour": "It smells like stale water and dust.",
        "south": "cavernousMountains"
    },
    "darkForest": {
        "name": "Dark Forest",
        "description": "Large trees surround you, moving quietly in the wind. You can see a faint light coming from the East where you entered. There seems to be a lightly trodden path leading North. The forest becomes denser to the South, with no path in sight; seemingly unexplored land.",
        "odour": "The air coming from the East is fresh. The forest smells like trees and dirt. What else?",
        "north": "troddenPath",
        "east": "frontGates",
        "south": "unexploredForest"
    },
    "unexploredForest": {
        "name": "Unexplored Forest",
        "description": "This part of the forest is wild and thick with trees and bushes. A large oak tree is in front of you. The air seems heavier here; filled with an old magic you don't quite understand.",
        "odour": "The air is humid and still. It smells like a mix of trees and dirt, as well as something you can't quite put your finger on.",
        "north": "darkForest"
    },
    "troddenPath": {
        "name": "Trodden Path",
        "description": "At the north end of the path you see daylight and can faintly smell smoke. Berry bushes line the path.",
        "odour": "The smoke seems to be coming from the north. Maybe there is a bonfire! Or a stake burning! Oh how I love a good stake burning.",
        "north": "theVillage",
        "south": "darkForest"
    },
    "theVillage": {
        "name": "The Village",
        "description": "The village seems to have been attacked! The thatch roofed cottages have been burnt down and it seems like the villagers are in distress!",
        "odour": "The smell of smoke is strong. You start to cough.",
        "south": "troddenPath"
    }
}