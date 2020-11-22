#! Python3
# game_actions.py

def north(game):
    textToPrint = "You went north"
    actionToEval = "north"
    return (textToPrint, actionToEval)

def south(game):
    pass

def east(game):
    pass

def west(game):
    pass

def help_(game):
    pass

def inventory(game):
    pass

def look(game):
    pass

def quit_(game):
    pass

def xyzzy(game):
    pass

def cast(game):
    pass

def close(game):
    pass

def drop(game):
    pass

def place(game):
    pass

def take(game):
    pass

def talk(game):
    pass

def smell(game):
    pass

def open_(game):
    pass

def use(game):
    pass

def empty(game):
    pass

def examine(game):
    pass

def move(game):
    pass

actionsDict = {
    "north":north,
    "south":south,
    "east":east,
    "west":west,
    "cast":cast,
    "close":close,
    "drop":drop,
    "empty":empty,
    "examine":examine,
    "help":help_,
    "inventory":inventory,
    "look":look,
    "move":move,
    "open":open_,
    "place":place,
    "quit":quit_,
    "smell":smell,
    "take":take,
    "talk":talk,
    "use":use,
    "xyzzy":xyzzy,
    }

