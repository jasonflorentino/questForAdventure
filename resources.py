#! Python3
# resources.py - class and functions definitions for main game.

class Game(object):
    def __init__(self, name):
        self.name = name
        self.player = {}
        self.items = {}
        self.places = {}