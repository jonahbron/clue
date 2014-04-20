
class Hand:

    def __init__(self, count=0, game=None, has=[], lacks=[]):
        self.count = max(count, len(has))
        self.has_set = set(has)
        self.lacks_set = set(lacks)
        self.eliminations_set = set()
        self.game = game

    def has(self, card):
        self.has_set.add(card)
        self.lacks_set.discard(card)
        self.__check_count()
        self.__eliminate()
        self.game.notify_has(self, card)

    def elimination(self, cards):
        self.eliminations_set.add(frozenset(cards))
        self.__eliminate()

    def lacks(self, card):
        self.lacks_set.add(card)
        self.has_set.discard(card)
        self.__eliminate()
        self.game.notify_lacks(self, card)

    def __check_count(self):
        if len(self.has_set) >= self.count:
            for c in self.game.cards - self.has_set:
                self.lacks(c)

    def __eliminate(self):
        for elimination in set(self.eliminations_set):
            for card in self.has_set:
                if card in elimination:
                    self.eliminations_set.discard(elimination)

        for elimination in set(self.eliminations_set):
            for card in self.lacks_set:
                if card in elimination:
                    self.eliminations_set.discard(elimination)
                    self.eliminations_set.add(frozenset(set(elimination) - set([card])))

        for elimination in set(self.eliminations_set):
            if len(elimination) == 1:
                self.eliminations_set.discard(elimination)
                self.has(list(elimination)[0])

    def __repr__(self):
        return "Has: {}\nLacks: {}\nOne ofs: \n    {}".format(
            list(self.has_set),
            list(self.lacks_set),
            "\n    ".join([str(list(sub)) for sub in self.eliminations_set]))
