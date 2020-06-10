import os
import textwrap

from room import Room
from player import Player

# Clear console
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Declare all the rooms

room = {
    "outside":  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    "foyer":    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    "overlook": Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    "narrow":   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    "treasure": Room("Treasure Chamber", """You"ve found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

    # Ask user where to go
    # (accepts a cardinal direction)
    choice = input("\nWhere do you want to go? (#): ")
    print()

    try:
        if choice == "q":
            break

        # Validate user input
        # -> accept cardinal direction
        if choice in ["n", "e", "s", "w"]:
            # Check if room exists
            if hasattr(player.current_room, f"{choice}_to"):
                # Move player into room
                player.current_room = getattr(player.current_room, f"{choice}_to")
                replLog.append(f"Entered room: {player.current_room.name}")

            else:
                # Room does not exist
                replLog.append("Room does not exist!")

        else:
            replLog.append("Not a valid cardinal direction!")

    except:
        replLog.append("Somthing went wrong! :(")
