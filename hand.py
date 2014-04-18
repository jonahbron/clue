
class Hand:

    def __init__(self, count=0, has=[], lacks=[]):
        self.count = max(count, len(has))
        self.has_set = has
        self.lacks_set = lacks

    def has(self, card):
        self.has_set.append(card)
        # Remove from lacks
        # Narrow options
        # Make sure unique in has
        # Notify all other hands
