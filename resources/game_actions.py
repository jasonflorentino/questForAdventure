#! Python3
# game_actions.py

from .response import Response

def move(game, inputObject, direction=False):
    response = Response()
    if not direction:
        direction = input("In what direction do you want to move?\n>> ").lower()
        if direction in ("north", "east", "south", "west"):
            pass
        else:
            response.addToPrint("That's not a direction")
            response.setGameStatus("Invalid Input")
            return response

    newLocation = game.getDirectionTarget(direction) # Check if there's a room at given direction
    if newLocation:
        response.addToPrint(game.movePlayer(newLocation))
        response.setGameStatus(direction)
        return response
    else:
        response.addToPrint("You can't go that way.")
        response.setGameStatus("No room at desired direction")
        return response

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
    response = Response()
    print(game.getStatus())
    game.activeRoom.listContents(game)
    response.addToPrint("").setGameStatus("Room Status")
    return response

def quit_(game, inputObject):
    response = Response()
    while True:
        sure = input("Are you sure you want to quit? (y/n)\n>> ").lower()
        if sure in ("y", "yes", "n", "no"):
            break
    if sure in ("y", "yes"):
        response.addToPrint("Quitting...").setGameStatus("quit")
        return response
    else:
        response.addToPrint("I knew you still had a bit in you").setGameStatus("continue")
        return response

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

def examine(game, userIn):
    response = Response()
    if not userIn.word2:
        userIn.word2 = input("What do you want to examine?\n>> ").lower()
    if not userIn.word2 in game.activeRoom.contents:
        response.addToPrint(f"There is no {userIn.word2} here.\n")
        response.setGameStatus("Item doesn't exist")
        return response
    else:
        output = f"You examine the {userIn.word2}...\n" + game.objects[userIn.word2].description + "\n"
        response.addToPrint(output).setGameStatus("examine")
        return response

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

# Each action function => response object based on querries to Game
def execute(game, userInputObject):
    return actionsDict[userInputObject.word1](game, userInputObject)