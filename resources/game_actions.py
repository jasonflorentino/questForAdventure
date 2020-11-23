#! Python3
# game_actions.py

def move(game, direction=False):
    if not direction:
        direction = input("In what direction do you want to move?\n> ").lower()
        if direction in ("north", "east", "south", "west"):
            pass
        else:
            return ("That's not a direction", "Invalid Input")
    textToPrint = f"You went {direction}"
    actionToEval = direction
    return (textToPrint, actionToEval)

def north(game):
    return move(game, "north")

def south(game):
    return move(game, "south")

def east(game):
    return move(game, "east")

def west(game):
    return move(game, "west")

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

