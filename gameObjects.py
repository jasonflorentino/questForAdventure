# python3
# gameObjects.py

"""____________________

      PLACE CLASS

____________________"""

class Place(object):
    def __init__(self, name="default", visits=0, north=False, east=False,
    south=False, west=False, locked=False, odour=False, shortDesc="default",
    longDesc="default", contents=[]):
        self.name = name
        self.visits = visits
        self.north = north 
        self.east = east
        self.south = south
        self.west = west
        self.locked = locked
        self.odour = odour
        self.shortDesc = shortDesc
        self.longDesc = longDesc
        self.contents = contents
    
    def printContents(self):
        if len(self.contents) == 0:
            print("Nothing of interest.")
        else:
            for item in self.contents:
                if item.visible:
                    print(f"{item.name.title()}, ", end='')
    
    def printLongDesc(self):
        print(self.longDesc)
    
    def printShortDesc(self):
        print(self.shortDesc)

    def addItems(self, *argv):
        for item in argv:
            self.contents.append(item)

"""_________________

     ITEM CLASS

_________________"""

class Item(object):
    def __init__(self, name="default", screenName="default", location="default", 
    visible=True, desc="default", odour=False, takeable=True, takeResp=False,
    useable=True, useResp=False, used=False, reUseable=False, dropResp=False,
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
    
    def addItems(self, *argv):
        for item in argv:
            self.contents.append(item)

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
                if len(self.contents) > 0:
                    self.contents[0].visible = True
                    self.contents[0].takeable = True
                    print(f"There's a {self.contents[0].name} inside.")
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
            print(f"You closed the {self.name}.")
            self.isOpen = False
            if len(self.contents) > 0:
                self.contents[0].visible = False
                self.contents[0].takeable = False
    
    def place(self, item):
        if self.container == False:
            print(f"You can't place {item.name} in the {self.name}.")
        elif self.isOpen == False:
            print(f"{self.name} isn't open.")
        elif len(self.contents) > 0:
            print(f"There's already something in the {self.name}.")
        else:
            print(f"You placed {item.name} in the {self.name}.")
            self.contents.append(item)
            item.location = self.name
    
    def empty(self):
        if self.container == False:
            print(f"You can't empty the {self.name}.")
        elif self.isOpen == False:
            print(f"{self.name} isn't open.")
        elif len(self.contents) == 0:
            print(f"There's nothing in the {self.name}.")
        else:
            print(f"You emptied the {self.name}.")
            return self.contents.pop()

"""_________________

    CREATE ROOMS

_________________"""

chamber = Place("Chamber")
chamber.shortDesc = "You are in your sleeping chamber. To the West is the Hallway."
chamber.longDesc = "You wake up from a restless night's sleep.\nSince you were also knighted for ridding the bog of a bog monster,\nyou could say you woke from a knight's restless night's sleep.\nYou are in your sleeping chamber.\nThere is a door to the West that leads to the Hallway.\nYou should probably get dressed before going out there."
chamber.contents = []

hallway1 = Place("Hallway")
hallway1.shortDesc = "Mounted animal heads stare down at you with their beady, beady eyes. I think the boar just winked at you. The front door is further West. The Weapons Room is to the North. And there are a bunch of other doors that lead you to unadventurous parts of the house."
hallway1.longDesc = "The long Hallway leads to the front door in the West. The walls are covered in hunting trophies and lavish gifts from far away. There is a door that leads to the Weapons Room to the North, as well as a bunch of other doors that lead you to unadventurous parts of the house that are definitely not worthwhile going to."
hallway1.contents = []

weaponsRoom = Place("Weapons Room")
weaponsRoom.odour = "Mmm...beeswax and dried blood."
weaponsRoom.shortDesc = "It's dark in here. Things glitter eerily in the weak light from the few candles scattered across the room."
weaponsRoom.longDesc = "A dark room filled with racks upon racks of swords and shields, bows and daggers, and even a few war axes. They glitter eerily in the weak light from the few candles scattered across the room. Examine what you see to check if it will suit your journey."
weaponsRoom.contents = []

utilityCloset = Place("Utility Closet")
utilityCloset.shortDesc = "Yup, still a closet."
utilityCloset.longDesc = "Well, this is a closet, that's for sure."
utilityCloset.contents = []

hallway2 = Place("Hallway")
hallway2.shortDesc = "The door outside is just over to the West. Places of no interest are North and South. Your Chamber is far East."
hallway2.longDesc = "I told you it was long. The door outside is just ahead to the West. Places of no interest are North and South. Your Chamber is far East."
hallway2.contents = []

boringRoom = Place("Boring Room")
boringRoom.shortDesc = "Boooorrring."
boringRoom.longDesc = "This room is so boring. When you get back from your adventure you should put a life-size statue of yourself in here. Hopefully you'll have slimmed down a bit by then, so that it won't take up the whole room."
boringRoom.contents = []

uninterestingRoom = Place("Uninteresting Room")
uninterestingRoom.shortDesc = "Doesn't look like there's anything in here. You should probably just go back North."
uninterestingRoom.longDesc = "Doesn't look like there's anything in here. Don't bother looking around. Certainly no chests in here. You should probably just go back North."
uninterestingRoom.contents = []

frontGates = Place("Front Gates")
frontGates.odour = "Smells like adventure!"
frontGates.shortDesc = "Ah, fresh air! You are so close to adventure you can smell it. Now you just have to decide where to go."
frontGates.longDesc = "Ah, fresh air! Something you've clearly not had enough of recently. You are so close to adventure you can smell it. Now you just have to decide where to go."
frontGates.contents = []

"""_________________

    CREATE ITEMS

_________________"""

lint = Item("lint", "lint", "hallway", True,
"It's lint",
False, True, "Um, okay.", False, False, False, False, False, False, False, False, [])

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
False, False, False, True, True, False, [])

