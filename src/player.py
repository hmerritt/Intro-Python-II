# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, inventory = []):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def itemExists(self, item):
        doesExist = False

        for invItem in self.inventory:
            if item.lower() == invItem.name.lower():
                doesExist = True
                break

        return doesExist

    def addToInventory(self, item):
        self.inventory.append(item)

    def removeFromInventory(self, item):
        itemRemoved = False

        for invItemIndex, invItem in enumerate(self.inventory):
            if item.lower() == invItem.name.lower():
                del self.inventory[invItemIndex]
                itemRemoved = True
                break

        return itemRemoved
