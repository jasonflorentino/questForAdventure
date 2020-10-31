# python3
# player.py

class Player(object):
    def __init__(self, name="default", currentLocation="default",
    inventory=[], turnCount=0):
    self.name = name
    self.currentLocation = currentLocation
    self.inventory = inventory
    self.turnCount = turnCount