
import card
from prompt import SetPrompt, BooleanPrompt, IntegerPrompt

class Play:

    def run(self, game):
        self.game = game

        while True:
            self.accusation()

    def accusation(self):
        accuser = self.game.prompt(SetPrompt('Accuser:', self.game.players))

        accusation = self.__prompt_accusation()
        passed = self.__prompt_passes(accuser, accusation)
        self.__lack_passed(passed, accusation)

        for player in self.game.players:
            print("{}\n    {}".format(player, str(player.hand).replace("\n", "\n    ")))
        print("Conviction:")
        print("    " + str(self.game.conviction).replace("\n", "\n    "))

    def __prompt_accusation(self):
        cards = set()
        while len(cards) < 3:
            types = set(card.TYPES) - set([c.type for c in cards])

            # Render types in "x, y, and z" format
            sentence_types = list(types)
            if len(sentence_types) > 1:
                sentence_types[-1] = 'or {}'.format(sentence_types[-1])
            delimiter = ', ' if len(sentence_types) != 2 else ' '

            cards.add(self.game.prompt(SetPrompt(
                '{} card:'.format(delimiter.join(sentence_types).capitalize()),
                [c for c in self.game.cards if c.type in types]
            )))
        return cards

    def __prompt_passes(self, exception, cards):
        other_players = self.game.players - set([exception])
        passed = set()
        answered = self.game.prompt(BooleanPrompt('Did anyone answer:'))
        if answered:
            answerer = self.game.prompt(SetPrompt('Who:', other_players))
            answerer.hand.elimination(cards)

            if exception == self.game.me:
                answerer.hand.has(self.game.prompt(SetPrompt('Card shown:', cards - answerer.hand.lacks_set)))

            passed_count = self.game.prompt(IntegerPrompt('How many passed:', len(other_players)))
            while len(passed) < passed_count:
                passed.add(self.game.prompt(SetPrompt('Passed player:', other_players, passed)))
        else:
            passed = other_players
        return passed

    def __lack_passed(self, players, cards):
        for player in players:
            for c in cards:
                player.hand.lacks(c)
