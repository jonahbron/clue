
from setup import Setup
from play import Play
from hand import Hand
import card

class Game:

    prompt_history = []
    prompt_queue = []

    def play(self):
        self.players = set()
        self.hands = set()
        self.cards = set()
        self.me = None
        self.conviction = None

        self.gamefile = open('gamefile.txt', 'r+', buffering=1)
        self.prompt_queue = [x.rstrip("\n") for x in self.gamefile]

        setup = Setup()
        setup.run(self)

        play = Play()
        play.run(self)

    def prompt(self, prompt):
        while True:
            if len(self.prompt_queue) > 0:
                response = self.prompt_queue.pop(0)
                from_input = False
            else:
                response = input(prompt.question)
                from_input = True

            prompt.respond(response)
            if prompt.satisfied():
                if from_input:
                    self.gamefile.write(response + "\n")
                self.prompt_history.append(response)
                break

        return prompt.response()

    def notify_has(self, has_hand, _card):
        for hand in self.hands - set([has_hand]):
            hand.lacks(_card)

        player_hands = [h for h in self.hands if h != self.conviction]
        conviction_types = [c.type for c in self.conviction.has_set]
        unconvicted_types = [t for t in card.TYPES if t not in conviction_types]
        for card_type in unconvicted_types:
            for c in [c for c in self.cards if c.type == card_type]:
                all_lack = True
                for hand in player_hands:
                    if c not in hand.lacks_set:
                        all_lack = False
                if all_lack:
                    self.conviction.has(c)
