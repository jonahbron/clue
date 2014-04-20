
from setup import Setup
from play import Play
from hand import Hand

class Game:

    prompt_history = []
    prompt_queue = []

    def play(self):
        self.players = set()
        self.cards = set()
        self.me = None
        self.conviction = None

        self.gamefile = open('gamefile.txt', 'r')
        self.prompt_queue = [x.rstrip("\n") for x in self.gamefile]
        self.gamefile.close()
        self.gamefile = open('gamefile.txt', 'w')

        setup = Setup()
        setup.run(self)

        play = Play()
        play.run(self)

    def prompt(self, prompt):
        while True:
            if len(self.prompt_queue) > 0:
                response = self.prompt_queue.pop(0)
            else:
                response = input(prompt.question)

            prompt.respond(response)
            if prompt.satisfied():
                self.prompt_history.append(response)
                self.gamefile.write(response + "\n")
                break

        return prompt.response()
