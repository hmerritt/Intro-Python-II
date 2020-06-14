# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.items = items

    def itemExists(self, item):
        doesExist = False

        for roomItem in self.items:
            if item.lower() == roomItem.name.lower():
                doesExist = True
                break

        return doesExist

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        itemRemoved = False

        for roomItemIndex, roomItem in enumerate(self.items):
            if item.lower() == roomItem.name.lower():
                del self.items[roomItemIndex]
                itemRemoved = True
                break

        return itemRemoved
