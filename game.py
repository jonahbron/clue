
from setup import Setup
from play import Play
from hand import Hand

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

    def notify_has(self, has_hand, card):
        for hand in self.hands - set([has_hand]):
            hand.lacks(card)
