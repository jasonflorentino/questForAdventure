#! Python3
# game_actions.py

def move(game, inputObject, direction=False):
    if not direction:
        direction = input("In what direction do you want to move?\n> ").lower()
        if direction in ("north", "east", "south", "west"):
            pass
        else:
            return ("That's not a direction", "Invalid Input")
    
    newLocation = game.rooms[game.player.currentLocation].getNextRoom(direction)
    if newLocation:
        textToPrint = game.movePlayer(newLocation)  
        actionToEval = direction
        return (textToPrint, actionToEval)
    else:
        return ("You can't go that way.", "No room at desired direction")

def north(game, inputObject):
    return move(game, inputObject, "north")

def south(game, inputObject):
    return move(game, inputObject, "south")

def east(game, inputObject):
    return move(game, inputObject, "east")

def west(game, inputObject):
    return move(game, inputObject, "west")

def help_(game, inputObject):
    pass

def inventory(game, inputObject):
    pass

def look(game, inputObject):
    pass

def quit_(game, inputObject):
    while True:
        sure = input("Are you sure you want to quit? (y/n)\n> ").lower()
        if sure in ("y", "yes", "n", "no"):
            break
    if sure in ("y", "yes"):
        return ("Quitting...", "quit")
    else:
        return ("I knew you still had a bit in you", "continue")

def xyzzy(game, inputObject):
    pass

def cast(game, inputObject):
    pass

def close(game, inputObject):
    pass

def drop(game, inputObject):
    pass

def place(game, inputObject):
    pass

def take(game, inputObject):
    pass

def talk(game, inputObject):
    pass

def smell(game, inputObject):
    pass

def open_(game, inputObject):
    pass

def use(game, inputObject):
    pass

def empty(game, inputObject):
    pass

def examine(game, inputObject):
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

