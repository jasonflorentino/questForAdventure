#! Python3
# resources.py - class and functions definitions for main game.

from gameData import gameData

def parseUserInput(userInput):
    text = userInput
    return text

class Game(object):
    def __init__(self, name):
        self.name = name
        self.player = globals()['gameData']['player']
        self.items = globals()['gameData']['items']
        self.places = globals()['gameData']['places']

    def changeName(self, newName):
        self.name = newName
    
    def printName(self):
        print('The game name is ' + self.name)

    def changeCurrentLocation(self, newLocation):
        self.player['currentLocation'] = newLocation
        
    def printCurrentLocation(self):
        print('Currently you are in ' + self.player['currentLocation'])

# game = Game('test')
# game.printCurrentLocation()
# game.changeCurrentLocation(game.places['hallway1']['screenName'])
# game.printCurrentLocation()
