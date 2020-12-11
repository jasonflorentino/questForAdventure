#! Python3
# game_actions.py

from .response import Response

def move(game, userIn, direction=False):
    response = Response("move")

    if not direction:
        direction = input("In what direction do you want to move?\n>> ").lower()
        if direction in ("north", "east", "south", "west"):
            pass
        else:
            return response.addToPrint("That's not a direction\n").setStatus_BadInput()

    # Check if there's a room at given direction
    newLocation = game.getDirectionTarget(direction)

    if newLocation:
        return game.movePlayer(newLocation, response).setGameStatus(direction)
    else:
        return response.addToPrint("You can't go that way.\n").setStatus_FailedAction(f"No room at {direction}")

def north(game, userIn):
    return move(game, userIn, "north")

def south(game, userIn):
    return move(game, userIn, "south")

def east(game, userIn):
    return move(game, userIn, "east")

def west(game, userIn):
    return move(game, userIn, "west")

def help_(game, userIn):
    pass

def inventory(game, userIn):
    pass

def look(game, userIn):
    response = Response("look")

    game.getStatus(response)
    game.getRoomContents(response)
    return response.setGameStatus("Room Status")

def quit_(game, userIn):
    response = Response("quit")

    while True:
        sure = input("Are you sure you want to quit? (y/n)\n>> ").lower()
        if sure in ("y", "yes", "n", "no"):
            break
    if sure in ("y", "yes"):
        response.addToPrint("Quitting...\n").setGameStatus("quit")
        return response
    else:
        response.addToPrint("I knew you still had it in you!\n").setGameStatus("continue")
        return response

def xyzzy(game, userIn):
    pass

def cast(game, userIn):
    pass

def close(game, userIn):
    pass

def drop(game, userIn):
    pass

def place(game, userIn):
    pass

def take(game, userIn):
    pass

def talk(game, userIn):
    pass

def smell(game, userIn):
    pass

def open_(game, userIn):
    pass

def use(game, userIn):
    pass

def empty(game, userIn):
    pass

def examine(game, userIn):
    response = Response("examine")

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