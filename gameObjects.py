# python3
# gameObjects.py

"""____________________

    CLASS DEFINITIONS

____________________"""

class Place(object):
    def __init__(self, name="default", visits=0, north=False, east=False,
    south=False, west=False, locked=False, odor=False, shortDesc="default",
    longDesc="default", contents=[]):
        self.name = name
        self.visits = visits
        self.north = north 
        self.east = east
        self.south = south
        self.west = west
        self.locked = locked
        self.odor = odor
        self.shortDesc = shortDesc
        self.longDesc = longDesc
        self.contents = contents
    
    def printContents(self):
        if len(self.contents) == 0:
            print("Nothing of interest.")
        else:
            for item in self.contents:
                print(item.name.title())
    
    def printLongDesc(self):
        print(self.longDesc)
    
    def printShortDesc(self):
        print(self.shortDesc)

class Item(object):
    def __init__(self, name="default", screenName="default", location="default", 
    visible=True, desc="default", odour=False, takeable=True, takeResp = "default",
    useable=True, useResp="default", used=False, reUseable=False, dropResp="default",
    container=False, closeable=False, isOpen=False, contents=[]):
        self.name = name
        self.screenName = screenName
        self.location = location
        self.visible = visible
        self.desc = desc
        self.odour = odour
        self.takeable = takeable
        self.takeResp = takeResp
        self.useable = useable
        self.useResp = useResp
        self.used = used
        self.reUseable = reUseable
        self.dropResp = dropResp
        self.container = container
        self.closeable = closeable
        self.isOpen = isOpen
        self.contents = contents

    def printDesc(self):
        print(self.desc)
    
    def printName(self):
        print(self.name.title())
    
    def use(self):
        if self.use == False:
            print("You can't use that.")
            return False
        elif self.used == True and self.reUseable == False:
            print("You've already used that.")
            return False
        else:
            print(self.useResp)
            if self.reUsable == False:
                self.used = True
    
    def open(self):
        if self.container == True:
            if self.isOpen == False:
                print(f"You opened the {self.name}.")
                self.isOpen = True
            else:
                print(f"The {self.name} is already open.")
        else:
            print(f"You can't open that")
    
    def close(self):
        if self.container == False:
            print("You can't close that.")
        elif self.closeable == False:
            print(f"The {self.name} can't be closed.")
        elif self.isOpen == False:
            print(f"The {self.name} is already closed.")
        else:
            print(f"You closed the {self.name}")
            self.isOpen = False
    
    def put(self, item):
        if self.container == False:
            print(f"You can't put {item.name} in the {self.name}.")
        elif self.isOpen == False:
            print(f"{self.name} isn't open.")
        else:
            print(f"You put {item.name} in the {self.name}.")
            self.contents.append(item)

"""_________________

    CREATE ROOMS

_________________"""

chamber = Place("Chamber", 0, False, False, False, False, False, False,
"You are in your sleeping chamber. To the West is the Hallway.",
"You wake up from a restless night's sleep.\nSince you were also knighted for ridding the bog of a bog monster,\nyou could say you woke from a knight's restless night's sleep.\nYou are in your sleeping chamber.\nThere is a door to the West that leads to the Hallway.\nYou should probably get dressed before going out there.",
)

hallway1 = Place("Hallway", 0, False, False, False, False, False, False,
"Mounted animal heads stare down at you with their beady, beady eyes. I think the boar just winked at you. The front door is further West. The Weapons Room is to the North. And there are a bunch of other doors that lead you to unadventurous parts of the house.",
"The long Hallway leads to the front door in the West. The walls are covered in hunting trophies and lavish gifts from far away. There is a door that leads to the Weapons Room to the North, as well as a bunch of other doors that lead you to unadventurous parts of the house that are definitely not worthwhile going to.",
[])

"""_________________

    CREATE ITEMS

_________________"""

bed = Item("bed", "bed", "chamber", True,
"It is comfortable and warm. No place for an Adventurer like yourself!",
"The sweet smell of fresh linen and days wasted.",
False, False, True,
"I guess we could just forget this whole adventure thing that happens to be *your calling in life*. Or you could get up, you lazy, son of a bar wench",
False, True, False, False, False, False, [])

mirror = Item("mirror", "mirror", "chamber", True,
"You can't help but wonder if the chain-mail makes your butt look big.",
False, False, False, True,
"You can't help but wonder if the chain-mail makes your butt look big.",
False, True, False, False, False, False, [])

chamberPot = Item("chamber pot", "chamber pot", "chamber", True,
"Why would you want to look at that? Gross.",
"Urrgh. Why would you do that? You know what goes in there!",
True,
"Why? I guess you could gross out your enemies with this.",
True,
"You feel ... relieved.",
False, False, False, True, False, True, [])

"""____________________________

    ASSIGN ITEMS & DIRECTIONS

____________________________"""

for item in (bed, mirror, chamberPot):
    chamber.contents.append(item)

# hallway1.contents.append(chamberPot)

chamber.west = hallway1
hallway1.east = chamber

allItems = {
    "bed": bed,
    "mirror": mirror,
    "chamber pot": chamberPot,
}
