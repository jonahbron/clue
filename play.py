
import card
from prompt import SetPrompt, BooleanPrompt

class Play:

    def run(self, game):
        self.game = game

        while True:
            self.accusation()

    def accusation(self):
        accuser = self.game.prompt(SetPrompt('Accuser:', self.game.players))
        cards = []
        for card_type in card.TYPES:
            cards.append(self.game.prompt(SetPrompt(
                'Type {} card:'.format(card_type),
                [card for card in self.game.cards if card.type == card_type],
                cards
            )))

        answered = self.game.prompt(BooleanPrompt('Did anyone answer:'))
        if answered:
            print("Someone answered")
        # Input passes and answers