wardrobe = Item("wardrobe", "wardrobe", "default", True,
"A large mahogany wardrobe.",
"This smells like grandma: mothballs and disappointment.",
False, False, False, False, False, False, False, True, True, False, [])

armour = Item("armour", "armour", "default", False,
"Ooooh...shiny.", "Smells like metal. Who would have thought?",
False,
"Oof! This weighs a tonne! You've been sitting around too long in your underpants eating sweets. You should put the armour on so you can at least look the part.",
True,
"It fits you like a glove. It looks like your boots could be buffed out a bit though. You should examine the mirror to see how you look.",
False, True, False, False, False, False, [])

huntingTrophies = Item("hunting trophies", "hunting trophies")
huntingTrophies.desc = "Every type of animal head imaginable is up on this wall."
huntingTrophies.takeable = False

lavishGifts = Item("lavish gifts", "lavish gifts")
lavishGifts.desc = "Oooh...shiny. Lots of gold this and bejewelled that up here."
lavishGifts.takeable = False


"""____________________________

    ASSIGN ITEMS & DIRECTIONS

____________________________"""

allItems = {
    "lint": lint,
    "bed": bed,
    "mirror": mirror,
    "chamber pot": chamberPot,
    "wardrobe": wardrobe,
    "armour": armour,
    "hunting trophies": huntingTrophies,
    "lavish gifts": lavishGifts,
}

chamber.addItems(lint, bed, mirror, chamberPot, wardrobe)

wardrobe.addItems(armour)

hallway1.addItems(huntingTrophies, lavishGifts)



chamber.west = hallway1

hallway1.east = chamber
hallway1.north = weaponsRoom
hallway1.south = utilityCloset
hallway1.west = hallway2

weaponsRoom.south = hallway1

utilityCloset.north = hallway1

hallway2.north = boringRoom
hallway2.east = hallway1
hallway2.south = uninterestingRoom
hallway2.west = frontGates

boringRoom.south = hallway2

uninterestingRoom.north = hallway2

frontGates.east = hallway2