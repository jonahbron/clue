
class Hand:

    def __init__(self, count=0, game=None, has=[], lacks=[]):
        self.count = max(count, len(has))
        self.has_set = set(has)
        self.lacks_set = set(lacks)
        self.eliminations_set = set()
        self.game = game

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
        for elimination in set(self.eliminations_set):
            for card in self.has_set:
                if card in elimination:
                    self.eliminations_set.remove(elimination)

        for elimination in set(self.eliminations_set):
            for card in self.lacks_set:
                if card in elimination:
                    self.eliminations_set.remove(elimination)
                    self.eliminations_set.add(frozenset(set(elimination) - set([card])))

        for elimination in set(self.eliminations_set):
            if len(elimination) == 1:
                self.eliminations_set.remove(elimination)
                self.has(elimination.pop())
