import os
import textwrap

from room import Room
from item import Item
from player import Player

# Clear console
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Declare all the rooms + items

items = {
    "gold": Item("Gold", "10g of solid gold"),
    "dust": Item("Dust", "Worthless piece of dust"),
    "mineral": Item("Mineral", "Rare mineral"),
    "gun": Item("Gun", "An old rifle"),
}

room = {
    "outside":  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [items["dust"]]),

    "foyer":    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                    [items["dust"], items["mineral"]]),

    "overlook": Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                    [items["gun"]]),

    "narrow":   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                    [items["dust"], items["mineral"]]),

    "treasure": Room("Treasure Chamber", """You"ve found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                    [items["gold"]]),
}


# Link rooms together

room["outside"].n_to  = room["foyer"]
room["foyer"].s_to    = room["outside"]
room["foyer"].n_to    = room["overlook"]
room["foyer"].e_to    = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to   = room["foyer"]
room["narrow"].n_to   = room["treasure"]
room["treasure"].s_to = room["narrow"]

#
# Main
#

# Make a new player object that is currently in the "outside" room.
player = Player("player1", room["outside"])

# Log list for a given REPL loop
replLog = []

# Dict to get full cardinal direction
direction = {
    "n": "north",
    "s": "south",
    "e": "east",
    "w": "west",
}

# Check if an item exists
# in a specifc room
# def itemExistsInRoom(item, room):
#     doesExist = False
#
#     for roomItem in room.items:
#         if item.lower() == roomItem.name.lower():
#             doesExist = True
#             break
#
#     return doesExist

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn"t allowed.
#
# If the user enters "q", quit the game.
while True:
    # Clear terminal
    # -> reduces terminal pollution
    clear()

    # Print current player location
    for log in replLog:
        print(f"> {log}")

    # Reset log array
    replLog = []

    # Print Player's current location
    print("\nLocation:")
    print(f"-- {player.current_room.name}")
    print(f"{textwrap.fill(player.current_room.description, 50)}")

    # Print room items
    print("\nRoom Items:")
    for i in player.current_room.items:
        print(f"-> {i.name} ({i.description})")

    # Ask user where to go
    # (accepts a cardinal direction)
    choice = input("\nWhere do you want to go? (#): ")
    print()

    # Split each word entered into a
    # different value within an array
    choices = choice.split(" ")

    try:
        if choice == "q":
            break

        # Validate user input
        # -> accept cardinal direction
        if len(choices) == 1:
            if choice in ["n", "e", "s", "w"]:
                replLog.append(f"Going {direction[choice]}")

                # Check if room exists
                if hasattr(player.current_room, f"{choice}_to"):
                    # Move player into room
                    player.current_room = getattr(player.current_room, f"{choice}_to")
                    replLog.append(f"Found room: {player.current_room.name}")

                else:
                    # Room does not exist
                    replLog.append(f"No room found to the {direction[choice]}")
            else:
                replLog.append("Not a cardinal direction!")

        else:
            # Pick an item up
            # in current room
            if choices[0].lower() == "get" or choices[0].lower() == "take":
                # Check if item exists in current room
                if player.current_room.itemExists(choices[1]):
                    # Add item to inventory
                    player.addToInventory(items[choices[1].lower()])

                    # Remove item from room
                    player.current_room.removeItem(choices[1])

                    replLog.append(f"Picked up item -> {choices[1]}")

                # Item does not exist
                else:
                    replLog.append(f"Item, {choices[1]}, could not be found!")

            # Drop an item in player's
            # inventory
            elif choices[0].lower() == "drop":
                # Check if player has item
                if player.itemExists(choices[1]):
                    # Remove item from inventory
                    player.removeFromInventory(choices[1])

                    # Add item to current room
                    player.current_room.addItem(items[choices[1].lower()])

                    replLog.append(f"Dropped item -> {choices[1]}")
                else:
                    replLog.append(f"Item, {choices[1]}, is not in inventory!")

            else:
                replLog.append("Not a valid command!")

    except:
        replLog.append("Somthing went wrong! :(")
