gameData = {
    "player": {
        "game": "new",
        "currentLocation": "Chamber",
        "inventory": []
    },
    "places": {
        "chamber": {
            "screenName": "Chamber",
            "visits": 0,
            "north": False, 
            "east": False,
            "south": False,
            "west": "hallway1",
            "locked": False,
            "odour": False,
            "shortDesc": "You are in your sleeping chamber. To the West is the Hallway.",
            "longDesc": "You wake up from a restless night's sleep.\nSince you were also knighted for ridding the bog of a bog monster,\nyou could say you woke from a knight's restless night's sleep.\nYou are in your sleeping chamber.\nThere is a door to the West that leads to the Hallway.\nYou should probably get dressed before going out there."
        },
        "hallway1": {
            "screenName": "Hallway",
            "visits": 0,
            "north": "weaponsRoom", 
            "east": "chamber",
            "south": "utilityCloset",
            "west": "hallway2",
            "locked": False,
            "odour": False,
            "shortDesc": "Mounted animal heads stare down at you with their beady, beady eyes. I think the boar just winked at you. The front door is further West. The Weapons Room is to the North. And there are a bunch of other doors that lead you to unadventurous parts of the house.",
            "longDesc": "The long Hallway leads to the front door in the West. The walls are covered in hunting trophies and lavish gifts from far away. There is a door that leads to the Weapons Room to the North, as well as a bunch of other doors that lead you to unadventurous parts of the house that are definitely not worthwhile going to."
        }
    },
    "items": {
        "template": {
            "screenName": "a template",
            "location": "somewhere",
            "visible": False,
            "desc": False,
            'odour': False,
            'takeable': False,
            'takeResp': False,
            'useable': False,
            'useResp': False,
            'inUse': False,
            'reUseable': False,
            'dropResp': False,
            'container': False,
            'closeable': False,
            'open': False,
            'contents': []
            },
        "bed": {
            "screenName": "your bed",
            "location": "chamber",
            "visible": True,
            "desc": "It is comfortable and warm. No place for an Adventurer like yourself!",
            'odour': "The sweet smell of fresh linen and days wasted.",
            'takeable': False,
            'takeResp': False,
            'useable': True,
            'useResp': "I guess we could just forget this whole adventure thing that happens to be *your calling in life*. Or you could get up, you lazy, son of a bar wench",
            'inUse': False,
            'reUseable': True,
            'dropResp': False,
            'container': False,
            'closeable': False,
            'open': False,
            'contents': []
        }
    }
}