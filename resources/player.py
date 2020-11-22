# python3
# player.py

class Player(object):
    def __init__(self, name="Player 1"):
        self.name = name
        self.currentLocation = None
        self.inventory = []