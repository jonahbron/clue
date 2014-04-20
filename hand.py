
class Hand:

    def __init__(self, count=0, has=[], lacks=[]):
        self.count = max(count, len(has))
        self.has_set = set(has)
        self.lacks_set = set(lacks)
        self.eliminations_set = set()

    def has(self, card):
        self.has_set.add(card)
        # Remove from lacks
        self.__eliminate()
        # Notify all other hands

    def elimination(self, cards):
        self.eliminations_set.add(frozenset(cards))
        self.__eliminate()

    def lacks(self, card):
        self.lacks_set.add(card)
        self.__eliminate()

    def __eliminate(self):
        # Narrow eliminations
        pass
