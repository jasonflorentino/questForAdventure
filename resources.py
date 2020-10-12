#! Python3
# resources.py - class and functions definitions for main game.

from time import sleep

from gameData import gameData

def write(text):
    for letter in text:
        print(letter, end='', flush=True)
        # sleep(.02) # Uncomment for slow printing

class Game(object):
    def __init__(self, name):
        self.name = name
        self.player = globals()['gameData']['player']
        self.items = globals()['gameData']['items']
        self.places = globals()['gameData']['places']
        self.turnCount = 0

    def incrementTurn(self):
        self.turnCount += 1

    def changeName(self, newName):
        self.name = newName
    
    def printName(self):
        print('The game name is ' + self.name)

    def changeCurrentLocation(self, newLocation):
        self.player['currentLocation'] = newLocation
        
    def printCurrentLocation(self):
        print('[%s]' % self.player['currentLocation'])
    
    def beginning(self):
        text = [
            "\nYou are an experienced adventurer who has saved kingdoms and rescued damsels in distress. You have slayed dragons and conquered sorcerers and have received generous rewards from Kings and villagers alike for your heroic feats. Now you are looking for your next adventure since you have grown weary of living in the lap of luxury.",
            "\nAnd so your quest begins...the quest for honour, glory, and fair maidens...",
            "\nThe Quest...",
            "\n   for Adventure!\n\n"
        ]
        for line in text:
            write(line)
            input()
        self.printCurrentLocation()
        write(self.places["chamber"]["longDesc"] + "\n")
        self.turnCount += 1

# game = Game('test')
# game.printCurrentLocation()
# game.changeCurrentLocation(game.places['hallway1']['screenName'])
# game.printCurrentLocation()
