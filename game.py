
from setup import Setup
from play import Play
from hand import Hand

class Game:

    prompt_history = []

    def play(self):
        self.players = []
        self.cards = []
        self.me = []
        self.conviction = None

        setup = Setup()
        setup.run(self)

        play = Play()
        play.run(self)

    def prompt(self, prompt):
        while True:
            response = input(prompt.question)
            prompt.respond(response)
            if prompt.satisfied():
                self.prompt_history.append(response)
                break
        return prompt.response()
