#! Python3
# rooms.py

"""
ROOM CLASS
"""

class Room():
    def __init__(self, name, description, shortDesc, north, east, south, west):
        self.name = name
        self.description = description
        self.shortDesc = shortDesc
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.visits = 0
        self.contents = []
    
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

"""
GENERATE ROOM OBJECTS
"""

def createRooms():
    roomObjects = {}
    for room in roomData.keys():
        name = roomData[room]["name"]
        description = roomData[room]["description"]
        shortDesc = roomData[room]["shortDesc"]
        north = roomData[room]["north"]
        east = roomData[room]["east"]
        south = roomData[room]["south"]
        west = roomData[room]["west"]

        roomObjects[room] = Room(name, description, shortDesc, north, east, south, west)

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
    },
    "chamber": {
        "name": "Chamber",
        "description": "You wake up from a restless night's sleep.\nSince you were also knighted for ridding the bog of a bog monster,\nyou could say you woke from a knight's restless night's sleep.\nYou are in your sleeping chamber.\nThere is a door to the West that leads to the Hallway.\nYou should probably get dressed before going out there.",
        "shortDesc": "You are in your sleeping chamber. To the West is the Hallway.",
        "north": False,
        "east": False,
        "south": False,
        "west": "hallway1",
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
}