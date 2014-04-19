
TYPE_PERSON = 'person'
TYPE_ROOM = 'room'
TYPE_WEAPON = 'weapon'
TYPES = (TYPE_PERSON, TYPE_ROOM, TYPE_WEAPON)
COUNT_TYPES = len(TYPES)

class Card:

    def __init__(self, type, name):
        self.type = type
        self.name = name

    def __repr__(self):
        return self.name