import card
from card import Card
from player import Player
from hand import Hand
from prompt import Prompt, IntegerPrompt, SetPrompt
import pprint

class Setup:

    def run(self, game):
        self.game = game
        self.cards_accounted_for = 0

        self.setup_conviction()
        self.initialize_cards()
        self.setup_me()
        self.setup_opponents()
        self.setup_my_cards()

    def setup_conviction(self):
        self.game.conviction = Hand(card.COUNT_TYPES)
        self.cards_accounted_for += card.COUNT_TYPES

    def initialize_cards(self):
        self.game.cards.add(Card(card.TYPE_ROOM, 'Lounge'))
        self.game.cards.add(Card(card.TYPE_ROOM, 'Dining Room'))
        self.game.cards.add(Card(card.TYPE_ROOM, 'Kitchen'))
        self.game.cards.add(Card(card.TYPE_ROOM, 'Ballroom'))
        self.game.cards.add(Card(card.TYPE_ROOM, 'Conservatory'))
        self.game.cards.add(Card(card.TYPE_ROOM, 'Billiard Room'))
        self.game.cards.add(Card(card.TYPE_ROOM, 'Library'))
        self.game.cards.add(Card(card.TYPE_ROOM, 'Study'))
        self.game.cards.add(Card(card.TYPE_ROOM, 'Hall'))

        self.game.cards.add(Card(card.TYPE_PERSON, 'Miss Scarlett'))
        self.game.cards.add(Card(card.TYPE_PERSON, 'Coloniel Mustard'))
        self.game.cards.add(Card(card.TYPE_PERSON, 'Misses White'))
        self.game.cards.add(Card(card.TYPE_PERSON, 'Mister Green'))
        self.game.cards.add(Card(card.TYPE_PERSON, 'Misses Peacock'))
        self.game.cards.add(Card(card.TYPE_PERSON, 'Professor Plumb'))

        self.game.cards.add(Card(card.TYPE_WEAPON, 'Lead Pipe'))
        self.game.cards.add(Card(card.TYPE_WEAPON, 'Wrench'))
        self.game.cards.add(Card(card.TYPE_WEAPON, 'Knife'))
        self.game.cards.add(Card(card.TYPE_WEAPON, 'Revolver'))
        self.game.cards.add(Card(card.TYPE_WEAPON, 'Candlestick'))
        self.game.cards.add(Card(card.TYPE_WEAPON, 'Rope'))

    def setup_me(self):
        name = self.game.prompt(Prompt('Your name:'))
        card_count = self.game.prompt(IntegerPrompt('Count your cards:', len(self.game.cards) - self.cards_accounted_for))
        player = Player(name, Hand(card_count, game=self.game))
        self.game.me = player
        self.game.players.add(player)
        self.cards_accounted_for += card_count

    def setup_opponents(self):
        while self.cards_accounted_for < len(self.game.cards):
            cards_left = len(self.game.cards) - self.cards_accounted_for
            name = self.game.prompt(Prompt('Opponent name:'))
            card_count = self.game.prompt(IntegerPrompt(
                'Cards held by {} ({} left):'.format(
                    name,
                    cards_left
                ),
                cards_left
            ))
            player = Player(name, Hand(card_count, game=self.game))
            self.game.players.add(player)
            self.cards_accounted_for += card_count

    def setup_my_cards(self):
        while len(self.game.me.hand.has_set) < self.game.me.hand.count:
            self.game.me.hand.has(self.game.prompt(SetPrompt('Your card:', self.game.cards, exclude=self.game.me.hand.has_set)))
