
TYPE_PERSON = 1
TYPE_ROOM = 2
TYPE_WEAPON = 4
COUNT_TYPES = 3

class Card:

    def __init__(self, type, name):
        self.type = type
        self.name = name

    def __repr__(self):
        return self.name