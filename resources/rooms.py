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

    def addToContents(self, itemString):
        self.contents.append(itemString)
        return self
    
    def removeFromContents(self, itemString):
        if not itemString in self.contents:
            self.contents.remove(itemString)
            return self
        else:
            print(f"Item not in contents of {self.name}.")
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
    
    def listContents(self):
        if len(self.contents) >= 1:
            print("You see:")
            for item in self.contents:
                print("- " + item.title())
        else:
            print("You see nothing of interest.")


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
        "contents": ["bed", "mirror"]
    },
    "hallway1": {
        "name": "Hallway",
        "description": "The long Hallway leads to the front door in the West. The walls are covered in hunting trophies and lavish gifts from far away. There is a door that leads to the Weapons Room to the North, as well as a bunch of other doors that lead you to unadventurous parts of the house that are definitely not worthwhile going to.",
        "shortDesc": "Mounted animal heads stare down at you with their beady, beady eyes. I think the boar just winked at you. The front door is further West. The Weapons Room is to the North. And there are a bunch of other doors that lead you to unadventurous parts of the house.",
        "north": "weaponsRoom",
        "east": "chamber",
        "south": "utilityCloset",
        "west": "hallway2",
    },
    "weaponsRoom": {
        "name": "Weapons Room",
        "description": "A dark room filled with racks upon racks of swords and shields, bows and daggers, and even a few war axes. They glitter eerily in the weak light from the few candles scattered across the room. Examine what you see to check if it will suit your journey.",
        "shortDesc": "It's dark in here. Things glitter eerily in the weak light from the few candles scattered across the room.",
        "south": "hallway2",
        "odour": "Mmm...beeswax and dried blood.",
    },
    "utilityCloset": {
        "name": "Utility Closet",
        "description": "Well, this is a closet, that's for sure.",
        "shortDesc": "Yup, still a closet.",
        "north": "hallway1",
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
        "shortDesc": "Doesn't look like there's anything in here. You should probably just go back North.",
        "north": "hallway2",
    },
    "frontGates": {
        "name": "Front Gates",
        "description": "Ah, fresh air! Something you've clearly not had enough of recently. You are so close to adventure you can smell it. Now you just have to decide where to go.",
        "shortDesc": "Ah, fresh air! You are so close to adventure you can smell it. Now you just have to decide where to go.",
        "odour": "Smells like adventure!",
        "east": "hallway2"
    }
}