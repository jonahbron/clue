
import card
from prompt import SetPrompt, BooleanPrompt, IntegerPrompt

class Play:

    def run(self, game):
        self.game = game

        while True:
            self.accusation()

    def accusation(self):
        accuser = self.game.prompt(SetPrompt('Accuser:', self.game.players))
        other_players = self.game.players - set([accuser])
        cards = set()
        for card_type in card.TYPES:
            cards.add(self.game.prompt(SetPrompt(
                'Type {} card:'.format(card_type),
                [card for card in self.game.cards if card.type == card_type],
                cards
            )))

        passed = set()
        answered = self.game.prompt(BooleanPrompt('Did anyone answer:'))
        if answered:
            answerer = self.game.prompt(SetPrompt('Who:', other_players))
            answerer.hand.elimination(cards)

            passed_count = self.game.prompt(IntegerPrompt('How many passed:', len(other_players)))
            while len(passed) < passed_count:
                passed.add(self.game.prompt(SetPrompt('Passed player:', other_players, passed)))
        else:
            passed = other_players

        for player in passed:
            for c in cards:
                player.hand.lacks(c)
