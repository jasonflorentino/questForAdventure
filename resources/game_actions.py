#! Python3
# game_actions.py

from .response import Response
from .util import toCamelCase

def move(game, userIn, direction=False):
    response = Response("move")

    if not direction:
        direction = input("In what direction do you want to move?\n>> ").lower()
        if direction in ("north", "east", "south", "west"):
            pass
        else:
            return response.add("That's not a direction\n").setStatus_BadInput()

    newLocation = game.getDirectionTarget(direction)

    if newLocation:
        return game.movePlayer(newLocation, response).status(direction)
    else:
        return response.add("You can't go that way.\n").setStatus_FailedAction(f"No room at {direction}")

def north(game, userIn):
    return move(game, userIn, "north")

def south(game, userIn):
    return move(game, userIn, "south")

def east(game, userIn):
    return move(game, userIn, "east")

def west(game, userIn):
    return move(game, userIn, "west")

def help_(game, userIn):
    response = Response("help")
    if game.helpCounter < 1:
        response.add("You call for help...\nThere's no answer.")
    elif game.helpCounter < 2:
        response.add("Well, if I helped you that wouldn't be any fun now would it?")
    elif game.helpCounter < 3:
        response.add("I don't know, try a verb?")
    elif game.helpCounter < 4:
        response.add("You tried that verb already...")
    elif game.helpCounter < 5:
        response.add("Here's one: 'quit'")
    else:
        response.add("You call for help...\nThere's no answer.")
    game.incrementHelpCounter()
    response.add("")
    return response

def inventory(game, userIn):
    response = Response("inventory")
    game.listInventory(response)
    return response.status("Show inventory")

def look(game, userIn):
    response = Response("look")
    game.getRoomContents(response)
    return response.status("Room Status")

def quit_(game, userIn):
    response = Response("quit")

    while True:
        sure = input("Are you sure you want to quit? (y/n)\n>> ").lower()
        if sure in ("y", "yes", "n", "no"):
            break
    if sure in ("y", "yes"):
        response.add("Quitting...\n").status("quit")
        return response
    else:
        response.add("I knew you still had it in you!\n").status("continue")
        return response

def xyzzy(game, userIn):
    pass

def cast(game, userIn):
    pass

def close(game, userIn):
    response = Response("close")
    if not userIn.hasSecondInput():
       userIn.setSecondInput(input("What do you want to close?\n>> ").lower())
    toClose = toCamelCase(userIn.secondInput())
    return game.closeItem(response, toClose)

def drop(game, userIn):
    response = Response("drop")
    if not userIn.hasSecondInput():
        userIn.setSecondInput(input("What do you want to drop?\n>> ").lower())
    toDrop = toCamelCase(userIn.secondInput())
    return game.dropItem(response, toDrop)

def put(game, userIn):
    response = Response("put")
    if not userIn.hasSecondInput():
        userIn.setSecondInput(input("What do you want to put?\n>> ").lower())
    toPut = toCamelCase(userIn.secondInput())
    return game.putItem(response, toPut)

def take(game, userIn):
    response = Response("take")
    if not userIn.hasSecondInput():
        userIn.setSecondInput(input("What do you want to take?\n>> ").lower())
    toTake = toCamelCase(userIn.secondInput())
    return game.takeItem(response, toTake)

def talk(game, userIn):
    pass

def smell(game, userIn):
    response = Response("smell")
    if not userIn.hasSecondInput():
        game.smellRoom(response)
    else:
        toSmell = toCamelCase(userIn.secondInput())
        game.smellItem(response, toSmell)
    return response

def open_(game, userIn):
    response = Response("open")
    if not userIn.hasSecondInput():
       userIn.setSecondInput(input("What do you want to open?\n>> ").lower())
    toOpen = toCamelCase(userIn.secondInput())
    return game.openItem(response, toOpen)

def use(game, userIn):
    pass

def empty(game, userIn):
    response = Response("empty")
    if not userIn.hasSecondInput():
       userIn.setSecondInput(input("What do you want to empty?\n>> ").lower())
    toEmpty = toCamelCase(userIn.secondInput())
    return game.emptyItem(response, toEmpty)

def examine(game, userIn):
    response = Response("examine")
    if not userIn.hasSecondInput():    # Get a target if none was given
        userIn.setSecondInput(input("What do you want to examine?\n>> ").lower())
    itemKey = toCamelCase(userIn.word2)
    return game.examineItem(response, itemKey)

def wear(game, userIn):
    response = Response("wear")
    if not userIn.hasSecondInput():
        userIn.setSecondInput(input("What do you want to wear?\n>> ").lower())
    toWear = toCamelCase(userIn.word2)
    return game.wearItem(response, toWear)

def remove(game, userIn):
    response = Response("remove")
    if not userIn.hasSecondInput():
        userIn.setSecondInput(input("What do you want to remove?\n>> ").lower())
    toWear = toCamelCase(userIn.word2)
    return game.removeItem(response, toWear)

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
    "put":put,
    "quit":quit_,
    "remove":remove,
    "smell":smell,
    "take":take,
    "talk":talk,
    "use":use,
    "wear":wear,
    "xyzzy":xyzzy,
    }

# Each action function => response object based on querries to Game
def execute(game, userInputObject):
    return actionsDict[userInputObject.word1](game, userInputObject)