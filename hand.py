
class Hand:

    def __init__(self, count=0, has=[], lacks=[]):
        self.count = max(count, len(has))
        self.has = has
        self.lacks = lacks
