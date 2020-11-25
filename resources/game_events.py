#! Python3
# events.py

from .util import write

"""
EVENT OBJECTS SHOULD HANDLE ALL PRINTING
"""

def beginning(game):
    text = [
        "\nYou are an experienced adventurer who has saved kingdoms and rescued damsels in distress. You have slayed dragons and conquered sorcerers and have received generous rewards from Kings and villagers alike for your heroic feats. Now you are looking for your next adventure since you have grown weary of living in the lap of luxury.",
        "\nAnd so your quest begins...the quest for honour, glory, and fair maidens...",
        "\nThe Quest...",
        "\n   for Adventure!\n\n"
    ]
    for line in text:
        write(line)
        input()
    write(game.movePlayer("chamber"))